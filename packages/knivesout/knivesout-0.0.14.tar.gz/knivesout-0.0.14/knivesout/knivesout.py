#!/usr/bin/env python3
import sys
import ast
import json
import asyncio
import os
import time
from abc import ABC, abstractmethod
from typing import Callable, Dict, List, Optional, Set, Tuple, Union

import codefast as cf
import fire
import pandas as pd
from codefast.asyncio import async_render
from codefast.io.osdb import osdb
from codefast.logger import setpath
from pydantic import BaseModel
import pprint

setpath('/tmp/kod.log')

_db = osdb('/var/log/knivesout.db')


class _ProgramState(object):
    init = 'init'
    running = 'running'
    restart = 'restart'
    stopped = 'stopped'
    error = 'error'
    deleted = 'deleted'


class Config(BaseModel):
    program: str
    directory: str
    command: str
    stdout_file: Optional[str] = '/tmp/stdout.txt'
    stderr_file: Optional[str] = '/tmp/stderr.txt'
    max_restart: Optional[int] = 3
    cur_restart: Optional[int] = 0
    cur_state: Optional[str] = ''
    next_state: Optional[str] = ''
    start_time: Optional[str] = pd.Timestamp.now().strftime(
        '%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return str(self.dict())

    def __eq__(self, other):
        return self.program == other.program

    def __hash__(self):
        return hash(self.program)


def parse_config_from_file(config_file: str) -> Config:
    """Parse config file and return a dictionary of parameters."""
    try:
        js = cf.js(config_file)
        return Config(**js)
    except json.decoder.JSONDecodeError as e:
        cf.warning("json decode error: {}".format(e))
        js = ast.literal_eval(cf.io.reads(config_file))
        return Config(**js)
    except Exception as e:
        cf.warning(e)
        return None


def parse_config_from_string(config_string: str) -> Config:
    """Parse config file and return a dictionary of parameters."""
    import ast
    try:
        js = ast.literal_eval(config_string)
        return Config(**js)
    except Exception as e:
        cf.error({
            'msg': 'parse_config_from_string error',
            'config_string': config_string,
            'error': str(e)
        })
        return None


class ConfigManager(object):

    @staticmethod
    def load() -> List[Config]:
        configs = _db.get('configs') or '[]'
        configs = [Config(**c) for c in ast.literal_eval(configs)]
        return list(set(configs))

    @staticmethod
    def add(config: Config):
        configs = ConfigManager.load()
        configs = [c for c in configs if c != config]
        configs.append(config)
        ConfigManager.save(configs)

    @staticmethod
    def delete_by_program_name(name: str):
        ConfigManager.stop_by_program_name(name)
        while True:
            config = next(
                (c for c in ConfigManager.load() if c.program == name), None)
            if config and config.cur_state == _ProgramState.stopped:
                break
        configs = ConfigManager.load()
        configs_new = [c for c in configs if c.program != name]
        ConfigManager.save(configs_new)

    @staticmethod
    def stop_by_program_name(name: str):
        configs = ConfigManager.load()
        configs_new = []
        command = ''
        for c in configs:
            if c.program == name:
                c.next_state = _ProgramState.stopped
                c.cur_state = _ProgramState.running  # Give control to RunningSwitcher
                c.start_time = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
                command = c.command
            configs_new.append(c)
        ConfigManager.save(configs_new)
        return command

    @staticmethod
    def save(configs: List[Config]):
        configs = list(set(configs))
        configs = [c.dict() for c in configs]
        _db.set('configs', configs)


class AbstractStateSwitcher(ABC):

    def _update_config(self, config: Config):
        ConfigManager.add(config)

    @abstractmethod
    def is_match(self) -> bool: ...

    @abstractmethod
    async def _switch(self): ...

    async def switch(self, config: Config):
        self.config = config
        if not self.is_match():
            return
        await self._switch()

    async def get_pids(self, config: Config) -> List[str]:
        pids = os.popen(
            f"ps -ef | grep '{config.command}' | grep -v grep | awk '{{print $2}}'"
        ).read().split()
        return pids

    async def is_running(self, config: Config):
        pids = await self.get_pids(config)
        return len(pids) > 0

    async def stop_execute(self, config: Config):
        cf.info(f"Stop running [{config.command}]")
        pids = await self.get_pids(config)
        self.config.cur_state = _ProgramState.stopped
        self.config.next_state = _ProgramState.stopped
        self._update_config(self.config)

        for pid in pids:
            os.system(f"kill -9 {pid}")

    async def restart_execute(self, config: Config):
        """stop and then start program"""
        cf.info(f"restarting [{config.command}]")
        pids = await self.get_pids(config)
        for pid in pids:
            os.system(f"kill -9 {pid}")
        self.config.cur_state = _ProgramState.init
        self.config.next_state = _ProgramState.running
        self.config.cur_restart = 0
        self._update_config(self.config)


class InitSwitcher(AbstractStateSwitcher):

    def is_match(self):
        return self.config.cur_state == _ProgramState.init and self.config.next_state == _ProgramState.running

    async def _switch(self):
        await self.start_execute(self.config)

    def check_log_file_permission(self, config: Config):
        if not os.path.exists(config.stdout_file):
            return True

        if not os.path.exists(config.stderr_file):
            return True

        if not os.access(config.stdout_file, os.W_OK):
            cf.error(f"stdout_file {config.stdout_file} is not writable")
            return False

        if not os.access(config.stderr_file, os.W_OK):
            cf.error(f"stderr_file {config.stderr_file} is not writable")
            return False
        return True

    def to_error_state(self, config: Config):
        config.cur_state = _ProgramState.error
        config.next_state = _ProgramState.error
        self._update_config(config)

    def to_running_state(self, config: Config):
        config.cur_state = _ProgramState.running
        self._update_config(config)

    async def start_execute(self, config: Config):
        if config.cur_restart >= config.max_restart:
            cf.error(
                f"restart [{config.command}] reached retry limit {config.max_restart}"
            )
            self.config.cur_state = _ProgramState.error
            self.config.next_state = _ProgramState.error
            self._update_config(self.config)

        else:
            cf.info(f'start config: {config}')
            if not self.check_log_file_permission(config):
                self.to_error_state(config)
                return
            else:
                self.to_running_state(config)

            cmd = f"{config.command} 1>> {config.stdout_file} 2>> {config.stderr_file}"
            cf.info(f"Start running [{config.command}]")
            is_running = await self.is_running(config)

            if is_running:
                cf.info({'msg': 'already running', 'config': config})
            else:
                self.config.start_time = pd.Timestamp.now().strftime(
                    '%Y-%m-%d %H:%M:%S')
                self._update_config(self.config)

                os.chdir(config.directory)
                proc = await asyncio.create_subprocess_shell(
                    cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE)
                stdout, stderr = await proc.communicate()

                # Failed to start
                msg = {'stdout': stdout, 'stderr': stderr, 'return code': proc.returncode}
                cf.info(msg)
                if int(proc.returncode) not in (0, 1, 2):
                    msg = (f"[{config.command}] is either terminated or failed to start, "
                           "return code: {proc.returncode}")
                    cf.warning(msg)

                config.cur_restart += 1
                self._update_config(self.config)


class RunningSwitcher(AbstractStateSwitcher):

    def is_match(self):
        return self.config.cur_state == _ProgramState.running

    async def _switch(self):
        if self.config.next_state == _ProgramState.stopped:
            await self.stop_execute(self.config)

        elif self.config.next_state == _ProgramState.restart:
            await self.restart_execute(self.config)

        elif self.config.next_state == _ProgramState.running:
            is_running = await self.is_running(self.config)
            if is_running:
                return
            self.config.cur_state = _ProgramState.init
            self.config.next_state = _ProgramState.running
            self._update_config(self.config)


class StopSwitcher(AbstractStateSwitcher):

    def is_match(self) -> bool:
        return self.config.cur_state == _ProgramState.stopped

    async def _switch(self):
        if self.config.next_state in (_ProgramState.init,
                                      _ProgramState.running):
            self.config.cur_state = _ProgramState.init
            self.config.next_state = _ProgramState.running
            self._update_config(self.config)


class Context(object):
    _SWITCHERS = [RunningSwitcher(), InitSwitcher(), StopSwitcher()]

    @staticmethod
    async def run():
        configs = ConfigManager.load()
        for config in configs:
            for switcher in Context._SWITCHERS:
                asyncio.create_task(switcher.switch(config))


class AbstractExecutor(ABC):

    @abstractmethod
    def serve(self, *args, **kwargs):
        pass

    @abstractmethod
    def is_match(self) -> bool:
        pass

    def exec(self, *args, **kwargs):
        if self.is_match():
            self.serve(*args, **kwargs)


class DaemonInitiator(AbstractExecutor):
    def __init__(self) -> None:
        super().__init__()
        self.service_str = """[Unit]
Description=Knives out daemon service
After=network.target

[Service]
Type=simple
User={}
WorkingDirectory=/tmp/
ExecStart={}
StandardOutput=append:/tmp/systemkod.log
StandardError=append:/tmp/systemkod.log
Restart=on-failure
RestartPreventExitStatus=0 255

[Install]
WantedBy=multi-user.target"""
        self.user = None
        self.exec_start = None
        self.service_location = '/etc/systemd/system/knivesd.service'
        self.tmp_location = '/tmp/knivesd.service'

    def serve(self, *args, **kwargs):
        if self.configure_systemd():
            self.enable_systemd()
            self.start_systemd()

    def _get_user(self) -> str:
        return cf.shell('whoami').strip()

    def _get_exec_start(self) -> str:
        return cf.shell('which knivesd').strip()

    def _get_previous_config(self) -> str:
        if not os.path.exists(self.service_location):
            return None
        with open(self.service_location, 'r') as f:
            return f.read()

    def _get_new_config(self) -> str:
        self.user = self._get_user() or ''
        self.exec_start = self._get_exec_start() or ''
        if not self.user:
            cf.warning('cannot get user')
        if not self.exec_start:
            cf.warning('cannot get exec start')
        self.service_str = self.service_str.format(self.user, self.exec_start + ' run')
        return self.service_str

    def configure_systemd(self):
        old, new = self._get_previous_config(), self._get_new_config()
        if old == new:
            return True

        try:
            cf.io.write(self.service_str, self.service_location)
        except PermissionError:
            cf.warning(f'Permission denied when writing to {self.service_location}')
            cf.io.write(self.service_str, self.tmp_location)
            cf.info('Run ` sudo cp /tmp/knivesd.service /etc/systemd/system/knivesd.service ` to install')
            return False
        return True

    def start_systemd(self):
        os.system('systemctl start knivesd')
        cf.info('knivesd started')

    def enable_systemd(self):
        os.system('systemctl daemon-reload')
        os.system('systemctl enable knivesd')
        cf.info('knivesd enabled')

    def is_match(self):
        return len(sys.argv) == 2 and sys.argv[1] == 'init'


class DaemonRunner(AbstractExecutor):
    async def _loop(self):
        while True:
            await asyncio.sleep(1)
            await Context.run()

    def serve(self, *args, **kwargs):
        asyncio.run(self._loop())

    def is_match(self):
        return len(sys.argv) == 2 and sys.argv[1] == 'run'


def serve_knivesd():
    """Run as a daemon."""
    executors = [DaemonInitiator(), DaemonRunner()]
    for executor in executors:
        executor.exec()


def knivesd():
    serve_knivesd()


class KnivesCli(object):
    """Terminal cli powered by fire."""

    def _check_daemon_status(self) -> None:
        """Check daemon status."""
        cf.info('Checking daemon status...')
        status = cf.shell('systemctl status knivesd')
        if not 'active (running)' in status:
            cf.warning('knivesd is not running')

    def _identify_config(self, proc_or_file: str) -> Config:
        """Find config by proc or file name

        Args:
            proc_or_file (str): proc or file name

        Returns:
            _type_: Config
        """
        self._check_daemon_status()

        configs = ConfigManager.load()
        config = next((c for c in configs if c.program == proc_or_file), None)
        file_exist = os.path.exists(proc_or_file) and os.path.isfile(proc_or_file)

        if file_exist:
            c_file = parse_config_from_file(proc_or_file)

            config = next((c for c in configs if c.program == c_file.program), None)
            # Tasks with same program name is forbidden
            if config:
                cf.info(f"Program [{config.program}] already exists")
            config = c_file

        if not config:
            cf.warning(f"Program [{proc_or_file}] not found")
            sys.exit(1)
        return config

    def start(self, proc_or_file: str):
        """Start a program."""
        config = self._identify_config(proc_or_file)

        if config:
            config.cur_state = _ProgramState.init
            config.next_state = _ProgramState.running
            c = next((_ for _ in ConfigManager.load() if _ == config), None)
            if c:
                config.start_time = c.start_time

            config.cur_restart = 0
            ConfigManager.add(config)
            cf.info(f"[{config.command}] started")
        else:
            cf.info(f"config not found: {proc_or_file}")

    def stop(self, proc_or_file: str):
        """Stop a program."""
        config = self._identify_config(proc_or_file)
        program = ConfigManager.stop_by_program_name(config.program)
        cf.info(f"[{program}] stopped")

    def restart(self, proc: str):
        """Restart a program."""
        config = self._identify_config(proc)
        config.cur_state = _ProgramState.running
        config.next_state = _ProgramState.restart
        ConfigManager.add(config)
        cf.info(f"[{config.program}] restarted")

    def _get_all_configs(self, proc: str = None) -> List[Config]:
        return cf.lis(ConfigManager.load())\
            .filter(lambda c: proc is None or c.program == proc)\
            .sort(lambda c: (c.cur_state, c.program)).data

    def _get_printable_config(self, configs: List[Config]) -> str:

        def _uptime_str(c: Config):
            uptime = pd.Timestamp.now() - pd.Timestamp(c.start_time)
            seconds = uptime.total_seconds()
            return cf.fp.readable_time(seconds)

        def _format(data: List[Tuple]) -> str:
            return ' | '.join([f'{d[1]:<{d[0]}}' for d in data])

        def _printable_text(c: Config) -> str:
            state = c.cur_state
            mapping = {_ProgramState.running: cf.fp.green,
                       _ProgramState.error: cf.fp.red,
                       _ProgramState.stopped: cf.fp.cyan,
                       _ProgramState.init: cf.fp.cyan}
            state = mapping.get(state, cf.fp.cyan)(state.upper())
            return _format([
                (7, state),
                (13, c.program),
                (15, _uptime_str(c)),
                (30, c.command),
            ])

        contents = [(7, 'state'), (13, 'proc_alias'),
                    (15, 'uptime'), (30, 'command')]
        text = _format(contents)
        texts = [text, '-'*66]

        cf.lis(configs).map(_printable_text).each(texts.append)
        return '\n'.join(texts)

    def status(self, proc: str = None):
        """Show status of a program."""
        print(self._get_printable_config(self._get_all_configs(proc)))

    def st(self, proc: str = None):
        """Alias of status"""
        self.status(proc)

    def delete(self, proc: str):
        """Delete a program."""
        ConfigManager.delete_by_program_name(proc)
        cf.info(f"[{proc}] deleted")

    def configs(self, proc: str = None):
        """Show configs of a program."""
        configs = self._get_all_configs(proc)
        for config in configs:
            pprint.pprint(config.dict())

    def cs(self, proc: str = None):
        """Show configs of a program."""
        self.configs(proc)


def knivescli():
    fire.Fire(KnivesCli)


if __name__ == '__main__':
    knivescli()

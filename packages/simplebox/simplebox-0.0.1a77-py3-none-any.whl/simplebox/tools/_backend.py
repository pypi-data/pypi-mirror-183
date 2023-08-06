#!/usr/bin/env python
# -*- coding:utf-8 -*-
import inspect
import os
import platform
from locale import getpreferredencoding
from pathlib import Path
from subprocess import Popen, PIPE
from sys import executable
from typing import Callable

from ..char import StringBuilder, String
from ..config import LogConfig
from ..log import LoggerFactory
from ..utils import ObjectsUtils, StringUtils

_logger = LoggerFactory.get_logger("backend")


class _Backend(object):
    """
    Create a new process and then run it in background mode
    """

    def __init__(self, func: Callable, log_path: str or Path = None):
        self.__message_builder = StringBuilder()
        self.__message_builder.append(f"Backend run [{platform.system()}]: ")
        if not issubclass(type(func), Callable):
            raise TypeError(f"expected is function, got a {type(func).__name__}")
        self.__func_name = func.__name__
        self.__func = func
        if self.__func_name == "<lambda>":
            raise TypeError("cannot be a lambda function")
        self.__log_path = None
        if log_path and (issubclass(type(log_path), str) or issubclass(type(log_path), Path)):
            p = Path(log_path)
            if not p.is_absolute():
                self.__log_path = LogConfig.dir.joinpath(log_path)
            else:
                self.__log_path = p
        self.__frame = inspect.stack()[2]
        self.__run_path = Path(self.__frame[1]).parent
        self.__module_name = Path(self.__frame[1]).stem
        # When find for processes, you can filter by filtering the keywords in commandline (flag here).
        self.__flag = f"simplebox-backend-run-{self.__module_name}-{self.__func_name}-{ObjectsUtils.generate_random_str(6)}"
        self.__import_statement = StringBuilder(sep=" ", start='"', end='"')
        self.__import_statement.append("import") \
            .append(self.__module_name + ";") \
            .append(f"{self.__module_name}.{self.__func_name}()").append(" #").append(self.__flag)

        os_name = os.name
        exec_func_name = f"_Backend__run_{os_name.lower()}_cmd"
        exec_func = getattr(self, exec_func_name, None)
        if exec_func:
            exec_func()
            self.__message_builder.append(";").append(f"process tag => {self.__flag}")
            _logger.info(self.__message_builder.string())
        else:
            raise RuntimeError(f"Unsupported operating systems: {os_name}")

    def __run_nt_cmd(self):
        """
        windows run
        """
        cmd = StringBuilder(sep=" ")
        cmd.append(executable) \
            .append("-c") \
            .append(self.__import_statement.string())
        if self.__log_path:
            cmd.append(">").append(self.__log_path)
        self.__sub_process(cmd.string())
        self.__get_pid_nt()

    def __run_posix_cmd(self):
        """
        unix-like run
        """
        cmd = StringBuilder(sep=" ")
        cmd.append("nohup") \
            .append(executable) \
            .append("-c") \
            .append(self.__import_statement.string())\
            .append(">")
        if self.__log_path:
            cmd.append(self.__log_path)
        else:
            cmd.append("/dev/null")
        cmd.append("2>&1 &")
        self.__sub_process(cmd.string())
        self.__get_pid_unix()

    def __get_pid_nt(self):
        cmd = StringBuilder(sep=" ")
        cmd.append("wmic") \
            .append("process") \
            .append("where") \
            .append("\"") \
            .append("commandline") \
            .append("like") \
            .append(f"'%%{self.__flag}%%'")\
            .append("and")\
            .append("name")\
            .append("!=")\
            .append("'WMIC.exe'")\
            .append("and")\
            .append("name")\
            .append("like")\
            .append("'python%'") \
            .append("\"") \
            .append("get") \
            .append("processid")
        process = Popen(cmd.string(), shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding=getpreferredencoding(False))
        out, err = process.communicate()
        if process.returncode == 0 and "ProcessId" in out:
            message = StringUtils.trip(out.split('ProcessId')[1])
        else:
            message = f"error: {err}"
        self.__message_builder.append(f"Pid => {message}")

    def __get_pid_unix(self):
        cmd = StringBuilder(sep=" ")
        cmd.append("ps")\
            .append("-ef")\
            .append("|")\
            .append("grep")\
            .append("-v")\
            .append("grep")\
            .append("|")\
            .append("grep")\
            .append("-w")\
            .append(self.__flag)\
            .append("|")\
            .append("awk")\
            .append("'{print $2}'")
        process = Popen(cmd.string(), shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE,
                        encoding=getpreferredencoding(False))
        out, err = process.communicate()
        if StringUtils.is_not_empty(out):
            message = StringUtils.trip(out)
        else:
            message = f"error: {err}"
        self.__message_builder.append(f"Pid => {message}")

    def __sub_process(self, cmd: String):
        Popen(cmd, cwd=self.__run_path, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)


def backend(func: Callable, log_path: str or Path = None):
    """
    Create a new process and then run it in background mode
    """
    _Backend(func, log_path)


__all__ = [backend]

# coding:utf-8
import inspect
import os
from typing import Any, List, Tuple
from unittest.mock import DEFAULT

from loguru import logger

LOGFILE = '/tmp/cf.log'
MAXSIZE = '100 MB'
MAXBACKUP = 3


def rename_rotated_file(filepath: str):
    for i in range(MAXBACKUP, 1, -1):
        old_path = LOGFILE + f'.{i-1}'
        new_path = LOGFILE + f'.{i}'
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
    os.rename(filepath, LOGFILE + '.1')


def set_log_path(_logger, log_path: str):
    try:
        _logger.add(log_path,
                    rotation=MAXSIZE,
                    retention=MAXBACKUP,
                    enqueue=True,
                    colorize=True,
                    backtrace=True,
                    diagnose=True,
                    compression=rename_rotated_file)
    except PermissionError:
        set_log_path(_logger, log_path + 'x')


def setpath(logpath: str):
    set_log_path(logger, logpath)


setpath(LOGFILE)


def info(msg: str, *args, **kwargs):
    """ Please use string-format to restrict unexpected behaviour. 
    """
    msg = str(msg)
    if args:
        msg += f" {args}"

    if kwargs:
        msg += f" {kwargs}"
    logger.opt(depth=1).info(msg)


trace = logger.trace
debug = logger.debug
success = logger.success
warning = logger.warning
error = logger.exception
critical = logger.critical
exception = logger.exception

log_colors_config = {
    'DEBUG': 'white',
    'INFO': 'bold_cyan',
    'WARNING': 'bold_yellow',
    'ERROR': 'bold_red',
    'CRITICAL': 'bold_red',
}


class Logger(object):
    def debug(self, *message):
        pass

    def info(self, *message):
        pass

    def warning(self, *message):
        pass

    def error(self, *message):
        pass

    def critical(self, *message):
        self.console('critical', *message)

    def __repr__(self) -> str:
        d = {'level': self._level, 'logname': self._logname}
        return str(d)


def test():
    frames = inspect.stack()
    print(frames)
    Logger().info("Line 6666")


if __name__ == "__main__":
    log = Logger()
    log.info("测试1")
    log.debug("测试2")
    log.warning("warning")
    log.error("error")
    log.critical("critical")
    test()

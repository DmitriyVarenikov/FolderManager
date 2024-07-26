from typing import Optional
import time

from configuration import Config


class BaseFile:
    _DIR = Config.DIR_TYPE_NAME
    _FILE = Config.FILE_TYPE_NAME

    def __init__(self,
                 path: str,
                 name: str,
                 is_dir: bool = True,
                 last_edit: Optional[str] = None,
                 size: Optional[str] = None,
                 visible: bool = True):
        self._path = path
        self._name = name
        self._is_dir = is_dir
        self._last_edit = last_edit
        self._size = size
        self._visible = visible

    def set_last_edit(self, value: float, *args) -> None:
        readable_time = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(value))
        self._last_edit = readable_time

    @property
    def is_dir(self):
        return self._is_dir

    @is_dir.setter
    def is_dir(self, value: bool):
        self._is_dir = value

    def get_type_name(self) -> str:
        return (self._FILE, self._DIR)[self._is_dir]

    @property
    def name(self):
        return self._name

    @property
    def last_edit(self):
        return self._last_edit

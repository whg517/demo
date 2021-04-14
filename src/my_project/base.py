"""
Base
"""
import asyncio
from asyncio import AbstractEventLoop
from typing import Optional


class BaseExecutor:
    """
    Base executor.
    """
    def __init__(
        self,
        name: str,
        pid: str,
        loop: Optional[AbstractEventLoop] = None,
    ):
        self.name = name
        self.pid = pid
        self._loop = loop

    @property
    def loop(self) -> AbstractEventLoop:
        """Current event loop"""
        if self._loop:
            return self._loop
        return asyncio.get_running_loop()

    def run(self) -> None:
        """Run executor."""
        raise NotImplementedError

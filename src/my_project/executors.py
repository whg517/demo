"""
Executors.
"""
from asyncio import AbstractEventLoop
from typing import Optional

from my_project.base import BaseExecutor


class DockerExecutor(BaseExecutor):
    """
    Docker Executor
    """
    def __init__(
        self,
        name: str,
        pid: str,
        loop: Optional[AbstractEventLoop] = None,
    ):
        super().__init__(name, pid, loop)

        self._client = 'Fake docker client'

    def run(self) -> None:
        """Run executor."""
        print(f'{id(self.loop)} Run executor')

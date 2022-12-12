import asyncio
from fastapi import FastAPI
from typing import Optional


class State(object):
    def __init__(self, loop: asyncio.AbstractEventLoop, config: dict):
        super().__init__()
        self.loop: asyncio.AbstractEventLoop = loop
        self.config: dict = config
        self.app: Optional[FastAPI] = None

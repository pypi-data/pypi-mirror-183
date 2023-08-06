"""Asynchronous python library to control 2N devices."""

from __future__ import annotations

import logging
import aiohttp

from typing import Any
from datetime import datetime, timedelta
from .const import CONNECT_ERRORS

from .model import Py2NDeviceData, Py2NConnectionData

from .exceptions import (
    NotInitialized,
    Py2NError,
    DeviceConnectionError,
    InvalidAuthError,
)

from .utils import get_info, get_status

_LOGGER = logging.getLogger(__name__)


class Py2NDevice:
    def __init__(self, aiohttp_session, connection_data: Py2NConnectionData):
        """Device init."""
        self.aiohttp_session: aiohttp.ClientSession = aiohttp_session
        self.connection_data = connection_data
        self._info: dict[str, Any] | None = None
        self._status: dict[str, Any] | None = None
        self._initializing: bool = False
        self._last_error: Py2NError | None = None
        self.initialized: bool = False

    @classmethod
    async def create(
        cls, aiohttp_session: aiohttp.ClientSession, options: Py2NConnectionData
    ) -> Py2NDevice:
        """Device creation."""
        instance = cls(aiohttp_session, options)
        await instance.initialize()
        return instance

    async def initialize(self) -> None:
        """Device initialization."""
        if self._initializing:
            raise RuntimeError("Already initializing")

        self._initializing = True
        self.initialized = False

        try:
            await self.update()
            self.initialized = True
        finally:
            self._initializing = False

    async def update(self) -> Py2NDeviceData:
        ip = self.options.ip_address

        try:
            self._info = await get_info(self.aiohttp_session, self.options)
            self._status = await get_status(self.aiohttp_session, self.options)

            data = Py2NDeviceData()
            data.model = self._info["variant"]
            data.serial = self._info["serialNumber"]
            data.uptime = datetime.now() - timedelta(seconds=self._status["upTime"])
        except InvalidAuthError as err:
            self._last_error = err
            _LOGGER.debug("host %s: error: %r", ip, self._last_error)
            raise
        except CONNECT_ERRORS as err:
            self._last_error = DeviceConnectionError(err)
            _LOGGER.debug("host %s: error: %r", ip, self._last_error)
            raise DeviceConnectionError(err) from err

        return self

    @property
    def ip_address(self) -> str:
        """Device ip address."""
        return self.options.ip_address

    @property
    def info(self) -> str:
        """Get device info."""
        if not self.initialized:
            raise NotInitialized

        return self._info

    @property
    def status(self) -> str:
        """Get device status."""
        if not self.initialized:
            raise NotInitialized

        if self._status is None:
            raise InvalidAuthError

        return self._status

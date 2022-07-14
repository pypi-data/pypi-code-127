#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : Ampel-ZTF/ampel/ztf/alert/ZiHealpixAlertSupplier.py
# License           : BSD-3-Clause
# Author            : mf <mf@physik.hu-berlin.de>
# Date              : 15.11.2021
# Last Modified Date: 27.04.2022
# Last Modified By  : jn <jnordin@physik.hu-berlin.de>

from datetime import datetime
from typing import Any, Callable, Dict, List, Literal, Sequence, Union

from ampel.alert.BaseAlertSupplier import BaseAlertSupplier
from ampel.protocol.AmpelAlertProtocol import AmpelAlertProtocol
from ampel.ztf.alert.ZiAlertSupplier import ZiAlertSupplier
from ampel.ztf.alert.load.ZTFHealpixAlertLoader import ZTFHealpixAlertLoader
from numpy import isin

class ZiHealpixAlertSupplier(BaseAlertSupplier):
    """
    Iterable class that, for each alert payload provided by the underlying alert_loader,
    returns an AmpelAlertProtocol instance.
    """

    # Override default
    deserialize = None

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def set_healpix(self, nside: int, healpix: List[int], time: datetime, with_history: bool = False) -> None:
        """
        Define the Healpix map property which will be used by the loader.
        Nominally set in Loader config?
        """
        if isinstance(self.alert_loader, ZTFHealpixAlertLoader):
            self.alert_loader.set_source( nside=nside, pixels=healpix, time=time, with_history=with_history )
        else:
            raise TypeError(f"set_healpix called with alert_loader {type(self.alert_loader).__name__}")


#    def set_time(self, time: datetime) -> None:
#        self.alert_loader.set_time(time)  # type: ignore[attr-defined]

    def __next__(self) -> AmpelAlertProtocol:
        """
        :returns: a dict with a structure that AlertConsumer understands
        :raises StopIteration: when alert_loader dries out.
        :raises AttributeError: if alert_loader was not set properly before this method is called
        """

        d = self._deserialize(next(self.alert_loader))  # type: ignore
        return ZiAlertSupplier.shape_alert_dict(d)

# This file is part of daf_butler.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (http://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
from astropy.table import Table as AstropyTable

from .._butler import Butler
from ..cli.utils import sortAstropyTable


class _Table:
    """Aggregates DataIds and creates an astropy table with one DataId per
    row. Eliminates duplicate rows.

    Parameters
    ----------
    dataIds : `iterable` [ ``DataId`` ]
        The DataIds to add to the table.
    """

    def __init__(self, dataIds):
        # use dict to store dataIds as keys to preserve ordering
        self.dataIds = dict.fromkeys(dataIds)

    def getAstropyTable(self, order):
        """Get the table as an astropy table.

        Returns
        -------
        table : `astropy.table.Table`
            The dataIds, sorted by spatial and temporal columns first, and then
            the rest of the columns, with duplicate dataIds removed.
        order : `bool`
            If True then order rows based on DataIds.
        """
        # Should never happen; adding a dataset should be the action that
        # causes a _Table to be created.
        if not self.dataIds:
            raise RuntimeError("No DataIds were provided.")

        dataId = next(iter(self.dataIds))
        dimensions = list(dataId.full.keys())
        columnNames = [str(item) for item in dimensions]

        # Need to hint the column types for numbers since the per-row
        # constructor of Table does not work this out on its own and sorting
        # will not work properly without.
        typeMap = {float: np.float64, int: np.int64}
        columnTypes = [typeMap.get(type(value)) for value in dataId.full.values()]

        rows = [[value for value in dataId.full.values()] for dataId in self.dataIds]

        table = AstropyTable(np.array(rows), names=columnNames, dtype=columnTypes)
        if order:
            table = sortAstropyTable(table, dimensions)
        return table


def queryDataIds(repo, dimensions, datasets, where, collections, order_by, limit, offset):
    # Docstring for supported parameters is the same as Registry.queryDataIds

    butler = Butler(repo)
    results = butler.registry.queryDataIds(
        dimensions, datasets=datasets, where=where, collections=collections
    )

    if order_by:
        results.order_by(*order_by)
    if limit > 0:
        if offset <= 0:
            offset = None
        results.limit(limit, offset)

    if len(results.graph) > 0:
        table = _Table(results)
        return table.getAstropyTable(not order_by)
    else:
        return None

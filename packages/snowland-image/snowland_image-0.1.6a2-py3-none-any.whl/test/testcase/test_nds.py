# -*- coding: utf-8 -*-


from typing import Union, List, Iterable

import numpy as np
from astartool.common import BIT_EACH
from astartool.project import time_clock

npa = np.array


def dms_to_nds(dms: Union[np.ndarray, List, float]):
    if isinstance(dms, (np.ndarray, list)):
        nds = ((1 << 32) / 360 * npa(dms)).astype(np.uint64)
    else:
        nds = npa([(1 << 32) / 360 * dms]).astype(np.uint64)
    return nds


def nds_to_morton(nds_lon, nds_lat):
    if isinstance(nds_lon, (np.uint, int)) and isinstance(nds_lat, (np.uint, int)):
        mortonCode = 0
        x, y = nds_lon, nds_lat
        if y < 0:
            y += 0x7FFFFFFF

        y <<= 1

        for i in range(32):
            mortonCode |= x & BIT_EACH[i * 2]
            x <<= 1
            mortonCode |= y & BIT_EACH[i * 2 + 1]
            y <<= 1

        return mortonCode
    if isinstance(nds_lon, list):
        nds_lon = npa(nds_lon)
    if isinstance(nds_lat, list):
        nds_lat = npa(nds_lat)

    assert len(nds_lon) == len(nds_lat)
    bit = 1
    morton_code = np.zeros_like(nds_lat, dtype=np.uint64)
    x, y = nds_lon, nds_lat
    y[y < 0] += 0x7FFFFFFF
    y <<= 1
    for i in range(32):
        morton_code |= x & bit
        x <<= 1
        bit <<= 1
        morton_code |= y & bit
        y <<= 1
        bit <<= 1
    return morton_code


def get_tile_id(lon: (np.ndarray, List[float]), lat: (np.ndarray, List[float]), level=13):
    """
    获得level层的瓦片
    """
    if isinstance(lon, Iterable):
        ndsLon = dms_to_nds(lon)
        ndsLat = dms_to_nds(lat)

        morton = nds_to_morton(ndsLon, ndsLat)
        ntile_id = (((morton >> (2 * (31 - level))) & 0xffffffff) + (1 << (16 + level)))
    else:
        tileids = get_tile_id([lon], [lat], level=level)
        ntile_id = tileids[0]
    return ntile_id


def nds_to_morton2(nds_lon, nds_lat):
    if isinstance(nds_lon, (np.uint, int)) and isinstance(nds_lat, (np.uint, int)):
        mortonCode = 0
        x, y = nds_lon, nds_lat
        if y < 0:
            y += 0x7FFFFFFF

        y <<= 1

        for i in range(32):
            mortonCode |= x & BIT_EACH[i * 2]
            x <<= 1
            mortonCode |= y & BIT_EACH[i * 2 + 1]
            y <<= 1

        return mortonCode
    if isinstance(nds_lon, list):
        nds_lon = npa(nds_lon)
    if isinstance(nds_lat, list):
        nds_lat = npa(nds_lat)

    assert len(nds_lon) == len(nds_lat)
    x, y = nds_lon, nds_lat
    y[y < 0] += 0x7FFFFFFF
    y <<= 1

    x_new = [int(f"{'0'.join(bin(xi)[2:][::-1])}", 2) for xi in x]
    y_new = [int(('0'.join(bin(yi)[2:][::-1])), 2) for yi in y]

    morton_code2 = npa([xi | yi for xi, yi in zip(x_new, y_new)])
    bit = 1
    morton_code = np.zeros_like(nds_lat, dtype=np.uint64)
    xii = np.zeros_like(nds_lat, dtype=np.uint64)
    yii = np.zeros_like(nds_lat, dtype=np.uint64)
    for i in range(32):
        xii |= x & bit
        x <<= 1
        bit <<= 1
        yii |= y & bit
        y <<= 1
        bit <<= 1
    morton_code = xii | yii
    return morton_code2


def get_tile_id2(lon: (np.ndarray, List[float]), lat: (np.ndarray, List[float]), level=13):
    """
    获得level层的瓦片
    """
    if isinstance(lon, Iterable):
        ndsLon = dms_to_nds(lon)
        ndsLat = dms_to_nds(lat)

        morton = nds_to_morton2(ndsLon, ndsLat)
        ntile_id = (((morton >> (2 * (31 - level))) & 0xffffffff) + (1 << (16 + level)))
    else:
        tileids = get_tile_id([lon], [lat], level=level)
        ntile_id = tileids[0]
    return ntile_id


if __name__ == '__main__':
    x = [119.135671785614] * 20
    y = [34.5738355769335] * 20
    s1 = time_clock()
    z = get_tile_id(x, y, 13)
    e1 = time_clock()
    z2 = get_tile_id2(x, y, 13)
    e2 = time_clock()
    print(e1 - s1, e2 - e1)
    for t1, t2 in zip(z, z2):
        assert t1 == 557386867
        assert t2 == 557386867

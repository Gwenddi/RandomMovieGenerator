from utils import *
from utils.util import df, typeList


def getMapData():
    print("找国家")
    maplist = typeList('拍摄国家')
    mapobj = {}

    for i in maplist:
        if mapobj.get(i, -1) == -1:
            mapobj[i] = 1
        else:
            mapobj[i] += 1
    print(mapobj.keys())
    print(mapobj.values())
    return list(mapobj.keys()), list(mapobj.values())

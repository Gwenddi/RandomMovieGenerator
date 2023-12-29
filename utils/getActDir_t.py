from utils import *
from utils.util import df, typeList, typeList_kang

def getDirData20():
    dirlist = typeList_kang ('导演')
    dirobj = {}

    for i in dirlist:
        if dirobj.get(i , -1) == -1:
            dirobj[i]=1
        else:
            dirobj[i] += 1
    #排序
    dirsobj = sorted(dirobj.items(),key = lambda x: x[1],reverse=True)[:20]
    print(dirsobj)
    row = []
    columns = []
    for i in dirsobj:
        row.append(i[0])
        columns.append(i[1])

    return row,columns,dirsobj

def getActData20():
    actlist = typeList ('演员')
    actobj = {}

    for i in actlist:
        if actobj.get(i , -1) == -1:
            actobj[i]=1
        else:
            actobj[i] += 1
    #排序
    actsobj = sorted(actobj.items(),key = lambda x: x[1],reverse=True)[:20]
    print(actsobj)
    row = []
    columns = []
    for i in actsobj:
        row.append(i[0])
        columns.append(i[1])

    return row,columns,actsobj

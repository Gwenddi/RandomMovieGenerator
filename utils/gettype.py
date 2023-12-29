from utils import *
from utils.util import df, typeList

def getTypeData():
    print("找类型")
    typelist = typeList ('电影类型')
    typeobj = {}

    for i in typelist:
        if typeobj.get(i , -1) == -1:
            typeobj[i]=1
        else:
            typeobj[i] += 1
    typeData = []
    #更改数据类型
    for key,item in typeobj.items():
        typeData.append({
            'name':key,
            'value':item
        })
    return typeData


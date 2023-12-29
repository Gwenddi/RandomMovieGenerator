from utils import *
from utils.util import df, typeList


def getTypeEcharData():
    typelist = typeList('电影类型')
    typeObj = {}
    for i in typelist:
        if typeObj.get(i,-1) == -1:
            typeObj[i] = 1
        else:
            typeObj[i]+=1
    typeEcharData = []
    for key,value in typeObj.items():
        typeEcharData.append({
            'name':key,
            'value':value
        })
    return typeEcharData

def getRateEcharData():
    ratelist = df['评分'].map(lambda x:float(x)).values
    ratelist.sort()
    rateObj = {}
    for i in ratelist:
        if rateObj.get(i,-1) == -1:
            rateObj[i] = 1
        else:
            rateObj[i]+=1
    return list(rateObj.keys()),list(rateObj.values())

def getTableData():
    return df.values



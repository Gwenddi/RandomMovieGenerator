from utils.util import df, typeList
import datetime


def getAllTypes():
    types = list(set((typeList('电影类型'))))
    filtered_types = [t for t in types if t != '情色' and t != '同性' and t != '儿童']
    return filtered_types


def getAllRateDatabyType(type):
    if type == 'all':
        rateList = typeList('评分')
    else:
        # print('here, and type is ' + type)
        typelist = df['电影类型'].map(lambda x: x.split(sep=' '))
        # print(typelist)
        oldRateList = typeList('评分')
        rateList = []
        # i为电影标号+1
        for i, item in enumerate(typelist):
            if type in item:
                rateList.append(oldRateList[i])

                # print(' i=' + str(i) + ' item=' + str(item))

    rateList.sort()
    rateObj = {} # 创建空字典
    for i in rateList: # i是评分
        if rateObj.get(i, -1) == -1:
            rateObj[i] = 1
        else:
            rateObj[i] += 1

    typeEcharData = [] # 创建空列表
    for key, value in rateObj.items():
        typeEcharData.append({
            'name': key, # 评分
            'value': value # 电影数量
        })
    return list(rateObj.keys()), list(rateObj.values()), typeEcharData

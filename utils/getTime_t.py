from utils.util import df, typeList
import datetime


# 定义函数 getYearData 用于获取电影年份数据并进行统计
def getYearData():
    # 从 DataFrame 中获取电影年份列表，并将年份转换为整数类型
    timeList = list(df['电影年份'].map(lambda x: int(x[:4])))

    # 对年份列表进行排序
    timeList.sort()

    # 初始化空字典用于存储年份统计结果
    timObj = {}

    # 统计每个年份的数量
    for i in timeList:
        if timObj.get(i, -1) == -1:
            timObj[i] = 1
        else:
            timObj[i] = timObj[i] + 1

    # 返回年份列表和对应数量的列表
    return list(timObj.keys()), list(timObj.values())


getYearData()

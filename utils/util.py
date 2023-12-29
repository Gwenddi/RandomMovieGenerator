import pandas as pd
from sqlalchemy import create_engine

con = create_engine('mysql+pymysql://root:021231@localhost:3306/dbmovie')

df = pd.read_sql('select * from movie', con=con)


def typeList (type):
    type = df[type].values
    if type is not None:
        type = [x for x in type if x is not None]  # 过滤掉None值
        type = list(map(lambda x: x.split(' '), type))
        typeList = []
        for i in type:
            for j in i:
                typeList.append(j)
        # print(typeList)
        return typeList
    else:
        return []

def typeList_kang (type):
    type = df[type].values
    if type is not None:
        type = [x for x in type if x is not None]  # 过滤掉None值
        type = list(map(lambda x: x.split('/'), type))
        typeList = []
        for i in type:
            for j in i:
                typeList.append(j)
        # print(typeList)
        return typeList
    else:
        return []


typeList('演员')
# def df():
#     return df

from pymysql import *

conn = connect(host='localhost',user='root',password='021231',database='dbmovie',port=3306)
cursor = conn.cursor()
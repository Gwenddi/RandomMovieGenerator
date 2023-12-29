import re
import urllib.error
import urllib.request

import xlwt
from bs4 import BeautifulSoup

# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则（字符串的模式）
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让换行符包含在字符中
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 影片概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")  # 列名
    # 写入第一行
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    # 写入数据
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存


def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数，10次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):  # 查找符合要求的字符串，形成列表
            data = []  # 保存一部电影的所有信息
            item = str(item)
            # 影片详情链接
            link = re.findall(findLink, item)[0]  # re库用来通过正则表达式查找指定字符串
            data.append(link)  # 添加链接
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)  # 添加图片
            titles = re.findall(findTitle, item)  # 片名可能只有一个中文名，没有外国名
            if len(titles) == 2:
                ctitle = titles[0]  # 添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/", "").replace(u'\xa0', '')  # 去掉无关的符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])
                data.append("")  # 外国名字留空
            rating = re.findall(findRating, item)[0]
            data.append(rating)  # 添加评分
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)  # 添加评价人数
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)  # 添加概述
            else:
                data.append(" ")  # 留空
            bd = re.findall(findBd, item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?", " ", bd)  # 去掉<br/>
            bd = re.sub('/', ' ', bd)  # 替换/
            data.append(bd.replace(u'\xa0', '').strip())  # 去掉空格
            datalist.append(data)  # 把处理好的一部电影信息放入datalist
    return datalist


def askURL(url):
    # 模拟浏览器头部信息
    head = {
        # 用户代理
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


def main():
    baseurl = "https://movie.douban.com/top250?start="
    savepath = "豆瓣电影Top250.xls"
    dbpath = "movieTop250.db"
    # 1.爬取网页
    datalist = getData(baseurl)
    # 2.保存数据
    saveData(datalist, savepath)


if __name__ == "__main__":
    main()
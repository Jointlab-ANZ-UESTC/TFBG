from pyh import *

''' 

前边朋友的code

'''

# 创建HTML页面
page = PyH("Results for Project 0")

# 创建展示数据表格
tb = page << table('', border='2', align='center')
tb << caption('Results for urls(status 200)')
with open('./results.csv', 'r') as f1:
    for line in f1:
        tb << tr(td(line.lstrip()))

#保存html文件
page.printOut('re.html')




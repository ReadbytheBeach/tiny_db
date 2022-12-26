from tinydb import TinyDB
from tinydb import Query
import datetime
import mypy

db = TinyDB('db.json')
# db.insert({'product':'ARS540','recording': '20221122_204218.mps4'})
# db.insert({'product':'ARS540','recording': '20221122_204657.mps4'})
# db.insert({'product':'ARS540','recording': '20221122_205106.mps4'})
# db.insert({'product':'ARS620','recording': '20221130_092047.mps4'})

print("Please input the product, for example input --- ARS540")
product_name = input()
print('product_name type =', type(product_name))
print("please input the recording name, for example input ---20221122_204218.mps4")
recording_name = input
print('recording_name type = ', type(recording_name))
print("please input the testcase type, for example input --- ACC forward")
recording_name = input
print('recording_name type = ', type(recording_name))

# 现在是一条条手动输入
# 允许
# ToDo: 连续输入多条
# ToDo：自动做文件夹遍历（条件是命名规则要事先定好，文件夹也要事先固定好）
db.insert({'product': product_name,'recording': recording_name, 'test_case': testcase_name})

for item in db:
    print(item)



'''

# 搜索特定数据
search_rec = Query()
search_result = db.search ((search_rec.product == 'ARS540') & (search_rec.recording == '20221122_204657.mps4'))
print ('search_result =', search_result)

# 删除特定数据
search_rec = Query()
db.remove(search_rec.product == 'ARS540' and search_rec.recording == '20221122_204657.mps4')


# ToDo:  写一个主函数
# ToDo:  做一个前端输入界面： 给出示例 （只要recording放进文件夹，自动遍历，并存入数据库---事先要规定格式）
# ToDo:  比较已有的记录，发现重复，则提示已有该条记录
# ToDo:  自动定期更新数据库
# ToDo:  进一步做数据分析
# ToDo:  做一个可视化报告
'''
import pymysql  # 导入 pymysql

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", user="controlarm",
                     password="123456", db="controlarm", port=3306,charset='utf8mb4')

# 使用cursor()方法获取操作游标
cur = db.cursor()

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
def dataSql(itemid,title,picture,oe,market,judege,sold):
    sql = "insert into baseinfo(itemid,title,picture,oe,market,judege,sold) values(%s,%s,%s,%s,%s,%s,%s)"
    try:
        res = cur.execute(sql,(itemid,title,picture,oe,market,judege,sold))  # 执行sql语句
        db.commit()
    except Exception as e:
        print(e)
    finally:
        pass
        # cur.close()  # 关闭连接

def saleInfoInsert(itemid,price,Quantity,Date_of_Purchase):
    # 插入销售记录页面全部内容
    sql = "insert into salesrecoder(itemid,price,Quantity,Date_of_Purchase) values(%s,%s,%s,%s)"
    try:
        res = cur.execute(sql,(itemid,price,Quantity,Date_of_Purchase))  # 执行sql语句
        db.commit()
    except Exception as e:
        print(e)
    finally:
        pass
        # cur.close()  # 关闭连接
def saleInfoSpecific(itemid,store_link,current_price,description,store_name,oem,internumber,othernumber,sold):
    sql = "insert saleinfospecific(itemid,store_link,current_price,description,store_name,oem,internumber,othernumber,sold_number)" \
          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        res = cur.execute(sql,(itemid,store_link,current_price,description,store_name,oem,internumber,othernumber,sold))  # 执行sql语句
        db.commit()
    except Exception as e:
        print(e)
    finally:
        pass


if __name__ == '__main__':
    dataSql(itemid=1,title=2,picture=3,oe=4,market=5)
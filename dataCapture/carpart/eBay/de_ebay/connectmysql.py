import pymysql  # 导入 pymysql

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", user="root",
                     password="root", db="controlarm", port=3306,charset='utf8mb4')

# 使用cursor()方法获取操作游标
cur = db.cursor()
#
# create table baseinfo(index int PRIMARY KEY auto_increment, title VARCHAR(500), itemid VARCHAR(100), picture VARCHAR(500))

#     primary key(col_name),
#     index idx_name(col_name1,col_name2,...),

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
def dataSql(itemid,title,picture,oe,market,judege,sold):
    sql = "insert into de_carparts(itemid,title,picture,oe,market,judege,sold) values(%s,%s,%s,%s,%s,%s,%s)"
    try:
        res = cur.execute(sql,(itemid,title,picture,oe,market,judege,sold))  # 执行sql语句
        db.commit()
    except Exception as e:
        print(e)
    finally:
        pass
        # cur.close()  # 关闭连接


def shopDataInsert(storename,produce_type,itemid, title, picture,  market,sold):
    sql = "insert into shop_data_control_arm(storename,produce_type,itemid,title,picture,market,sold) values(%s,%s,%s,%s,%s,%s,%s)"
    try:
        cur.execute(sql, (storename,produce_type,itemid, title, picture,  market,sold))  # 执行sql语句
        db.commit()
    except Exception as e:
        print(e)
    finally:
        pass
        # cur.close()  # 关闭连接



def dataLook(oe):
    sql = "select * from moogcontrolarm where moogoe like '%{}%'".format(oe)
    cur.execute(sql)
    res = cur.fetchall()
    print(res)
    return res

if __name__ == '__main__':
    # dataSql(itemid=1,title=2,picture=3,oe=4,market=5)
    dataLook(oe='kljljklk')
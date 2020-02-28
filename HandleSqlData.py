
def handle_data():
    # 导入pymysql模块
    import pymysql as pmy
    print('\n' + '*' * 100)
    # 连接database
    conn = pmy.connect('localhost', 'root', '123wangchao', 'its_cops', charset='utf8')
    # 得到一个可以执行SQL语句的光标对象
    cur = conn.cursor()
    # 定义要执行的SQL语句
    # sql1 删除重复数据
    print('开始删除重复数据..................')
    sql1 = '''DELETE t1 FROM entinfo t1, entinfo t2 WHERE t1.Name = t2.Name and t1.IndexID > t2.IndexID'''
    # sql2，sql3充值index
    print('开始充值索引Index.................')
    sql2 = '''SET @i=0;'''
    sql3 = '''UPDATE `chelianwang2` SET `IndexID`=(@i:=@i+1);'''
    print('数据处理完成......................')
    # 执行SQL语句
    cur.execute(sql1)
    cur.execute(sql2)
    cur.execute(sql3)
    # 提交事务
    conn.commit()
    # 关闭光标对象
    cur.close()
    # 关闭数据库连接
    conn.close()
    print('*' * 100 + '\n')

if __name__ == "__main__":
    handle_data()

#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:SaveDataToSql.py
@Time:2020/02/26 13:25:52
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:存储公司工商注册信息到数据库中
'''

# 导入pymysql模块
import pymysql as pmy
import time
from tqdm import tqdm


def save_to_sql(entlist):
    print('\n' + '*' * 100)
    start_time = time.time()
    # 连接database
    conn = pmy.connect('localhost',
                       'root',
                       '123wangchao',
                       'its_cops',
                       charset='utf8')
    # 得到一个可以执行SQL语句的光标对象
    cur = conn.cursor()
    # 定义要执行的SQL语句
    sql = """ insert into entinfo (Name,Reg_Capital,Paid_Capital,Legal_Rep,Manage_State,Old_Name,Industry,Credit_Code,Tax_Id_No,Com_Reg_No,Org_Code,Reg_Auth,Estab_Date,Cop_Type,Business_Ierm,admin_Div,Annual_Inspect,Reg_Addr,Business_Scope) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    print('开始将数据存入数据库..............')
    pbar = tqdm(entlist, desc='共计%s家企业' % len(entlist), leave=True, position=1)
    for ent in pbar:
        cur.execute(
            sql,
            (ent.Name, ent.Reg_Capital, ent.Paid_Capital, ent.Legal_Rep,
             ent.Manage_State, ent.Old_Name, ent.Industry, ent.Credit_Code,
             ent.Tax_Id_No, ent.Com_Reg_No, ent.Org_Code, ent.Reg_Auth,
             ent.Estab_Date, ent.Cop_Type, ent.Business_Ierm, ent.admin_Div,
             ent.Annual_Inspect, ent.Reg_Addr, ent.Business_Scope))
        # 提交事务
        conn.commit()
    # 关闭光标对象
    cur.close()
    # 关闭数据库连接
    conn.close()
    end_time = time.time()
    print('数据存储完成................')
    print('总耗时%s' % (end_time - start_time))
    print('*' * 100 + '\n')


if __name__ == "__main__":
    pass
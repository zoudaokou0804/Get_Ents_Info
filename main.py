#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:main.py
@Time:2020/02/27 22:34:58
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:读取txt中的公司注册信息链接，解析数据，存入数据库
'''

from tqdm import tqdm
from EntClass import EntItem
from SaveDataToSql import save_to_sql
from HandleSqlData import handle_data
from Parse_Ent_Info import parse_buiness_data
import time
# import multiprocessing


def get_link_from_txt(path):
    print('\n' + '*' * 100)
    print('获取公司注册信息链接...............')
    with open(path, 'r', encoding='utf-8') as f:
        link_list = f.readlines()
    pbar = tqdm(range(len(link_list)),
                desc='共计%s家企业' % len(link_list),
                leave=True,
                position=1)
    for i in pbar:
        link_list[i] = 'h' + link_list[i].split(':h')[1].replace('\n', '')
    print('所有公司链接获取完成...............')
    print('*' * 100 + '\n')
    return link_list


def loads_data(link_list):
    start_time = time.time()
    entlist = []
    print('\n' + '*' * 100)
    print('获取公司对象中.............')
    # pool = multiprocessing.Pool(processes=4)
    pbar = tqdm(link_list,
                desc='共计%s家企业' % len(link_list),
                leave=True,
                position=1)
    for link in pbar:
        try:
            entdata = parse_buiness_data(link)
            # entdata = pool.apply_async(parse_buiness_data,(link,))
            ent = EntItem(entdata)
            entlist.append(ent)
        except Exception as e:
            continue
    # pool.close()
    # pool.join()
    end_time = time.time()
    print('公司对象获取完成.............')
    print('总耗时%s' % (end_time - start_time))
    print('*' * 100 + '\n')
    return entlist


if __name__ == "__main__":
    path = r'智慧交通linklist.txt'
    link_list = get_link_from_txt(path)
    entlist = loads_data(link_list)
    save_to_sql(entlist)
    handle_data()

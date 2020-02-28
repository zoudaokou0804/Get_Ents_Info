#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:Get_Ents_Link.py
@Time:2020/02/26 13:32:10
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:获取所有查找公司的详情页（工商注册信息）的链接，并写入txt中
'''
"""
搜索公司关键词函数，返回关键词用于构建查询URL
"""
import time
import requests
from fake_useragent import UserAgent
import json
from tqdm import tqdm
import os


def choose_kw():
    # 选择要查询的公司关键字
    print('\n' + '*' * 100)
    skw_no = input('确认搜索关键词：1、车联网 2、智能网联 3、智能交通 4、智慧交通 5、其他' + '\n' + "请选择序号：")
    skw = ''
    if skw_no == '1':
        skw = '车联网'
    elif skw_no == '2':
        skw = '智能网联'
    elif skw_no == '3':
        skw = '智能交通'
    elif skw_no == '4':
        skw = '智慧交通'
    elif skw_no == '5':
        skw = input('请输入搜索关键词：' + '\n')
    else:
        print('又出什么幺蛾子')
    print('*' * 100 + '\n')
    return skw


skw = choose_kw()
"""
由用户选择的关键词构建查询企业的初始URL
返回结果：为关键词查询企业数据连接URL
"""


def Gen_Url(data, page=1):
    url = 'https://xin.baidu.com/s/l?q={}&t=0&p={}&s=10&o=0&f={}&_={}'.format(
        skw, str(page), data, str(int(time.time() * 1000)))
    url = url.replace(' ', '')
    return url


def get_index_num(data):
    url = Gen_Url(data)
    user_agent = UserAgent().random
    # 注意：请求头中一定要加入cookie，否则会一直重定位
    headers = {
        'User-Agent':
        user_agent,
        "Cookie":
        "BIDUPSID=97AC18FF352A68DC1E8EA57FB51E094D; PSTM=1562157172; BAIDUID=920CFE34646FF4D8F95ADF2CBC90A5C3:FG=1; __cfduid=d438a78ae491903dee1e76d9101740e7d1573713887; BDUSS=g0UWxzUm8tSWczbX5Wem41VUlUSmtjZTFyYWdFZUthRWF0T35BRU9iSnNwMUJlRVFBQUFBJCQAAAAAAAAAAAEAAADuTBAQem91ZGFva291MDgwNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGwaKV5sGiled2; MCITY=-%3A; H_WISE_SIDS=138596_141183_100806_140348_139405_138496_139812_135846_141003_138945_138470_140853_139281_138878_137979_140174_131247_132551_137746_138165_138883_140259_141368_140631_140202_139296_138585_139177_139625_140114_136196_140591_140579_133847_140792_140065_131423_141174_140368_139575_110085_140325_127969_141108_140593_140864_139882_137252_127416_138313_138426_141194_138943_140683_141190_140597_138752_140962; BDPPN=6d3ed66cd2a6c5d8551eddf942d3c27c; log_guid=b00bfc61669d0923aa97510cd7e0c0fa; delPer=0; PSINO=3; Hm_lvt_baca6fe3dceaf818f5f835b0ae97e4cc=1582285149,1582416533,1582502721,1582535854; Hm_lpvt_baca6fe3dceaf818f5f835b0ae97e4cc={}; BDRCVFR[yxi3RW9Ex4T]=mk3SLVN4HKm; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0"
        .format(str(int(time.time() * 1000))),
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    Data = json.loads(html)
    totalNumFound = Data['data']['totalNumFound']
    totalPageNum = Data['data']['totalPageNum']
    facets = Data['data']['facets']
    try:
        select_index = list(facets.keys())[0]
    except Exception as e:
        select_index = ''
        print('出错了：没有更细的指标了', e)
        continue
    try:
        select_values = Data['data']['facets'][select_index]['values']
    except Exception as e:
        select_values = {}
        print('出错了：', e)
        continue
    return totalNumFound, select_index, select_values, totalPageNum


def get_onepage_links(page, data):
    url = Gen_Url(data, page)
    user_agent = UserAgent().random
    headers = {
        'User-Agent':
        user_agent,
        "Cookie":
        "BIDUPSID=97AC18FF352A68DC1E8EA57FB51E094D; PSTM=1562157172; BAIDUID=920CFE34646FF4D8F95ADF2CBC90A5C3:FG=1; __cfduid=d438a78ae491903dee1e76d9101740e7d1573713887; BDUSS=g0UWxzUm8tSWczbX5Wem41VUlUSmtjZTFyYWdFZUthRWF0T35BRU9iSnNwMUJlRVFBQUFBJCQAAAAAAAAAAAEAAADuTBAQem91ZGFva291MDgwNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGwaKV5sGiled2; MCITY=-%3A; H_WISE_SIDS=138596_141183_100806_140348_139405_138496_139812_135846_141003_138945_138470_140853_139281_138878_137979_140174_131247_132551_137746_138165_138883_140259_141368_140631_140202_139296_138585_139177_139625_140114_136196_140591_140579_133847_140792_140065_131423_141174_140368_139575_110085_140325_127969_141108_140593_140864_139882_137252_127416_138313_138426_141194_138943_140683_141190_140597_138752_140962; BDPPN=6d3ed66cd2a6c5d8551eddf942d3c27c; log_guid=b00bfc61669d0923aa97510cd7e0c0fa; delPer=0; PSINO=3; Hm_lvt_baca6fe3dceaf818f5f835b0ae97e4cc=1582285149,1582416533,1582502721,1582535854; Hm_lpvt_baca6fe3dceaf818f5f835b0ae97e4cc={}; BDRCVFR[yxi3RW9Ex4T]=mk3SLVN4HKm; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0"
        .format(str(int(time.time() * 1000))),
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    Data = json.loads(html)
    resluts = Data['data']['resultList']
    links = {}
    pbar3 = tqdm(resluts,
                 desc='该页共%s家企业' % len(resluts),
                 leave=False,
                 position=3)
    for reslut in pbar3:
        pid = reslut['pid']
        name = reslut['titleName']
        ent_url = 'https://xin.baidu.com/detail/compinfo?pid=%s' % pid
        links[name] = ent_url
        # time.sleep(0.1) # 减轻服务器压力
    return links


def get_allpages_links(data):
    pages = get_index_num(data)[3]
    links_total = {}
    pbar2 = tqdm(range(1, pages + 1),
                 desc='共计%s页' % pages,
                 leave=False,
                 position=2)
    for page in pbar2:
        links = get_onepage_links(page, data)
        links_total.update(links)
    return links_total


all_ents_links = {}


def get_allents_links(data):
    global all_ents_links
    print('\n' + '*' * 100)
    start_time = time.time()
    vaules_tuple = get_index_num(data)
    totalNumFound = vaules_tuple[0]
    if totalNumFound == 101:
        select_index = vaules_tuple[1]
        select_values = vaules_tuple[2]
        pbar1 = tqdm(select_values, desc=select_index, leave=True, position=1)
        for value_data in pbar1:
            value = value_data['value']
            count = int(str(value_data['count']).replace('+', ''))
            data = json.loads(data)
            data[select_index] = value
            data = str(data).replace('None', 'null')
            data = data.replace('\'', '\"')
            if count > 100:
                all_ents_links = get_allents_links(data)
                # all_ents_links.extend(links_total)
            else:
                # totalPageNum = vaules_tuple[3]
                links_total = get_allpages_links(data)
                all_ents_links.update(links_total)
    else:
        # totalPageNum = vaules_tuple[3]
        links_total = get_allpages_links(data)
        all_ents_links.update(links_total)
    end_time = time.time()
    print('公司详情页链接下载完成.............')
    print('总耗时%s' % (end_time - start_time))
    print('*' * 100 + '\n')
    return all_ents_links


"""
将所有链接写入到txt中
"""


def loads_to_txt(datalist):
    print('\n' + '*' * 100)
    start_time = time.time()
    with open(os.path.join(os.path.dirname(__file__), '%slinklist.txt' % skw),
              'w',
              encoding='utf-8') as f:
        for name, url in datalist.items():
            f.write(name + ':' + url + '\n')
    end_time = time.time()
    print('数据写入完成.............')
    print('总耗时%s' % (end_time - start_time))
    print('*' * 100 + '\n')


if __name__ == "__main__":
    data = '{"provinceCode":null,"cityCode":null}'
    x = get_allents_links(data)
    loads_to_txt(x)

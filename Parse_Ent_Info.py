#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:Parse_Ent_Info.py
@Time:2020/02/27 20:10:18
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:解析公司工商注册信息
'''

import requests
from lxml import etree
from fake_useragent import UserAgent


def parse_buiness_data(url):
    data = []
    user_agent = UserAgent().random
    # 注意：请求头中一定要加入cookie，否则会一直重定位
    headers = {
        'User-Agent': user_agent,
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html_tree = etree.HTML(response.text)
    x0 = html_tree.xpath('//span[@class="entName"]/text()')[0]
    data.append(x0)
    trlist = html_tree.xpath(
        '//table[@class="zx-detail-basic-table"]//tbody/tr')
    count = len(trlist)
    for i in range(count - 2):
        try:
            x1 = trlist[i].xpath('./td[2]/text()')[0]
        except Exception as e:
            # print(e)
            x1 = 0
        try:
            x2 = trlist[i].xpath('./td[4]/text()')[0]
        except Exception as e:
            # print(e)
            x2 = 0
        data.append(x1)
        data.append(x2)
    x3 = trlist[count - 2].xpath('./td[2]/text()')[0]
    x4 = trlist[count - 1].xpath('./td[2]//p/@data-content')[0]
    data.append(x3)
    data.append(x4)
    data[1] = data[1].replace(',', '').split('万')[0]
    data[2] = data[2].replace(',', '').split('万')[0]
    return data


if __name__ == "__main__":
    url = r'https://xin.baidu.com/detail/compinfo?pid=xlTM-TogKuTwABnS-*9c5nQj58VU7a3W0Qmd'
    parse_buiness_data(url)
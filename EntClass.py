#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:EntClass.py
@Time:2020/02/26 13:14:22
@Author:zoudaokou
@Version:1.0
@Contact:xxxxxx
@desc:新建公司类
'''

# 最原始定义类的方法，但是这种方法就是一旦参数特别多，后面给类实例化复制特别麻烦
# 有个偷懒的办法，直接传入列表或元祖
# class EntItem:
#     def __init__(self, Name, Reg_Capital, Paid_Capital, Legal_Rep,
#                  Manage_State, Old_Name, Industry, Credit_Code, Tax_Id_No,
#                  Com_Reg_No, Org_Code, Reg_Auth, Estab_Date, Cop_Type,
#                  Business_Ierm, admin_Div, Annual_Inspect, Reg_Addr,
#                  Business_Scope, province, city):
#         self.Name = Name  # 公司名称
#         self.Reg_Capital = Reg_Capital  # 注册资本
#         self.Paid_Capital = Paid_Capital  # 实缴资本
#         self.Legal_Rep = Legal_Rep  # 法定代表人
#         self.Manage_State = Manage_State  # 经营状态
#         self.Old_Name = Old_Name  # 曾用名
#         self.Industry = Industry  # 所属行业
#         self.Credit_Code = Credit_Code  # 统一社会信用代码
#         self.Tax_Id_No = Tax_Id_No  # 纳税人识别号
#         self.Com_Reg_No = Com_Reg_No  # 工商注册号
#         self.Org_Code = Org_Code  # 组织机构代码
#         self.Reg_Auth = Reg_Auth  # 登记机关
#         self.Estab_Date = Estab_Date  # 成立日期
#         self.Cop_Type = Cop_Type  # 企业类型
#         self.Business_Ierm = Business_Ierm  # 经营业期限
#         self.admin_Div = admin_Div  # 行政区划
#         self.Annual_Inspect = Annual_Inspect  # 审核/年检日期
#         self.Reg_Addr = Reg_Addr  # 注册地址
#         self.Business_Scope = Business_Scope  # 经营范围
#         # self.province = province  # 所在省份
#         # self.city = city  # 所在城市


class EntItem:
    def __init__(self, data):
        (
            self.Name,
            self.Reg_Capital,
            self.Paid_Capital,
            self.Legal_Rep,
            self.Manage_State,
            self.Old_Name,
            self.Industry,
            self.Credit_Code,  # 统一社会信用代码
            self.Tax_Id_No,
            self.Com_Reg_No,
            self.Org_Code,
            self.Reg_Auth,
            self.Estab_Date,
            self.Cop_Type,
            self.Business_Ierm,
            self.admin_Div,
            self.Annual_Inspect,
            self.Reg_Addr,
            self.Business_Scope) = data


if __name__ == "__main__":
    pass
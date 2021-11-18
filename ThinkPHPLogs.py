import datetime
import requests
import argparse

description = "Please use a valid parameter"
parser = argparse.ArgumentParser(description=description)
parser.add_argument('-u', type=str, help="需要检测的日志文件的目标网址", dest="URL", default="")
args = parser.parse_args()
target = args.URL

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61'
}


def is_leap_year():
    year = datetime.datetime.now().year
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return "y"
            else:
                return "n"
        else:
            return "y"
    else:
        return "n"


def get_url_1():
    part = ["Admin", "Common", "Home", "Install"]
    year = str(datetime.datetime.now().year)[2:4]
    urls = []
    mon_max = datetime.datetime.now().month + 1
    day_max = datetime.datetime.now().day + 1
    for i in part:
        for mon in range(1, mon_max):
            if mon < 10:
                if mon in (1, 3, 5, 7, 8):
                    if mon != mon_max - 1:
                        for day in range(1, 32):
                            if day < 10:
                                url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_0" + str(day) + ".log"
                                urls.append(url)
                            else:
                                url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_" + str(day) + ".log"
                                urls.append(url)
                    elif mon == mon_max - 1:
                        for day in range(1, day_max):
                            if day < 10:
                                url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_0" + str(day) + ".log"
                                urls.append(url)
                            else:
                                url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_" + str(day) + ".log"
                                urls.append(url)
                elif mon in (4, 6, 9):
                    if mon != mon_max - 1:
                        for day in range(1, 31):
                            if day < 10:
                                url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_0" + str(day) + ".log"
                                urls.append(url)
                            else:
                                url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_" + str(day) + ".log"
                                urls.append(url)
                    elif mon == mon_max - 1:
                        for day in range(1, day_max):
                            if day < 10:
                                url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_0" + str(day) + ".log"
                                urls.append(url)
                            else:
                                url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_" + str(day) + ".log"
                                urls.append(url)
                else:
                    if is_leap_year() == "y":
                        if mon != mon_max - 1:
                            for day in range(1, 30):
                                if day < 10:
                                    url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_0" + str(day) + ".log"
                                    urls.append(url)
                                else:
                                    url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_" + str(day) + ".log"
                                    urls.append(url)
                        elif mon == mon_max - 1:
                            for day in range(1, day_max):
                                if day < 10:
                                    url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_0" + str(day) + ".log"
                                    urls.append(url)
                                else:
                                    url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_" + str(day) + ".log"
                                    urls.append(url)
                    elif is_leap_year() == "n":
                        if mon != mon_max - 1:
                            for day in range(1, 29):
                                if day < 10:
                                    url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_0" + str(day) + ".log"
                                    urls.append(url)
                                else:
                                    url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_" + str(day) + ".log"
                                    urls.append(url)
                        elif mon == mon_max - 1:
                            for day in range(1, day_max):
                                if day < 10:
                                    url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_0" + str(day) + ".log"
                                    urls.append(url)
                                else:
                                    url = "/Runtime/Logs/" + i + "/" + year + "_0" + str(mon) + "_" + str(day) + ".log"
                                    urls.append(url)
            else:
                if mon in (10, 12):
                    if mon != mon_max - 1:
                        for day in range(1, 32):
                            if day < 10:
                                url = "/Runtime/Logs/" + i + "/" + year + "_" + str(mon) + "_0" + str(day) + ".log"
                                urls.append(url)
                            else:
                                url = "/Runtime/Logs/" + i + "/" + year + "_" + str(mon) + "_" + str(day) + ".log"
                                urls.append(url)
                    elif mon == mon_max - 1:
                        for day in range(1, day_max):
                            if day < 10:
                                url = "/Runtime/Logs/" + i + "/" + year + "_" + str(mon) + "_0" + str(day) + ".log"
                                urls.append(url)
                            else:
                                url = "/Runtime/Logs/" + i + "/" + year + "_" + str(mon) + "_" + str(day) + ".log"
                                urls.append(url)
                elif mon == 11:
                    if mon != mon_max - 1:
                        for day in range(1, 31):
                            if day < 10:
                                url = "/Runtime/Logs/" + i + "/" + year + "_" + str(mon) + "_0" + str(day) + ".log"
                                urls.append(url)
                            else:
                                url = "/Runtime/Logs/" + i + "/" + year + "_" + str(mon) + "_" + str(day) + ".log"
                                urls.append(url)
                    elif mon == mon_max - 1:
                        for day in range(1, day_max):
                            if day < 10:
                                url = "/Runtime/Logs/" + i + "/" + year + "_" + str(mon) + "_0" + str(day) + ".log"
                                urls.append(url)
                            else:
                                url = "/Runtime/Logs/" + i + "/" + year + "_" + str(mon) + "_" + str(day) + ".log"
                                urls.append(url)
    return urls


def get_url_2():
    year = str(datetime.datetime.now().year)
    urls = []
    mon_max = datetime.datetime.now().month + 1
    day_max = datetime.datetime.now().day + 1
    for mon in range(1, mon_max):
        if mon < 10:
            if mon in (1, 3, 5, 7, 8):
                if mon != mon_max - 1:
                    for day in range(1, 32):
                        if day < 10:
                            url = "/runtime/log/" + year + "0" + str(mon) + "/0" + str(day) + ".log"
                            urls.append(url)
                        else:
                            url = "/runtime/log/" + year + "0" + str(mon) + "/" + str(day) + ".log"
                            urls.append(url)
                elif mon == mon_max - 1:
                    for day in range(1, day_max):
                        if day < 10:
                            url = "/runtime/log/" + year + "0" + str(mon) + "/0" + str(day) + ".log"
                            urls.append(url)
                        else:
                            url = "/runtime/log/" + year + "0" + str(mon) + "/" + str(day) + ".log"
                            urls.append(url)
            elif mon in (4, 6, 9):
                if mon != mon_max - 1:
                    for day in range(1, 31):
                        if day < 10:
                            url = "/runtime/log/" + year + "0" + str(mon) + "/0" + str(day) + ".log"
                            urls.append(url)
                        else:
                            url = "/runtime/log/" + year + "0" + str(mon) + "/" + str(day) + ".log"
                            urls.append(url)
                elif mon == mon_max - 1:
                    for day in range(1, day_max):
                        if day < 10:
                            url = "/runtime/log/" + year + "0" + str(mon) + "/0" + str(day) + ".log"
                            urls.append(url)
                        else:
                            url = "/runtime/log/" + year + "0" + str(mon) + "/" + str(day) + ".log"
                            urls.append(url)
            else:
                if is_leap_year() == "y":
                    if mon != mon_max - 1:
                        for day in range(1, 30):
                            if day < 10:
                                url = "/runtime/log/" + year + "0" + str(mon) + "/0" + str(day) + ".log"
                                urls.append(url)
                            else:
                                url = "/runtime/log/" + year + "0" + str(mon) + "/" + str(day) + ".log"
                                urls.append(url)
                    elif mon == mon_max - 1:
                        for day in range(1, 30):
                            if day < 10:
                                url = "/runtime/log/" + year + "0" + str(mon) + "/0" + str(day) + ".log"
                                urls.append(url)
                            else:
                                url = "/runtime/log/" + year + "0" + str(mon) + "/" + str(day) + ".log"
                                urls.append(url)
                elif is_leap_year() == "n":
                    if mon != mon_max - 1:
                        for day in range(1, 29):
                            if day < 10:
                                url = "/runtime/log/" + year + "0" + str(mon) + "/0" + str(day) + ".log"
                                urls.append(url)
                            else:
                                url = "/runtime/log/" + year + "0" + str(mon) + "/" + str(day) + ".log"
                                urls.append(url)
                    elif mon == mon_max - 1:
                        for day in range(1, day_max):
                            if day < 10:
                                url = "/runtime/log/" + year + "0" + str(mon) + "/0" + str(day) + ".log"
                                urls.append(url)
                            else:
                                url = "/runtime/log/" + year + "0" + str(mon) + "/" + str(day) + ".log"
                                urls.append(url)
        else:
            if mon in (10, 12):
                if mon != mon_max - 1:
                    for day in range(1, 32):
                        if day < 10:
                            url = "/runtime/log/" + year + str(mon) + "/0" + str(day) + ".log"
                            urls.append(url)
                        else:
                            url = "/runtime/log/" + year + str(mon) + "/" + str(day) + ".log"
                            urls.append(url)
                elif mon == mon_max - 1:
                    for day in range(1, day_max):
                        if day < 10:
                            url = "/runtime/log/" + year + str(mon) + "/0" + str(day) + ".log"
                            urls.append(url)
                        else:
                            url = "/runtime/log/" + year + str(mon) + "/" + str(day) + ".log"
                            urls.append(url)
            elif mon == 11:
                if mon != mon_max - 1:
                    for day in range(1, 31):
                        if day < 10:
                            url = "/runtime/log/" + year + str(mon) + "/0" + str(day) + ".log"
                            urls.append(url)
                        else:
                            url = "/runtime/log/" + year + str(mon) + "/" + str(day) + ".log"
                            urls.append(url)
                elif mon == mon_max - 1:
                    for day in range(1, day_max):
                        if day < 10:
                            url = "/runtime/log/" + year + str(mon) + "/0" + str(day) + ".log"
                            urls.append(url)
                        else:
                            url = "/runtime/log/" + year + str(mon) + "/" + str(day) + ".log"
                            urls.append(url)
    return urls


def is_access():
    if target != "" and ("https://" in target or "http://" in target):
        for i in ("/Runtime/Logs", "/runtime/log"):
            url = target + i
            code = requests.get(url=url, headers=header).status_code
            if code in (200, 403):
                if i == "/Runtime/Logs":
                    return "get_url_1_can_test"
                else:
                    return "get_url_2_can_test"
            elif code not in (200, 403):
                print("抱歉，该网站可能不存在日志文件")
                exit()
    elif target == "" or "https://" not in target or "http://" not in target:
        print("貌似你输入的链接不对，必须是一个完整的链接，例如：https://www.baidu.com/")


def run():
    re = 0
    target_urls = []
    if is_access() == "get_url_1_can_test":
        urls = get_url_1()
        print("测试日志类型为: /Runtime/Logs")
        print("当前共有%d条测试记录，请耐心等待测试结果·····" % (len(urls)))
        for i in urls:
            url = target + str(i)
            try:
                code = requests.get(url=url, headers=header).status_code
                if code == 200:
                    print(url)
                    target_urls.append(url)
            except TimeoutError:
                print(url + "连接超时！")
                continue
            except requests.exceptions.ConnectionError:
                print(url + "连接超时！")
                re = re + 1
                if re > 2:
                    print("貌似当前IP已经被封或者服务器已宕机")
                    break
    elif is_access() == "get_url_2_can_test":
        urls = get_url_2()
        print("测试日志类型为: /runtime/logs")
        print("当前共有%d条测试记录，请耐心等待测试结果·····" % (len(urls)))
        for i in urls:
            url = target + str(i)
            try:
                code = requests.get(url=url, headers=header).status_code
                if code == 200:
                    print(url)
                    target_urls.append(url)
            except TimeoutError:
                print(url + "连接超时！")
                continue
            except requests.exceptions.ConnectionError:
                print(url + "连接超时！")
                re = re + 1
                if re > 4:
                    print("貌似当前IP已经被封了或者访问速度过快")
                    break
    print("所有测试已完毕，共有%d条记录" % (len(target_urls)))
    if len(target_urls) != 0:
        choice = input("是否需要将所有结果保存到本地：y/n")
        if choice == "y" or choice == "Y" or choice == "yes" or choice == "YES" or choice == "Yes":
            file = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day) + ".txt"
            with open(file, "w", encoding="UTF-8") as f:
                for i in target_urls:
                    f.write(i)
                    f.write('\n')
            print("结果已保存到：" + file)
        elif choice != "y" or choice != "Y" or choice != "yes" or choice != "YES" or choice != "Yes":
            exit()


if __name__ == '__main__':
    run()
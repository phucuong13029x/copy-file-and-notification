from datetime import datetime
import os
import shutil
import time
import requests
 
def sendteams(chatid:str, messenger:str, mentions:list=[]):
    try:
        url = "http://.../microsoft/chats/send"
        token = ""
        headers = {
            "accept": "application/json",
            "token": token
        }
        data = {
            "chatid": chatid,
            "messenger": messenger,
            "mentions": mentions
        }
        response = requests.post(url=url, headers=headers, json=data)
        print(response.content)
        return response.content
    except Exception as e: print(e)

def waittime(number):
    for i in range(number):
        print(f"[+] Please wait: {int(number) - (i + 1)} second           ", end="\r")
        time.sleep(1)
    print("")

dt = datetime.now().strftime('%Y-%m-%d')
mth = datetime.now().strftime('T%m-%Y')
source_dir = f'C:/auto-report/{dt}'
dir_rick = f'//10.10.10.../Data/YS/Risk/A- BAO CAO IT/148002/{mth}/{dt}'
dir_selt = f'//10.10.35.../HOS-Report/{dt}'
list_file_selt = ['RPT-148002', 'RPT-028002', 'RPT-148040', 'RPT-148044', 'RPT-148046']
list_file_rick = ['RPT-148002']

while True:
    try:
        list_file_root = os.walk(source_dir)
        for root, dirs, files in os.walk(source_dir):
            if not list_file_selt: break
            for file in files:
                if not list_file_selt: break
                for i in list_file_selt:
                    if str(file).find(i) != -1:
                        print(f"[-] Copy: {i} ...")
                        src_file = os.path.join(root, file)
                        if not os.path.exists(dir_selt): os.makedirs(dir_selt)
                        dest_file_selt = os.path.join(dir_selt, file)
                        sz = int(os.stat(src_file).st_size)
                        if sz > 0: # check file size > 0
                            shutil.copy(src_file, dest_file_selt)
                            list_file_selt.remove(i)
                            print(f"[+] Copy: {i} success")
                            sendteams(messenger=f"[+] Copy file {file} success.", chatid='19:........................@thread.v2') # TS Monitor
                        else: print(f"[-] Copy: {i} fail. Size file {sz} byte")
                        break
                if list_file_rick:
                    for i in list_file_rick:
                        if str(file).find(i) != -1:
                            print(f"[-] Copy: {i} ...")
                            src_file = os.path.join(root, file)
                            if not os.path.exists(dir_rick): os.makedirs(dir_rick)
                            dest_file_rick = os.path.join(dir_rick, file)
                            sz = int(os.stat(src_file).st_size)
                            if sz > 0: # check file size > 0
                                shutil.copy(src_file, dest_file_rick)
                                list_file_rick.remove(i)
                                print(f"[+] Copy: {i} success")
                                sendteams(messenger=f"[+] Copy file {file} success.", chatid='19:........................@thread.v2') # Rick
                            else: print(f"[-] Copy: {i} fail. Size file {sz} byte")
                            break
    except Exception as e:print(e)
    if not list_file_selt: break
    waittime(60)

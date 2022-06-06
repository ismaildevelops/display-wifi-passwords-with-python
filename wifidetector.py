

import subprocess
def wifi_detector():
        
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print ("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print ("{:<30}|  {:<}".format(i, ""))


        data = subprocess.check_output(['ipconfig']).decode('utf-8').split('/n')


        for b in data :
            stringer = ''
            if "IPv4 Address" in b:
                b.split(":")[1][1:-1]
                stringer = stringer + b
                
        print(i)
    except:
        print("Thanks Bisharat")
wifi_detector()
##file = open('text.txt','w')
##file.write(b)
##file.close()
##
##

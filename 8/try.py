import requests

s = requests.Session()
login_data = {'username':'aksagg', 'password':'WLyyNdQSjc6QXx1'}
r_login = s.post("https://172.27.20.32:8443/login.php", login_data, verify=False)
s.cookies['logged_in'] = '1'
s.headers.update({'referer': 'example.com'})
s.headers.update({'User-Agent': 'CS628'})
r = s.get("https://172.27.20.32:8443/chal8.php", verify=False) 
print r.headers['x-http-flag']




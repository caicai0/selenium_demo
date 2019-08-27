import requests,bs4
from requests import Response

header = {
    "cookie":"JSESSIONID=390972CBD0F650CF724CFC0DA029FA15-n1; Hm_lpvt_0f56a9ce703c8244905685b4a4ca2cb3=1566901574; Hm_lvt_0f56a9ce703c8244905685b4a4ca2cb3=1566296615,1566437049,1566572476,1566881941; nologinmemtoken=3a542986-1230-4109-95d0-9849673a24b0; UM_distinctid=16bd1ea071e803-043695bc6c5a528-491b3700-13c680-16bd1ea071f535"
}

res: Response = requests.get(url="http://www.cn-healthcare.com/freezing/member/getList_authUserMng.xhtml",headers=header)

print(res.text)
f = open('local.html','w')
f.write(res.text)
f.close()

soup = bs4.BeautifulSoup(res.text, 'html.parser')


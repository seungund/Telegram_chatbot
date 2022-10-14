import requests
from bs4 import BeautifulSoup
import json
import datetime
import re

"""  
ex) 동대부고 https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100000420&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=2&schYmd=20221015
https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=(학교코드)&schulCrseScCode(n)4&schulKndScCode=(nn)&schMmealScCode=(ni)&schYmd=날짜(yyyymmdd) 형태  """


path_e = 'D:\Build\Chatbot_general\Cafeteria\E.json'
path_m = 'D:\Build\Chatbot_general\Cafeteria\M.json'
path_h = 'D:\Build\Chatbot_general\Cafeteria\H.json'

pn = input('학교 급 (고등학교/중학교/초등학교) :')
#pcode = input('학교이름 :')
pcode = '동국대학교사범대학부속고등학교'
dt = str(datetime.date.today())
dt_a = dt.replace('-','')


ni = 2

if pn == '고등학교':
    n = '4'
    ns = '04'
    with open(path_h, 'r', encoding='utf-8') as h:
        data_h = json.load(h)
        for a in data_h['list']:
            if a['SCHUL_NM'] == pcode:
                code = a['SCHUL_CODE']
                
                break
            
        
elif pn == '중학교':
    n = '3'
    ns = '03'  
    with open(path_m, 'r', 'utf-8') as m:
        data_m = json.load(m)
        for a in data_m['list']:
            if a['SCHUL_NM'] == pcode:
                code = a['SCHUL_CODE']
                
                break
         
     
        
elif pn == '초등학교':
    n = '2'
    ns = '02'
    with open(path_e, 'r', 'utf-8') as e:
        data_e = json.load(e)
        for a in data_e['list']:
            if a['SCHUL_NM'] == pcode:
                code = a['SCHUL_CODE']
                
                break
        
else:
    print("잘못 입력하였습니다 처음부터 다시 입력해 주세요") 
  

coder = code.replace("S01", "B10")      
#(임시코드)코드의 앞머리 S01의 변화에 관한 정보가 아직 없으므로 다른학교에서는 작동하지 않을 수 있음           
url = 'https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode={}&schulCrseScCode={}&schulKndScCode={}&schMmealScCode={}&schYmd={}'.format(coder,n,ns,ni,dt_a)

req = requests.get(url)
result = BeautifulSoup(req.text, "html.parser")
elem = result.find_all("tr")
print(elem)




          
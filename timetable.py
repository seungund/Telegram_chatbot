import requests
from bs4 import BeautifulSoup
import json
import datetime
import re

#변수은 이곳에 기록 key = b0a0e01a8df841228238bcbfc7aa7013
#Hurl=고등학교 api url, H_timetable = 고등학교 api get, name = 학교이름 code=학교코드, grade=학년, clss=반, Gcodeurl = 학교기본정보 api url, Gcode = 학교기본정보 api get
#
sch = input('학급을 입력하세요(고등학교/중학교/초등학교):')
name = input('학교이름을 입력하세요:')
grade = input('학년을 입력하세요 (1/2/3/4/5/6):')
clss = input('반을 입력하세요:')
time = input('오늘의 날짜를 입력하세요(YYYYMMDD):')

Gcodeurl = 'https://open.neis.go.kr/hub/schoolInfo?KEY=b0a0e01a8df841228238bcbfc7aa7013&Type=json&pidex=1&pSize=10'+'&SCHUL_NM={}'.format(name)
Gcode = requests.get(Gcodeurl).json()
code = Gcode['schoolInfo'][1]['row'][0]['SD_SCHUL_CODE']
scode = Gcode['schoolInfo'][1]['row'][0]['ATPT_OFCDC_SC_CODE']

#고등학교
if sch == '고등학교':
    Hurl = 'https://open.neis.go.kr/hub/hisTimetable?KEY=b0a0e01a8df841228238bcbfc7aa7013&Type=json&pidex=1&pSize=10'\
    +'&ATPT_OFCDC_SC_CODE={}&SD_SCHUL_CODE={}&ALL_TI_YMD={}&GRADE={}&CLASS_NM={}'.format(scode,code,time,grade,clss)
    H_timetable = requests.get(Hurl).json()
    table = H_timetable['hisTimetable'][1]['row']
    tablestr = str(table)

    if "'PERIO': '6'" in tablestr and "'PERIO': '7'" not in tablestr :
        for i in range(6):
            print(table[i]['ITRT_CNTNT'])
        
    elif "'PERIO': '7'" in tablestr :
        for i in range(7):
            print(table[i]['ITRT_CNTNT'])
    
    else :
        print("ERROR")        
            


#중학교
if sch == '중학교':
    Murl = 'https://open.neis.go.kr/hub/misTimetable?KEY=b0a0e01a8df841228238bcbfc7aa7013&Type=json&pidex=1&pSize=10'\
    +'&ATPT_OFCDC_SC_CODE={}&SD_SCHUL_CODE={}&ALL_TI_YMD={}&GRADE={}&CLASS_NM={}'.format(scode,code,time,grade,clss)
    M_timetable = requests.get(Murl).json()
    table = M_timetable['misTimetable'][1]['row']
    tablestr = str(table)
    
    if "'PERIO': '7'" in tablestr :
        for i in range(7):
            print(table[i]['ITRT_CNTNT'])
    
    elif "'PERIO': '6'" in tablestr and "'PERIO': '7'" not in tablestr :
        for i in range(6):
            print(table[i]['ITRT_CNTNT'])
            
    elif "'PERIO': '6'" not in tablestr and "'PERIO': '7'" not in tablestr and "'PERIO': '5'" in tablestr :
        for i in range(5):
            print(table[i]['ITRT_CNTNT'])
    
    else:
        print("ERROR")        
                
elif sch == '초등학교' :
    Eurl = 'https://open.neis.go.kr/hub/elsTimetable?KEY=b0a0e01a8df841228238bcbfc7aa7013&Type=json&pidex=1&pSize=10'\
    +'&ATPT_OFCDC_SC_CODE={}&SD_SCHUL_CODE={}&ALL_TI_YMD={}&GRADE={}&CLASS_NM={}'.format(scode,code,time,grade,clss)
    E_timetable = requests.get(Eurl).json()
    table = E_timetable['elsTimetable'][1]['row']
    tablestr = str(table)
    
    if "'PERIO': '7'" in tablestr :
        for i in range(7):
            print(table[i]['ITRT_CNTNT'])
    
    elif "'PERIO': '6'" in tablestr and "'PERIO': '7'" not in tablestr :
        for i in range(6):
            print(table[i]['ITRT_CNTNT'])
            
    elif "'PERIO': '6'" not in tablestr and "'PERIO': '7'" not in tablestr and "'PERIO': '5'" in tablestr :
        for i in range(5):
            print(table[i]['ITRT_CNTNT'])
            
    elif "'PERIO': '6'" not in tablestr and "'PERIO': '7'" not in tablestr and "'PERIO': '5'" not in tablestr and "'PERIO': '4'" in tablestr :
        for i in range(4):
            print(table[i]['ITRT_CNTNT'])
                 
    else:
        print("ERROR")
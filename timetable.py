import requests
from bs4 import BeautifulSoup
import json
import datetime
import re

#변수은 이곳에 기록 key = b0a0e01a8df841228238bcbfc7aa7013
#Hurl=고등학교 api url, H_timetable = 고등학교 api get, name = 학교이름 code=학교코드, grade=학년, clss=반, Gcodeurl = 학교기본정보 api url, Gcode = 학교기본정보 api get

name = '동국대학교사범대학부속고등학교'

Gcodeurl = 'https://open.neis.go.kr/hub/schoolInfo?KEY=b0a0e01a8df841228238bcbfc7aa7013&Type=json&pidex=1&pSize=10'+'&SCHUL_NM={}'.format(name)

Gcode = 1

code = 1
grade =1
clss =1


Hurl = 'https://open.neis.go.kr/hub/hisTimetable?KEY=b0a0e01a8df841228238bcbfc7aa7013&Type=json&pidex=1&pSize=10'+'&SD_SCHUL_CODE={}&GRADE={}&CLASS_NM={}'.format(code,grade,clss)
H_timetable = requests.get(Hurl)

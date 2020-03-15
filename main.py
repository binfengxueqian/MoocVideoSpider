import requests
import json
import settings
from couresparser import parseCourse
from download import downliadList
import breakpoint
from settings import downloads
def getCourseInfoByNet(tid:str):
    data = {
        'termId':tid,
        'tid':tid,
        'mob-token': settings.headers['mob-token']
    }
    try:
        response = requests.post(url=settings.url, headers=settings.headers,data=data)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        responseJson = json.loads(response.text,encoding='utf-8')
        parseCourse(responseJson)
        downloads(downliadList)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    breakpoint.go_on()
    getCourseInfoByNet('1206616230')
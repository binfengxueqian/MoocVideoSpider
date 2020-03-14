import requests
import json
import settings
from couresparser import parseCourse
from download import downloads
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
        downloads()
    except Exception as e:
        print(e)
# def getCourseInfoByJson(jsonPath:str):

if __name__ == '__main__':
    getCourseInfoByNet('1206616230')
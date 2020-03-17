import requests
import json
import settings
from couresparser import parseCourse
from download import downloadList
import breakpoint
from download import slecetDownload
from models import selectVideoQuality
def getCourseInfoByNet(tid:str):
    from download import downloads
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
        downloads(downloadList)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    # slecetDownload()
    breakpoint.go_on()
    selectVideoQuality()
    getCourseInfoByNet('1450273447')
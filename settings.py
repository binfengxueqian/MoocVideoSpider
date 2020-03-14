import os
import download.downloads
import download.asyncDownloads

downloads = download.downloads
headers = {'Host': 'www.icourse163.org',
    'edu-app-type': 'android',
    'edu-app-version': '3.19.10',
    'edu-app-channel': 'ucmooc_store_qq',
    'imei': 'U8BBB18C17150469',
    'device-id': '02:00:00:00:00:00_a438dfa7604c06f1',
    'mob-token': '06765c59965b7f918787ed48f9adbb858a7290f69e95970c3e16c2e7aa14c9fc206c03d2781c9e27468fa8c09af84b8e10bd29ebbc4b353f19376349a6b7c9f09e8ea50141de5a4a9c2c4e954d3b4054bcd437a019990be9ca1732e589bfedd43fb9853e1ba8fb0c7b20fa7c589da1c20de67ff1c570b9b561bb1e6b56ca136446f7b51452cbdfb34482a01ad3f30d2d1f534d687f5304567a418d7c783a955bf4f23c65862d1ba6cca9dd737163b86ac3e3713cf7724e61da134382bbf49ef1',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; AGS2-W09 Build/HUAWEIAGS2-W09)'
}
url='https://www.icourse163.org/mob/course/courseLearn/v1'

resourceRoot=os.path.join(os.path.dirname(os.path.abspath(__file__)),'CourseWare')
if not os.path.exists(resourceRoot):
    os.makedirs(resourceRoot)
remainListFile = os.path.join(resourceRoot,'remainList.json')
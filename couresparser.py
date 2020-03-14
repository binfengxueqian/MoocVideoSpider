import os
import json
from bs4 import BeautifulSoup
import models
from settings import resourceRoot
from lib import createDir

courseData = {
    'description':'',
    'outline':'',
    'teacherInfo':[],
    'courseName':'',
    'courseware':[]
}

coursePath = ''

def _parseCourseInfo(responseJson):
    soup = BeautifulSoup(responseJson['results']['termDto']['description'], 'html.parser')
    with open(os.path.join(coursePath,'course.json'),'w',encoding='utf-8')as f:
        json.dump(responseJson,f,ensure_ascii=False,indent=4)
    for i in soup.find_all('p'):
        courseData['description'] += i.text + '\n'
    with open(os.path.join(coursePath,'课程简介.txt'),'w',encoding='utf-8')as f:
        f.write(courseData['description'])
    soup = BeautifulSoup(responseJson['results']['termDto']['outline'], 'html.parser')
    for i in soup.find_all('p'):
        courseData['outline'] += i.text + '\n'
    with open(os.path.join(coursePath,'课程目录.txt'),'w',encoding='utf-8')as f:
        f.write(courseData['outline'])

def _parseCourseware(responseJson):
    chapters = responseJson['results']['termDto']['chapters']
    for chapter in chapters:
        models.Chapter(coursePath,**chapter)

def parseCourse(responseJson):
    global coursePath
    courseData['courseName'] = responseJson['results']['courseDto']['name']
    coursePath = os.path.join(resourceRoot, courseData['courseName'])
    createDir(coursePath)
    _parseCourseInfo(responseJson)
    _parseCourseware(responseJson)

if __name__ == '__main__':
    f = open('2.json', 'r', encoding='utf-8')
    responseJson = json.load(f)
    f.close()
    _parseCourseware(responseJson)
    # print(downliadList.__len__())
    # for i in downliadList:
    #     downloadNew(*i)

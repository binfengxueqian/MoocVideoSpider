import os
from download import downliadList
SHDVideo = True
class Vedio():
    def __init__(self,path,**kwargs):
        self.name = kwargs['name']
        self.path = os.path.join(path, self.name)+'.mp4'
        if SHDVideo:
            if not kwargs['resourceInfo']['videoSHDUrl']=='':
                self.videoUrl = kwargs['resourceInfo']['videoSHDUrl']
            elif not kwargs['resourceInfo']['videoHDUrl']=='':
                self.videoUrl = kwargs['resourceInfo']['videoHDUrl']
            elif not kwargs['resourceInfo']['videoUrl']=='':
                self.videoUrl = kwargs['resourceInfo']['videoUrl']
        else:
            self.videoUrl = kwargs['resourceInfo']['sdMp4Url']
        downliadList.append([self.path, self.videoUrl])
    def __getitem__(self, item):
        return getattr(self,item)

class Doc():
    def __init__(self,path,**kwargs):
        self.name = kwargs['name']
        self.path = os.path.join(path, self.name)+'.pdf'
        self.textUrl = kwargs['resourceInfo']['textUrl']
        downliadList.append([self.path, self.textUrl])
    def __getitem__(self, item):
        return getattr(self,item)

class Lesson():
    def __init__(self,path,**kwargs):
        self.name = kwargs['name']
        self.path = os.path.join(path, self.name)
        self.Units = []
        units = kwargs['units']
        for unit in units:
            if unit['contentType']==1:
                video = Vedio(self.path,**unit)
                self.Units.append(video)
            elif unit['contentType']==3:
                doc = Doc(self.path,**unit)
                self.Units.append(doc)

class Chapter():
    def __init__(self,path,**kwargs):
        self.name = kwargs['name']
        self.path = os.path.join(path,self.name)
        self.Lesson = []
        self.threads = []
        for i in kwargs['lessons']:
            lesson = Lesson(self.path,**i)
            self.Lesson.append(lesson)

def selectVideoQuality():
    global SHDVideo
    a = input('是否下载高清画质，这将花费更长的时间？(y,n)')
    if a == 'n':
        SHDVideo = False
    elif a == 'y':
        SHDVideo = True
    else:
        exit()
    print(SHDVideo)
import os
from download import downliadList

class Vedio():
    def __init__(self,path,**kwargs):
        self.name = kwargs['name']
        self.path = os.path.join(path, self.name)+'.mp4'
        self.videoUrl = kwargs['resourceInfo']['sdMp4Url']
        # if 'videoSHDUrl' in kwargs['resourceInfo']:
        #     self.videoUrl = kwargs['resourceInfo']['videoSHDUrl']
        # elif 'videoHDUrl' in kwargs['resourceInfo']:
        #     self.videoUrl = kwargs['resourceInfo']['videoHDUrl']
        # elif 'videoUrl' in kwargs['resourceInfo']:
        #     self.videoUrl = kwargs['resourceInfo']['videoUrl']
        downliadList.append((self.path, self.videoUrl))
    def __getitem__(self, item):
        return getattr(self,item)

class Doc():
    def __init__(self,path,**kwargs):
        self.name = kwargs['name']
        self.path = os.path.join(path, self.name)+'.pdf'
        self.textUrl = kwargs['resourceInfo']['textUrl']
        downliadList.append((self.path, self.textUrl))
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
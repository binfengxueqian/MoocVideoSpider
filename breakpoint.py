from settings import remainListFile
import json
def go_on():
    from download import downloads
    try:
        f = open(remainListFile,'r',encoding='utf-8')
        loadlist = json.load(f)
        f.close()
        isContinue = False
        if not loadlist==[]:
            while True:
                s = input('您有未完成的下载，是否继续下载？(y,n)')
                if s=='y':
                    isContinue=True
                    break
                elif s=='n':
                    isContinue=False
                    break
                else:
                    continue
        if isContinue:
            downloads(loadlist)
            exit()
        else:
            return
    except Exception as e:
        print(e)
        return
if __name__ == '__main__':
    go_on()
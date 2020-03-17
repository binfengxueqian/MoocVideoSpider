import os,json
import requests
from lib import createDir,getFileSize
from contextlib import closing
from settings import remainListFile
import asyncio
import aiohttp
downloadList = []
remainList = []

def _myPrintProcess(content_size,data_count,name):
    now_jd = (data_count / content_size) * 100
    print("\r文件下载进度：%d%%(%s/%s) - %s" % (now_jd, getFileSize(data_count), getFileSize(content_size), name),end='')

def _downloadold(path,url):
    try:
        with closing(requests.get(url, stream=True)) as response:
            chunk_size = 1024*100  # 单次请求最大值
            content_size = int(response.headers['content-length'])  # 内容体总大小
            data_count = 0
            with open(path, "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    data_count = data_count + len(data)
                    _myPrintProcess(content_size,data_count,os.path.basename(path))
                print("\r 文件下载完成 - %s" % (os.path.basename(path)))
            remainList.remove([path,url])
            with open(remainListFile,'w',encoding='utf-8')as f:
                json.dump(remainList,f,ensure_ascii=False,indent=4)
    except:
        print('\r文件下载失败---------------', os.path.basename(path))

def _download(path,url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.3.2.1000 Chrome/30.0.1599.101 Safari/537.36"
        }
        print('正在下载%s' % os.path.basename(path),end='')
        data_count = 0
        if os.path.exists(path):
            headers['Range'] = 'bytes=%d-' % (os.path.getsize(path))
            data_count = os.path.getsize(path)
        with closing(requests.get(url, stream=True, headers=headers)) as response:
            chunk_size = 1024 * 100  # 单次请求最大值
            content_size = int(response.headers['content-length'])+data_count  # 内容体总大小
            with open(path, "ab") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    data_count += len(data)
                    _myPrintProcess(content_size, data_count, os.path.basename(path))
            print("\r 文件下载完成 - %s" % (os.path.basename(path)))
        remainList.remove([path,url])
        with open(remainListFile,'w',encoding='utf-8')as f:
            json.dump(remainList,f,ensure_ascii=False,indent=4)
    except Exception as e:
        print(e)
        print('\r文件下载失败---------------', os.path.basename(path))

def normalDownloads(List:list):
    global remainList
    remainList = List.copy()
    for i in List:
        path, url = i[0],i[1]
        dir = os.path.dirname(path)
        createDir(dir)
        _download(path,url)

def asyncDownloads(List:list):
    global remainList
    remainList = List.copy()
    tasks = []
    for i in List:
        path, url = i[0], i[1]
        dir = os.path.dirname(path)
        createDir(dir)
        tasks.append(asyncDownload(path,url))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

async def fetch(session, url, dst, headers=None):
    if headers:
        async with session.get(url, headers=headers) as req:
            with(open(dst, 'ab')) as f:
                while True:
                    chunk = await req.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
    else:
        async with session.get(url) as req:
            return req

async def asyncDownload(path,url):
    '''异步'''
    async with aiohttp.ClientSession() as session:
        req = await fetch(session, url, path)

        file_size = int(req.headers['content-length'])
        if os.path.exists(path):
            first_byte = os.path.getsize(path)
        else:
            first_byte = 0
        if first_byte >= file_size:
            return file_size
        header = {"Range": f"bytes={first_byte}-{file_size}"}
        await fetch(session, url, path, headers=header)
        print("文件下载完成 - %s" % (os.path.basename(path)))
        remainList.remove([path,url])
        print('正在删除%s' % (os.path.basename(path)))
        with open(remainListFile,'w',encoding='utf-8')as f:
            json.dump(remainList,f,ensure_ascii=False,indent=4)

downloads = normalDownloads

def slecetDownload():
    global downloads
    a = input('是否使用异步下载，这将使你无法时时查看下载进度?(y,n)')
    if a == 'n':
        downloads = normalDownloads
    elif a== 'y':
        downloads = asyncDownloads
    else:
        exit()
if __name__ == '__main__':
    url='http://jdvodrvfb210d.vod.126.net/mooc-video/nos/mp4/2015/10/04/2271185_sd.mp4?ak=99ed7479ee303d1b1361b0ee5a4abceeb7d0245376adaec84fdde1ecee9d15fbd3fc04c908c652600d5f74a92c114e9937a6abb08078d4df6df77e77fdda405b2701580aae0d7646b5fbf20d7a8eceebe88c01d51083d19b7f37bb90ce91f584ff95aee726907876d470c935a98ed2969466599be4f424183703589739adf00fcb8ec4c9d97c26298fee68fc20a7d05d4870092f831ac65589dad0d872f68a6436998ed577dd2cb418c206f27a0cb550'
    path = 'encrypt-1850010-1449935342020.mp4'
    _download(path,url)

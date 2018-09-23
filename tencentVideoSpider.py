#/usr/bin/python
#coding:utf-8
import requests
import urllib
from requests.adapters import HTTPAdapter
import time
import os
def convert_file(_path, filename):
    tmp = []
    if '\\' in _path:
      _path=_path.replace('\\','\\\\')
    files = os.listdir(_path)
    for file in files:
      if '.ts' in file:
        tmp.append(_path+"\\"+str(file))
    os.chdir(_path)
    shell_str = '+'.join(tmp)
    shell_strc = 'copy /b '+ shell_str + ' ' + filename+"g.mp4"
    print(shell_strc)
    #os.system(shell_strc)
    #os.system('del /Q *.ts')
    return
def download_txvideo(_url,_path):
#url ='https://ltsdl.qq.com/-mgUm5ptL_fxzLjvXXTfjA58wwsJj3qNpiqJ16ZBtg6NKjlsRAlf6jAzO-11_6ZmKo9CRPtt4qEuFoOGcPdK41LeOAByF-zcRCMP555O7mB_U1UDw2KgwQuqQaNTyXpHmo1wMYNNrW2robWPAx1-M20FGnWSEy3Z/g0027gix4dm.321004.ts.m3u8?ver=4'
     r = requests.get(url=_url)
     with open(_path+'/videoUrl.txt', 'wb') as f:
        f.write(r.content)

     fo = open(_path+"/videoUrl.txt",'r')
     fc = fo.readlines()
     count=0
     for i in fc:
       if 'ver=4' in i:
         urltemp=_url.split('/')
         urldl=_url.replace(urltemp[urltemp.__len__()-1],i).strip()
         print(urltemp[urltemp.__len__()-1])
         s=requests.session()
         s.mount('https://',HTTPAdapter(max_retries=3))
         r=s.get(urldl,timeout=3)
        #urllib.request.urlretrieve('https://www.baidu.com',str(count)+'.ts')
         with open(_path+'/'+str(count)+'.ts', 'wb') as f:
            f.write(r.content)
         count+=1
         time.sleep(1)
     return

if __name__=='__main__':
    _path=input("输入下载路径：\n")
    _url=input("输入下载链接：\n")
    filename=input("输入下载文件名称：\n")
    download_txvideo(_url,_path)
    convert_file(_path,filename)



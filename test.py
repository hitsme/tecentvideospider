import  requests
from requests.adapters import HTTPAdapter
import os
def convert_file(_path, files, filename):
    tmp = []

    for file in files:
        tmp.append(_path+str(file))
    os.chdir(_path)
    shell_str = '+'.join(tmp)
    shell_strc = 'copy /b '+ shell_str + ' ' + filename+"g.mp4"
    print(shell_strc)
    os.system(shell_strc)
    os.system('del /Q *.ts')



filelist=os.listdir('G:\\pycharmWorkspace\\tecentvideospider\\vd')
for item in filelist:
    print(item)
path='G:\\pycharmWorkspace\\tecentvideospider\\vd'
print(path.replace('\\','/'))
newfile=open('G:\\pycharmWorkspace\\tecentvideospider\\vd\\new.mp4','w')
convert_file('G:\\pycharmWorkspace\\tecentvideospider\\vd\\',filelist,'new')

#coding:utf-8
from moviepy.editor import *
import os
L = []

for root, dirs ,files in os.walk("G:\\vd"):

    for i in range(12,files.__len__()-1 ):
        print(i)
        if os.path.splitext(str(i)+'.ts')[1] == '.ts':
            filePath = os.path.join(root, str(i)+'.ts ')
            video = VideoFileClip(filePath)
            L.append(video)

final_clip = concatenate_videoclips(L)

final_clip.to_videofile("./target.mp4", fps=25, remove_temp=False)


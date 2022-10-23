def clip(x):
    result = ""
    for i in range(x):
        if i == x-1:
            result = result + "clip" + str(i+1)
        else: 
            result = result + "clip" + str(i+1) +", entre,  "
    return result


from moviepy.editor import *
import os
import shutil
number_video = len(os.listdir("./video"))
if number_video == 1: 
    clip1 = VideoFileClip("./video/video1.mp4")
    timecode = int(clip1.duration)
    cutcode = int(timecode/2)
    clip1 = clip1.subclip(0, cutcode)
    clip1.write_videofile("./result/result1.mp4")
    clip1 = clip1.subclip(cutcode, timecode)
    clip1.write_videofile("./result/result2.mp4")

f = open("./temp.py", "w+")
f.write("""from moviepy.editor import *
import os
import shutil
from os import remove
from sys import argv
""")
for i in range(number_video):
    f.write("clip" + str(i+1) + """ = VideoFileClip("./video/video""" + str(i+1) + """.mp4")
""")
f.write("""entre = VideoFileClip("./entre/entre.mp4")
""")
f.write("result = concatenate_videoclips([" + clip(number_video) + """], method="compose")""")
f.write("""
result.write_videofile("./result/result.mp4", fps = 30)
remove(argv[0])""")
f.close()
os.system("python3 temp.py 1")
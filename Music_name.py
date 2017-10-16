import os
import os.path
import sys

rootdir = sys.path[0]
print("脚本所在位置:" + rootdir)


dirName = input("输入需要进行资源包整理的文件夹名字：")
firstDir = input("输入音乐包起始ID:")

def walkMusicFile(dirname,firstid):
    startID = int(firstid)
    for parent, dirnames, filenames in os.walk(os.path.join(rootdir, dirName)):
        for dir in dirnames:
            array = renameMusic(os.path.join(parent,dir),startID)
            startID = array[-1] + 1
            os.rename(os.path.join(parent, dir), os.path.join(parent, str(startID - len(array) - 1)))


def renameMusic(musicname,musicid)->list:
    print("正在处理专辑：" + musicname + "起始ID:" + str(musicid))
    idarray = []
    for parent,dirnames,filenames in os.walk(os.path.join(rootdir,musicname)):
        for dir in dirnames:
            musicid += 1
            idarray.append(musicid)
            oldname = os.path.join(parent,dir)
            newname = os.path.join(parent,str(musicid))
            os.rename(oldname,newname)
    print("专辑处理完毕，返回ID" + str(musicid))
    return idarray



walkMusicFile(dirName,firstDir)



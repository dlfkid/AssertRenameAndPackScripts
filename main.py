import os
import os.path
import shutil
import sys


rootdir = sys.path[0]
print("脚本所在位置:" + rootdir)
path = input("输入需要进行资源包整理的文件夹名字：")

def walkTheFile(path):
    for parent,dirnames,filenames in os.walk(os.path.join(rootdir,path)):
      for filename in filenames:
          if filename != ".DS_Store":
              print("正在处理" + filename)
              nameArr = os.path.splitext(filename)
              prename = nameArr[0]
              extendname = nameArr[1]
              dirPath = os.path.join(parent, prename)
              if os._exists(dirPath) != True:
                print(prename + "目录不存在，将创建目录")
                os.mkdir(dirPath)
              txtFile = dirPath + "/" + prename + ".txt"
              print("生成文件标识" + prename + ".txt")
              txt = open(txtFile,'a')
              txt.close()
              newName = "a"+extendname
              os.rename(os.path.join(parent,filename),os.path.join(parent,newName))
              sourcePath = parent + "/" + newName
              destPath = dirPath + "/" + newName
              shutil.move(sourcePath,destPath)
              print("资源处理完毕")

walkTheFile(path)


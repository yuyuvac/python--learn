from os import name


def fileinfo(file_name):
    file1=None
    try:
       file1=open(file_name, "r", encoding="UTF-8")
       print(f"这是文件:{file1.read()}")
    except  Exception as e:
        print(f"文件未找到:{e}")
    finally:
        if file1 != None:
            file1.close()
if __name__ == "__main__":
        fileinfo("D:/OneDrive/Desktop/kill.txt")
def appendfile(file_name,data):
    file2=open(file_name,"a",encoding="UTF-8")
    file2.write(data)
if __name__ == "__main__":
    appendfile("D:/OneDrive/Desktop/cill.txt","\n早上好我爱你")

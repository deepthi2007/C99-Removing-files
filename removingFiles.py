import os
import shutil
import time

def getFileAge (path) :
    ctime = os.stat(path).st.ctime()
    return ctime

def removeFile (path):
    if not os.remove(path) :
        print(path," is successfully removed")
    else :
        print("Error deleting the "+path)

def removeFolder (path) :
    if not shutil.rmtree(path) :
        print(path," is successfully removed")
    else :
        print("Error deleting the "+path)

def main () :

    deleted_files=0
    deleted_folders=0
    path = "/PATH TO DELETE"
    days = 30

    seconds = time.time() - (days*24*60*60)

    if os.path.exists(path) :
        for roots,dirs,files in os.walk(path) :
            if seconds >= getFileAge(roots) :
                removeFolder(roots)
                deleted_folders+=1
                break
            else :
                for folder in dirs :
                    folder_path = os.path.join(roots,folder)
                    if seconds >= getFileAge(folder_path):
                        removeFolder(folder_path)
                        deleted_folders+=1

                for file in files :
                    file_path = os.path.join(roots,file)
                    if seconds >= getFileAge(file_path) :
                        removeFile(file_path)
                        deleted_files+=1

        else :
            file_path = os.path.join(roots,file)
            if seconds >= getFileAge(file_path) :
                removeFile(file_path)
                deleted_files+=1

    else :
        print(path," is not found")
        print("no.of folder deleted : ",deleted_files)
        print("no.of files deleted",deleted_files)


if __name__ == "__main__" :
    main()
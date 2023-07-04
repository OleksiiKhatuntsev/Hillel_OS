import os
import test_folder.test2

# print(os.getcwd())  # where we are
# os.chdir('test_folder')  # change directory  "cd"
# print(os.getcwd())
# os.chdir('..')  # cd ..
# print(os.getcwd())

#
# print(os.cpu_count())  # CPU
# print(os.getlogin())  # Current user

# print(os.listdir())  # get all files and folders in current folder    - colsole analog "ls"
# print(type(os.listdir()))

# for item in os.scandir():
#     print(item.name)
#     print(item.path)
#     print(item.is_file())
#     print("***********************************")

# os.mkdir("test_folder_via_command")  # mkdir - console
# os.rmdir("test_folder_via_command")
# os.makedirs("a/b/c")  # cascade create

# import shutil
# shutil.rmtree("a")  # cascade remove


# os.system("type os_example.py")  # linux - cat file_name.py


for dirpath, dirnames, filenames in os.walk('.'):
    print(dirpath)
    print(dirnames)
    print(filenames)
    print("****************************************************")
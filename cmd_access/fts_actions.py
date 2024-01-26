import requests
import sys

def disp():
    url = "https://ramvilas.pythonanywhere.com/display_files_cmd"
    response =requests.get(url)
    files = (response.text.split())
    if len(files)==0:
        print("NO FILES")
    else:
        for i in files:
            print(i)

def up(filename):
    import os
    url = "https://ramvilas.pythonanywhere.com/upload_file"
    if not os.path.isfile(filename):
        print("FILE NOT FOUND")
        exit()
    else:
        with open(filename, 'rb') as file:
            files = {'files':(os.path.basename(filename), file)}
            response = requests.post(url, files=files)
    if response.status_code == 200:
        print("DONE")
    else:
        print("FAILED")

def down(filename):
    url = "https://ramvilas.pythonanywhere.com/download/" + filename
    response = requests.get(url)
    if response.status_code==200:
        new_file_path =input("Enter the file path you want to save the file to:")
        file_path = new_file_path + "\\" + filename
        with open(file_path, 'wb')as file:
            file.write(response.content)
    else:
        print("DOWLOAD FAILED")


def rem(filename):
    url = "https://ramvilas.pythonanywhere.com/delete/"+filename
    response =requests.get(url)
    if response==200:
        print("FILE DELETED")
    else:
        print("DELETION FAILED")
        print(response)

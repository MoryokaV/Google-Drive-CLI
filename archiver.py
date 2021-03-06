#!/opt/homebrew/bin/python3

import os

def compressFolder(foldername, folderpath, script_path):
    print("\n")    
    print("#################### Compressing files! Please wait!... ####################\n")
     
    try:
        os.system("7z a " + "\"" + script_path + "\\" + renameFile(foldername) + "\"" + " " + "\"" + folderpath + "\"")

        print("\n")
        print("############################################################################\n")
    except:
        print("\n")
        print("An error occured while compressing...")
        print("Make sure you have '7zip' installed!")
        print("Run 'precache' for auto-install")

def renameFile(foldername):
    if '.' in foldername:
        foldername = foldername[0: foldername.find("."):]
        foldername += ".zip"        
        return foldername
    else:
        foldername += ".zip"
        return foldername

def deleteCompressedFolder(filename, script_path):
    filename = renameFile(filename)
    
    if os.path.exists(script_path + "\\" + filename):
        os.remove(script_path + "\\" + filename)       
    else:
        print("File doesn't exists anymore!")

def extractFile(filename,script_path):
    print("\n")
    print("#################### Extracting files! Please wait.... #####################\n")
    
    try:
        os.system("7z x " + "\"" + script_path + "\\" + filename + "\"")

        print("\n")
        print("##############################################################################\n")
    except:
        print("\n")
        print("An error occured while extracting...")
        print("Make sure you have '7zip' installed!")
        print("Run 'precache' for auto-install")
    

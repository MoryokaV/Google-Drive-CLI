#!/usr/bin/env python3

# - - Code by Vlaviano - - #

from __future__ import print_function
import pickle
import os.path
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import extractor
import uploader
import archiver
import precache
import downloader

SCOPES = ['https://www.googleapis.com/auth/drive']
global service
script_path = str(os.environ.get('DRIVE_HOME'))

def initialize_api():
    creds = None

    #if the user is already logged in load the credentials
    if os.path.exists(script_path + "/" + 'token.pickle'):
        with open(script_path + "/" + 'token.pickle', 'rb') as token:
           creds = pickle.load(token)

    #if there's no credentials let the user login to the Google Drive Account
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                    script_path + "/" + 'credentials.json', SCOPES)
            creds = flow.run_local_server(port = 8888)
        #Save the Credentials for the next run
        with open(script_path + "/" + 'token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    global service
    service = build('drive', 'v3', credentials = creds)
    print("### Goole Drive V3 API ###")
    print("\n")

def helpDialog():
    print("") 
    print("################# Google Drive Sync Terminal ################# - Code by Vlaviano")
    print("download(d) + file name | -> downloading file/folder from GDrive")
    print("upload(u) + file name | -> uploading file/folder to GDrive")
    print("root | -> showing the root folders and files from GDrive")
    print("files | -> showing all files ")
    print("precache | -> installing required programs for running API")
    print("search + file name | -> check for specified file availability in your Drive")
    print("delete + file name | -> delete a file from your drive root")
    sys.exit()

def selector():
    try:
        select = sys.argv[1]
    except:
        print("Invalid command! - type 'help' for more details")
        sys.exit()
    if select == "download" or select == "d":
        filename = sys.argv[2]
        if filename != "":
            downloader.downloadFile(filename, service, script_path)
            archiver.extractFile(filename, script_path)
            archiver.deleteCompressedFolder(filename, script_path)
        else:
            print("Inseart a valid file name!")
    elif select == "upload" or select == "u":
        foldername = sys.argv[2]
        if os.path.exists(os.path.abspath(foldername)):
            archiver.compressFolder(foldername,os.path.abspath(foldername), script_path)
            uploader.uploadFile(foldername, script_path + "\\" + archiver.renameFile(foldername), service)
            archiver.deleteCompressedFolder(foldername, script_path)
        else:
            print("File not found!")
            sys.exit()
    elif select == "root":
        extractor.root(service, True) 
    elif select == "help" or select == "h":
        helpDialog()
    elif select == "files":
        extractor.file_list(service)
    elif select == "search":
        filename = sys.argv[2]
        if filename != "":
            extractor.searchFile(filename,service)
        else:
            print("Insert a valid file name!")
            sys.exit()
    elif select == "precache":
        precache.install7z()
        sys.exit()
    elif select == "delete":
        filename = sys.argv[2]
        if filename != "":
            extractor.delete(filename, service)
        else:
            print("Insert a vaild file name!")
            sys.exit()
    else:
        print("Unknown command! - Type 'help' for more details")
        sys.exit()

if __name__ == '__main__':
    #Call the GOOGLE DRIVE API v3
    initialize_api()    
    selector() 


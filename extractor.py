#!/opt/homebrew/bin/python3

# - - Code by Vlaviano - - #

page_token = None

from apiclient import errors
import sys


def file_list(service):

    results = service.files().list(q = "'me' in owners and trashed = false", 
            spaces = 'drive',
            fields = 'nextPageToken, files(id, name)',
            pageToken = page_token).execute()    
        
    files = results.get('files', [])
    
    if not files: 
        print("Your drive is empty")
    else:
        for f in files:
            print(u"{0} ({1})".format(f['name'], f['id']))

def root(service, printall):
        
    results = service.files().list(q = "'root' in parents and trashed = false", 
            spaces = 'drive',
            fields = 'nextPageToken, files(id, name, modifiedByMeTime)',
            pageToken = page_token).execute()    
        
    files = results.get('files', [])
    
    if printall:
        if not files: 
            print("Your drive is empty")
        else:
            for f in files:
                print(u"{0} ({1})".format(f['name'], f['id']))
    return files

def searchFile(filename,service):
    files = root(service, False)
    
    if files:
        for f in files:
            if f['name'] == filename:
                size = f.get('size', ' - Unknown - ')
                print(u"{0} | File size: {1} | Last time modified: {2} | (id: {3}) ".format(f['name'], size, f['modifiedByMeTime'], f['id']))
                return f['id']
        print("File not found! -- type 'root' for more details")
        return "null"
    else:
        print("Your drive is empty!")

def delete(filename, service):    
    select = input("Are you sure you want to delete " + filename + " (Y/N): ")
    
    if select == "y" or select == "Y":    
        
        print("\nRemoving file...\n") 

        f_id = searchFile(filename, service)

        if f_id != "null": 
            # delete file without moving to trash 
            try:
                service.files().delete(fileId = f_id).execute()
                print("### File was deleted succesfully! ###\n")
            except errors.HttpError as error:
                print("Error on deleting file: " + error)
        else:
            # a message is already printed by search function so i will close it 
            sys.exit()
    elif select == "n" or select == "N":
        sys.exit()
    else:
        print("Unknown command!")
        sys.exit()
 

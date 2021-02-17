#!/usr/bin/env python3

# - - Code by Vlaviano - - #

import extractor
import io
from googleapiclient.http import MediaIoBaseDownload
import shutil
import extractor

def downloadFile(filename, service, download_path):
    f_id = extractor.searchFile(filename, service)
    
    if f_id != "null":
        
        request = service.files().get_media(fileId = f_id)
        fh = io.BytesIO() #downloading file to RAM memory
        downloader = MediaIoBaseDownload(fh, request, chunksize = 1024 * 2048)
        complete = False
        
        
        needDelete = input("Do you want to delete file from cloud after download complete? (Y / N): ")        

        print("")
        print("Starting download...")
        print("")

        while complete is False:
            status, complete = downloader.next_chunk()
            print("Download status: " + str("%.2f" % round(status.progress() * 100, 2)) + "%", end = "\r")
       
        #Converting from memory to disk
        print("Converting...\n")
        fh.seek(0)
        with open(download_path + "\\" + filename,'wb') as f:
            shutil.copyfileobj(fh, f, length = fh.getbuffer().nbytes)
        if downloader:
            print("\nFile was downloaded succesfully! \n")

        #Delete file if needed from cloud to optimize time
        if needDelete == "Y" or needDelete == "y":
            print("Deleting file from cloud...")
            extractor.delete(filename, service)

    else: 
        print("There's no file/folder " + filename + " on your Drive")

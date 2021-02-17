#!/opt/homebrew/bin/python3

# - - Code by Vlaviano - - #

from apiclient.http import MediaFileUpload
import archiver

def uploadFile(filename, filepath, service):
    print("")
    print("Uploading...")
    print("")

    file_metadata = {'name': archiver.renameFile(filename)}

    media = MediaFileUpload(filepath, resumable = True, mimetype='archive/zip',chunksize = 1024 * 2048)
    f = service.files().create(body=file_metadata, media_body=media)
    
    response = None
    while response == None:
        status, response = f.next_chunk()
        if status:
            print ("Google Drive API v3 Upload status %s%%." % str("%.2f" % round(status.progress() * 100, 2)),end = "\r")
    if f:
        print("\n### " + filename + " uploaded succesfully! ###\n")

    print("Drive upload done!")

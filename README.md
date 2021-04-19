# Google-Drive-CLI

Command line program for making your terminal even more functional!

The project is cross-platform (Windows, MacOS, Linux)!

# To use this script you need a few steps of settings:

Windows: - Go to "Edit Environment Variables for your account"  
         - Add a new variable called "DRIVE_HOME" and add the script directory there  
         - Enter in Path variable  
         - Add the directory there.  
         - Now go to Command Prompt and call it "sync.py" + the words mentioned below  
         (For the first run the browser will prompt to give API access to your account)  
         
         
Linux / MacOS: - Add in your .zshrc / .bashrc a varable called "DRIVE_HOME" and add the script's directory  
               - Add along the PATH variable the directory of the script.  
               - Now go open the Terminal and call it "sync.py" + the words mentioned below  
               (For the first run the browser will prompt to give API access to your account)  
         

  download(d) + file name | -> downloading file/folder from GDrive  
  upload(u) + file name | -> uploading file/folder to GDrive  
  root | -> showing the root folders and files from GDrive  
  files | -> showing all files  
  precache | -> installing required programs for running API  
  search + file name | -> check for specified file availability in your Drive  
  delete + file name | -> delete a file from your drive root  

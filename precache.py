#!/opt/homebrew/bin/python3

import os
import subprocess
import sys

def os_gathering():
    import platform    
    return platform.system()


def install7z():
    if os_gathering() == "Windows":
        print("Please run the installer: ....")
        os.startfile("dependencies")
    else:
        os.system("sudo snap install p7zip-desktop")

    print("\nPrecache done succesfully!\n")


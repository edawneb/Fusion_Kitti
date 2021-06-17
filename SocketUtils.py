#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:14:36 2021

@author: ben
"""

import socket

class socketConfigs:
    def __init__(self):
        infile = open("SocketConfigs.txt", "r")
        self.MyPort, self.MyIP, self.YourPort, self.YourIP, self.role= infile.readlines()
        self.MyPort = self.cleanString(self.MyPort, "MyPort")
        self.MyIP = self.cleanString(self.MyIP, "MyIP")
        self.YourPort = self.cleanString(self.YourPort, "YourPort")
        self.YourIP = self.cleanString(self.YourIP, "YourIP")
        self.role = self.cleanString(self.role, "Role")
        self.MAX_SIZE = self.cleanString(self.MAX_SIZE, "Max Size") #Max size in bytes
        self.RECV_SIZE = self.cleanString(self.RECV_SIZE, "Recv Size")
        infile.close()
        
        if(self.role=="client"):
            self.start_client()
        elif(self.role=="server"):
            self.start_server()
        else:
            print("Incorrect role, check config file")
            
    
    def start_client(self, packet):
        self.prepPacket(packet)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysocket:
            mysocket.connect((self.YourIP, self.YourPort))
            mysocket.sendall((packet))
            
            data = mysocket.recv(self.RECV_SIZE)
        
        #CHANGE THIS TO DO A THING WITH THE RECIEVED PACKAGE
        print(data) 
            
    
    def start_server(self):
        with socket.socket(socket.AF.INET, socket.SOCK_STREAM) as mysocket:
            mysocket.bind((self.MyIP, self.MyPort))
            mysocket.listen()
            conn, address = mysocket.accept()
            with conn:
                print("Connected by", address)
                while True:
                    data = conn.recv(self.MAX_SIZE)
                    if not data:
                        break
                    
                    #CHANGE HERE TO SEND TO MODEL
                    conn.sendall(data)

    def prepPacket(self, packet):
        #DO SOMETHING SMART HERE
        
        return
        
    def cleanString(self, InputString, StringID):
        StringID = StringID + " "
        InputString.strip(StringID)
        return InputString

    def GetMyPort(self):
        return(self.MyPort)
    
    def GetMyIP(self):
        return(self.MyIP)
    
    def GetYourPort(self):
        return(self.YourPort)
    
    def GetYourIP(self):
        return(self.YourIP)
        
    def GetRole(self):
        return(self.role)
        
    

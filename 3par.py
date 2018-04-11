#!/usr/bin/python

import json
import requests
import datetime
import sys

#---arguments---
IP = '10.61.43.108'
user = 'restapi'
passwd = '123456'
port = '8008'
#---------------

class _3PAR:
        arg_conn= {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"
        }
        PostURL = ''
        GetURLsystem = ''
        GetURLcapacity = ''
        auth_json = ''

        def __init__(self, IP, user, passwd, port):
                self.PostURL = "http://"+IP+":"+port+"/api/v1/credentials"
                self.GetURLsystem = "http://"+IP+":"+port+"/api/v1/system"
                self.GetURLcapacity = "http://"+IP+":"+port+"/api/v1/capacity"
                self.auth_json = "{\"user"+"\":\""+user+"\",\"password\":\""+passwd+"\"}"

        def get_key (self):     # connect to get key
                try:
                        r = requests.post(self.PostURL, data=self.auth_json, headers=self.arg_conn,verify=False)
                        key = json.loads(r.text)["key"]
                        r.connection.close()
                        self.arg_conn["X-HP3PAR-WSAPI-SessionKey"] = json.loads(r.text)["key"]
                except:
                        Exceptions(self.PostURL)

        def get_data_URL (self,url):    # connekt to url
                try:
                        r = requests.get(url, data=None, headers=self.arg_conn,verify=False)
                        r.connection.close() #print(r.status_code, r.reason)
                        return (r.text)
                except:
                        Exceptions(url)
                        return None

def Exceptions(URL):
        print ("Problem with connection: "+URL+". Work can't be continued ...")
        sys.exit()

class Separation_capacity:
        Menory = {}
        t_dict = {}
        def post_dict(self):
                pass
        def get_dict(self):
                pass

def Separ_capacity_info(capacity_info,label):
        capacity_obj = Separation_capacity()
        capacity_obj.t_dict = json.loads(capacity_info)[label]
        capacity_obj.Menory[label+'_totalMiB']=capacity_obj.t_dict.get('totalMiB')
        capacity_obj.Menory[label+'_freeMiB']=capacity_obj.t_dict.get('freeMiB')
        capacity_obj.Menory[label+'_failedCapacityMiB']=capacity_obj.t_dict.get('failedCapacityMiB')
        capacity_obj.t_dict = capacity_obj.t_dict["allocated"]
        capacity_obj.Menory[label+'_totalAllocatedMiB']=capacity_obj.t_dict.get('totalAllocatedMiB')
        list = capacity_obj.Menory
        #capacity_obj.Menory.clear()
        return capacity_obj.Menory
        #print (capacity_obj.t_dict)

def Separ_system_info():
        pass

def main ():
        dict_3par={}
        mas_capacity_info = ['NLCapacity','SSDCapacity','allCapacity','FCCapacity']

        _3par = _3PAR(IP, user, passwd, port)
        _3par.get_key()
        system_info = _3par.get_data_URL(_3par.GetURLsystem)
        capacity_info = _3par.get_data_URL(_3par.GetURLcapacity)

        for label_cap in mas_capacity_info:
                dict_3par = Separ_capacity_info(capacity_info,label_cap)
        print (dict_3par)
                #dict_3par = json.loads(d)
        #print ( json.loads(dict_3par))

if __name__ == '__main__':
    main()

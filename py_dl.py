#! /etc/python3

import os
import subprocess as sp
import requests
from bs4 import BeautifulSoup
import urllib
import re
import http.client
from urllib.parse import urlparse


def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True



#def one_dl(pre_url , every_link):
#    print ("downloading:\n",pre_url+every_link)
#    try:
#        wg_comand  = "wget -c "+pre_url+every_link
#        os.system(wg_comand)
#    except:
#       print("error downloading file")



def add_single(inp_url = None):
    if(inp_url == None): inp_url = input("pls enter a url\n")
    try:
        list = open('list.txt','a')
        list.write(inp_url+ "\n")
        print("url added to list")
    except: print("error in appending to list    ")



def add_batch():
    inp_url = input("pls enter a url\n")
    print("parsing html...")
    try :
        test = urllib.request.urlopen(inp_url).read()
        page = requests.get(inp_url)
        bs = BeautifulSoup(page.content, features='lxml')
    except :
        print("error parsing html")
        return

    keyword = input("pls enter keyword to search: (a for nothing) ")
    if keyword == "a" or keyword == "" : keyword = "";

    OPT = input("page have full link or no? (f or n)")
    pre_url = inp_url
    if OPT in 'fy ' : pre_url = "";


    for link in bs.findAll('a'):
        every_link = link.get('href')
        if keyword in every_link:
            add_single(pre_url+every_link);


def start_wget():
    print("starting wget . .. ")
    wg_comand  = "wget -c -i list.txt"
    os.system(wg_comand)

def print_list():
    print()
    os.system("cat list.txt");

def edit_list():
    os.system("nano list.txt");

# - - -- main program - - - -

while (1==1):

    command = input("\nwhat do you want to do?\nadd html Batch = b \nSingle file = s  \nContinue Download = d\nPrint queue = p\nEdit queue = e\n")
    command = command.lower()

    if command in ["continue" ,"download" , "d" , "c" ] : start_wget();

    elif command in ["single", "s"] : add_single()

    elif command in ["batch" , "b"] : add_batch()

    elif command in ["print" , "p"] : print_list()

    elif command in ["edit" , "e"] : edit_list()

    else : exit()

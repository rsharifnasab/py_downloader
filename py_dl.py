#!/usr/bin/python3

import os
import subprocess as sp
#import requests
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


# def one_dl(pre_url , every_link):
#    print ("downloading:\n",pre_url+every_link)
#    try:
#        wg_comand  = "wget -c "+pre_url+every_link
#        os.system(wg_comand)
#    except:
#       print("error downloading file")


def add_single(inp_url=None):
    if(inp_url == None):
        inp_url = input("pls enter a url\n")
    try:
        list = open('list.txt', 'a')
        list.write(inp_url + "\n")
        print(inp_url, " added to list")
    except:
        print("error in appending to list    ")


def add_multi_single():
    print("now enter links, separated by enter")
    while(1 == 1):
        inp_url = input("pls enter a url,done = d\n")
        if inp_url.lower() in ["done", "d", "end", "e", "exit"]:
            break
        add_single(inp_url)


def auto_add():
    regex = r"[Ss]\d{1,2}[Ee](\d{1,2})"
    main_url = input("pls enter first episode link here:\n")
    m = re.search(regex, main_url)
    if m == None:
        print("no serial found")
    else:
        all = m.group()
        first_ep = int(all[4:6])
        n = int(input("last episode?: "))
        for i in range(n+1 - first_ep):
            final = main_url
            episode = str(first_ep + i)
            if int(episode) < 10:
                episode = "0" + episode
            episode = all[0:4] + episode
            final = re.sub(regex, episode, final)
            add_single(final)


def add_batch():
    inp_url = input("pls enter a url\n")
    print("parsing html...")
    try:
        test = urllib.request.urlopen(inp_url).read()
        page = requests.get(inp_url)
        bs = BeautifulSoup(page.content, features='lxml')
    except:
        print("error parsing html")
        return

    keyword = input("pls enter keyword to search: (a for nothing) ")
    if keyword == "a" or keyword == "":
        keyword = ""

    OPT = input("page have full link or no? (f or n)")
    pre_url = inp_url
    if OPT in 'fy ':
        pre_url = ""

    for link in bs.findAll('a'):
        every_link = link.get('href')
        if keyword in every_link:
            add_single(pre_url+every_link)


def start_wget():
    print("starting wget . .. \n downloading to :")
    os.system("pwd")
    # -O ~/Downloads/dl_py/
    aria_command = "aria2c -i list.txt  -c -d ~/Downloads/aria_dl/ -j1 "
    wg_command = "wget -c -i list.txt "
    os.system(wg_command)

def start_aria():
    print("starting aria . .. \n downloading to :")
    os.system("pwd")
    # -O ~/Downloads/dl_py/
    aria_command = "aria2c -i list.txt  -c -d ~/Downloads/aria_dl/ -j1 "
    wg_command = "wget -c -i list.txt "
    os.system(aria_command)

def print_list():
    print()
    os.system("cat list.txt")


def edit_list():
    os.system("nano list.txt")


def shutdown(order):
    if order == "wget" :start_wget()
    if order == "aria" :start_aria()
    os.system("shutdown 10")

def clear():
    os.system('echo "" > list.txt')

# - - -- main program - - - -


while (1 == 1):

    Command = input("\nwhat do you want to do?\nadd html Batch = b \nSingle file = s\nmulti single = bs  \nContinue Download = c\nPrint queue = p\nEdit queue = e\nAuto serial find = a\n")
    command = Command.lower()

    if command in ["continue", "download", "d", "c"]:
        start_wget()

    elif command in ["aria", "ac"]:
        start_aria()

    elif command in ["ariashut" , "ashut"]:
        shutdown("aria")

    elif command in ["shut", "cs", "csh", "shutd"]:
        shutdown("wget")

    elif command in ["single", "s"]:
        add_single()

    elif command in ["a", "auto", "ad"]:
        auto_add()

    elif command in ["bs", "multi", "ms"]:
        add_multi_single()

    elif command in ["batch", "b"]:
        add_batch()

    elif command in ["print", "p"]:
        print_list()

    elif command in ["edit", "e"]:
        edit_list()

    elif command in ["quit", "q", 'exit', "x", "ex"]:
        exit()

    elif command in ["clear"]:
        clear()

    else:
        os.system(Command)

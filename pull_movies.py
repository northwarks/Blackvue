#! /usr/bin/env python
# -*- coding: utf-8

#=======================#
#= NORTHWARKS JAN 2018 =#
#=======================#

# Blackvue 750s Movie Puller v1.0

import socket
import time
import datetime
import sys
import os
import wget
import subprocess
from subprocess import PIPE
import urllib

#============== Check Internet is up ==========================
#Check for Internet, needs 'import socket'
#checking port 80 - could be another eg 8080!
def check_internet(My_URL):
    for timeout in [1,5,10,15,20,30]:
        try:
            socket.setdefaulttimeout(timeout)
            host = socket.gethostbyname(My_URL)
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True
        except Exception,e:
            return False
#=============================================================
# Write log NOTE Log file has to exist e.g. touch file.log
def write_log(some_msg):
  ts = time.time()
  timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
  filepath = "VALID/FILE/PATH/TO/LOG/dash_cam_import.log"
  fh = open(filepath, "a")
  fh.write(timestamp +' - ' + some_msg)
  fh.write("\n")
  fh.close
  return
#============================================================
#Count movies on  DashCam
def count_movies(movie_list):
  movie_count = len(movie_list)
  return movie_count
#=============================================================
#find difference between remote and local files
def check_duplicates(remote_list):
  local_list = []
  diff_list = []
  path = '/VALID/FILE/PATH/TO/MOVIE/FOLDER'
  dirs = os.listdir(path)
  for file in dirs:
    local_list.append(file)
  # Create a list of whats missing and needs downloading
  diff_list = [x for x in remote_list if x not in local_list]
  return diff_list
#=============================================================
#download movies
def download_movies(file_list):
  movie_count = 0
  file_prefix ="http://VALID IP OF BLACKVUE/Record/"
  file_local_folder = '/VALID/FILE/PATH/TO/MOVIE/FOLDER'
  for movie in file_list:
    try:
      url = file_prefix + movie
      pro = subprocess.Popen(['wget', '-O', os.path.join(file_local_folder, movie), url])
      pro.wait() #wait() without this subprocess starts multiple  instances of wget - this forces it to wait for each 1 to finish
      write_log(movie + ' Downloaded OK')
      movie_count = movie_count +1
    except:
      msg = 'Unable to download file - '
      write_log(msg + movie)
      continue
  write_log('Finished - Downloaded ' + str(movie_count) + ' New Movies') 

#=============================================================
#runs from here
def main():
  if check_internet('VALID IP OF BLACKVUE'):
    print 'Conected'
    write_log('Dash Cam Conected')
    movies_toget = get_images()
    download_movies(movies_toget)
  else:
    print 'Not Conected!'
    write_log('Dash Cam Dissconected!')
#============================================================

if __name__== "__main__":
  main()

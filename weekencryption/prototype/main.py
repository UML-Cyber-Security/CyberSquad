# deps
import loger
import encryption
import HashPasswords
import multiprocessor
import LoadBar
import base64
import os
import random
import string
import shutil
import time
import stdiomask
import multiprocessing
from HashPasswords import pass_compare_with_pickle
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from os import urandom, path as file_path
from hashlib import pbkdf2_hmac as hash_algo
from random import choices
from string import ascii_uppercase as uppercase
from string import ascii_lowercase as lowercase
from string import digits
from random import randrange
# end deps

def make_clean():
  [os.remove(file) for file in ['pepper.encrypted', 'pickle.encrypted', 'salt.encrypted', 'userData.encrypted'] if os.path.exists(file)]

if __name__ == '__main__':
  while True:
    if loger.getNumUsers() == 0:
      reg_status = loger.registerUser()
    if reg_status == -1:
      break
    status = input("Login? (y/n) ")
    accept = ['y', 'yes', 'log', 'login', 'log in']
    decline = ['n', 'no', 'nope']
    command = 'make clean'
    valid_responce = accept + decline + [command]
    while status.lower() not in valid_responce:
      status = input("Login? (y/n) ")
    if status.lower() in accept:
      encryption_key, name, email = loger.login()
      print(f'Content Discoverd: ({encryption_key=}, {name=}, {email=})')
      time.sleep(0.5)
      print("logging out",end='\r')
      time.sleep(0.5)
      print("logging out.",end='\r')
      time.sleep(0.2)
      print("logging out..",end='\r')
      time.sleep(0.2)
      print("logging out...")
      continue
    elif status == 'make clean':
      make_clean()
      continue
    else:
      break
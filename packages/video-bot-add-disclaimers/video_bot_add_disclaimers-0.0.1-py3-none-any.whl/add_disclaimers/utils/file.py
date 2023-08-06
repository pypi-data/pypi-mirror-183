import os
import glob
import shutil
from urllib.parse import urlparse


import pickle
import json
import base64



def to_base64(data, decode = True):

    array_bytes = pickle.dumps(data)

    data = base64.b64encode(array_bytes) 
    if (decode == True):
        data = data.decode('ascii')

    return data


def read_binary_file(file):
   with open(file, 'rb') as f:
      return f.read()

def delete_directory(directory):
    shutil.rmtree(directory, ignore_errors=True, onerror=None)

def delete_file(file):
    os.remove(file)

def file_exists(file):
    return os.path.isfile(file)

def delete_all_files(directory):
    files = glob.glob(directory + '/*')
    for f in files:
        delete_file(f)

def get_all_files(directory):
    files = glob.glob(directory + '/*')
    return files


def copy_file(src, dst):
    shutil.copyfile(src, dst)        

def get_url_path(url):
    url_path = urlparse(url).path
    return url_path

def get_url_extension(url):
    url_path = get_url_path(url)
    ext = get_extension(url_path)
    return ext

def get_extension(file):
    try:
        
        ext = os.path.splitext(file)[1]
        ext = str(ext).replace('.', '')
        if (":" in str(ext)):
            ext = str(ext).split(':')[0]

        return ext 
    except:
        return ''    
'''
Version 1.0.3
Lastest Update: 2021.1.26
by Yuzhe H.
'''

import cv2
import numpy as np
import os
import math
from matplotlib import pyplot as plt
from tqdm import tqdm

func_list = [
    'info',
    'del_file_suffix',
    'read_files_in_path',
    'magic_draw',
    'read_lines_in_file',
    'write_lines_to_file',
    'upper_dir',
]

def help(func_name=''):
    if func_name == '':
        for item in func_list:
            print('* '+item)
        func_name = input(':')
    length = len(func_name)
    content = read_lines_in_file('./README.md')
    flag = 0
    for line in content:
        if (line[4:4+length]==func_name):
            flag = 1
        if flag == 0: pass
        else:
            if(line!='----'): print(line)
            else: return 
            
def info(text):
    print('\033[7;32m[info]\033[0m ' + str(text))

def warning(text):
    print('\033[7;33m[WARNING]\033[0m ' + str(text))

def error(text):
    print('\033[7;31m[ERROR]\033[0m ' + str(text))

def debug(text):
    print('\033[7;36;40m[debug]\033[0m ' + str(text))


def del_file_suffix(string):
    for i in range(len(string)):
        if string[-(i+1)] == '.':
            return string[:-(i+1)]
    error()
    print('NO SUFFIX FOUND FOR THE INPUT STRING : "%s" !' % string)

def read_files_in_path(work_path,show_hidden=False):
    if work_path[-1]!='/': work_path += '/'
    if work_path[0]!='~' and work_path[0]!='/': work_path = '/' + work_path
    files, dirs = [], []
    for f in os.listdir(work_path):
        if os.path.isdir(work_path + f):
            dirs.append(f)
        else:
            files.append(f)
    if not show_hidden:
        files = [f for f in files if not f[0] == '.']
        dirs = [d for d in dirs if not d[0] == '.']
    files.sort()
    dirs.sort()
    return files,dirs

def magic_draw(y,
    x = None,
    figsize = (15,6),
    title = None,
    x_label = None,
    y_label = None,
    colors = ['deepskyblue','orange','limegreen','#C82B46','#4EA089','#8B77D0','#93613A','#A5CC4F'],
    alpha = 0.87,
    color_code = None,
    legend = None
    ):

    plt.figure(figsize=figsize)
    plt.grid()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)


    # if multiple input:
    if type(y[0]) == list:
        pics_num = len(y)
        if pics_num > 8:
            error('picture are too many to draw! (max 8 but got %d)' % pics_num)
            return
        # if no input x-coordinate situation:
        if not x:
            x = []
            for data in y:
                x.append(range(len(data)))
        for i in range(pics_num):
            plt.plot(x[i],y[i],alpha=alpha,color=colors[i])

    # if single input:
    else:
        # if no input x-coordinate situation:
        if not x: x = range(len(y))
        # if no color requirement:
        if not color_code:
            color = colors[0]
        # if has requiremnet for color:
        else:
            if type(color_code) == str:
                color = color_code
            elif type(color_code)==int and (color_code>=0 and color_code<=7):
                color = colors[color_code]
            else:
                warning('color code went wrong, automatically choose default.')
        plt.plot(x, y, alpha=alpha, color=color)
    if legend!=None:
        plt.legend(labels=legend, loc='best')
    plt.show()



def read_lines_in_file(file_path):
    f = open(file_path)
    box = []
    for line in f:
        if line!='\n':
            box.append(line[:-1])
    f.close()
    info("file reading finished.")
    return box

def write_lines_to_file(box, file_path, type='a'):
    save = open(file_path,type)
    for line in box:
        print(line, file=save)
    save.close()
    # info("file saving finished.")

import time
def TIMESTAMP():
    string = time.strftime("%Y-%m-%d-%a-%H:%M:%S-%Z", time.localtime())
    return string

def upper_dir(string):
    WAVE_START_flag = False
    if string[-1] == '/': string = string[:-1]
    if string[0] == '~':
        string = string[1:]
        WAVE_START_flag = True

    path_list = string.strip().split('/')
    current = path_list[-1]
    upper_dir = os.path.join('/',*path_list[:-1])
    if WAVE_START_flag: upper_dir = '~'+upper_dir

    return upper_dir,current



















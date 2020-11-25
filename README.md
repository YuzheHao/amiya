# README

### template(`input_arg`, *default_arg*)

#### ---> input (1):
* arg#1 `input_arg` (type): explanation.  
* arg#2 `default_arg=default_value` (type): explanation.

#### ---> output (1):
* return (type): explanation.
* more memo

#### ---> example:
``````python
>>>

``````
----

### info(`text`), warning(`text`), error(`text`), bug(`text`)

* just for highlight some information.
* same usage as `print`


----

### read_files_in_path(`work_path`, *show_hidden*)

#### ---> input (2)：  
* arg#1 `work_path`  (string): a path string, where the files you want to read are in.  
* arg#2 `show_hidden=False` (bool): a flag bool, if it is *False*, the hidden file will be ignored.   

#### ---> output (2)：  
* return#1 `files` (list): a list of strings, which are the names of all files in this path.  
* return#2 `dirs`(list): a list of strings, which are the names of all directories in this path.  
* the returned list have been sorted:  `List.sort()`

#### ---> example:
``````python
>>> files, dirs = read_files_in_path('/User/amiya/Desktop/')
>>> files
['map.jpg','memo.txt','video_tape.mp4']
>>> dirs
['album','resume','normal_files',]

>>> files, dirs = read_files_in_path('/User/amiya/Desktop/',show_hidden=True)
>>> files
['map.jpg','video_tape.mp4','memo.txt','.chen.doc']
>>> dirs
['normal_files','album','resume','.elite_resume']
``````

----

### del_file_suffix(`string`)

#### ---> input (1)：  
* arg#1 `string` (string): a string needed to remove its suffix (usually to be a file name).  

#### ---> output (1)：  
* return (string): the string after the suffix is removed.  

#### ---> example:
``````python
>>> after = del_file_suffix('password_book.txt')
>>> after
'password_book'

>>> after = del_file_suffix('password_book')
>>> after
#print: [ERROR] NO SUFFIX FOUND FOR THE INPUT STRING : "password_book" !
``````

----

### magic_draw(`y`, *x*, *fig_size*, *fig_title*, *x_label*, *y_label*, *color_code*, *colors*, *alpha*)

#### ---> input (1+8):
* **arg#1** `y`(List / Lists' List): list/several lists of data need to be drew. 
* **arg#2** `x=range(len(y))` (List / Lists' List): list/several lists of x-coordinates, default as an one-by-one conuting list.
* arg#3 `figsize=(15,6)` (tuple): the size of figure.
* arg#4 `title=None` (string): title of figure.
* arg#5 `x_lable=None` (string): label shown on x-axis.
* arg#6 `y_lable=None` (string): label shown on y-axis.
* arg#7 `colors=['deepskyblue','orange','limegreen','#C82B46','#4EA089','#8B77D0','#93613A','#A5CC4F']` (list): the color used during drawing (max 8 for input).
* arg#8 `alpha=0.87` (float): the transparent degree.
* **arg#9** `color_code=None` (int / string): the color you want to use when drawing a single curve. if input an integer, then it will use it as index to choose from the colors box; or you could specify a color name/6-digit-Hex-color-code; if input an invalid code, the color will be deepskyblue by default.
* **arg#10** `legend=None` (list of string): the legend you want to show on the figure, the length should be the same as input y and x.

#### ---> output (1):
* show the drew figure 

#### ---> example:
``````python
>>> a = [1,2,2,3,4,5,5,4,1,2,3,1,4]
>>> b = [6,5,8,5,8,6,5,8,5,4,5,7,4]
>>> u = range(len(a))
>>> u1 = [x+20 for x in u]
>>> u2 = [x+15 for x in u]

>>> magic_draw(a)

>>> magic_draw(a,color_code='gold')
>>> magic_draw(a,color_code=3)

>>> magic_draw(a,color_code=999)
#print: [ERROR] color code went wrong, automatically choose default.

>>> magic_draw(b,x=u1)

>>> magic_draw([a,b], x=[u1,u2])
``````
----

### read_lines_in_files(`file_path`)

#### ---> input (1):
* arg#1 `file_path` (string): path of the file which you want to read its content.  

#### ---> output (1):
* return (list): a list of strings, which contains the strings of each line in the file..
* the last char '\n' is deleted during the function.

#### ---> example:
``````python
>>> read_lines_in_files('/home/mydir/myfile.txt')
['first line in file','second line in file','thrid line in file']
``````
----

### write_lines_to_file(`box`, `file_path`, *type='a'*)

#### ---> input (3):
* arg#1 `box` (list of string): the content that you want to write in the file, each string element is the content of a line.  
* arg#2 `file_path`  (string): path of the file which you want to write your content.  
* arg#3 `type='a'` (string): 'w' for overwrite the original content, and default 'a' for append new content to the original text.

#### ---> output (0):
* an info will notice you the writing have finished. 

#### ---> example:
``````python
>>> write_lines_to_file(my_content_list, '/home/mydir/myfile.txt')
#print: file saving finished.
``````
----


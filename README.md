# Text Processing Tool

these are tools used for everyday task automation such as 
- Text slitting with fulltop, excalmation marks and question marks with option of adding spaces or not
- removing urls from a txt file
- remove hashtags and more.

## How to use it

the tools are made using python and javascript (on Nodejs runtime). hence, to use it make sure [python interpreter](https://www.python.org/downloads/) and  [nodejs](https://nodejs.org/) are installed in your computer.

### Nodejs

make sure to run
``` javascript
 npm install
```

### for Python
Make sure to install the necessary packages

## for text cleaning

This module was written with  nodejs runtime. The python script is still being worked on.

the script takes three parameters, hence
- "target_file"
- desctintion_file
- --no-space=yes|no

therefore, to use this script just run;
``` javascript
node clean_text.js [target file] [destination file] --no-space=yes|no 
```
- the no space attribut specifies if you want an empty line after each splitted sentences. :Yes" means leave a space after each line of sentences while "no" means no empty lines.
- "target file" is the file to be cleaned.
- "destination file" is the new file to create 

## remove URLs

the remove url script is written with python. hence,
```python
python3 remove_url.py [target file]
```
- "target file" is the file you want to remove the urls from

## remove all hashtasg

the remove hashtags script is written with python. hence,
```python
python3 remove_all_hashtags.py [target file]
```
- "target file" is the file you want to remove the hashtags from

*NOTE: its a work in progress. the intention is ease and automate everyday task at work. Also, aspect written with the nodejs runtime are being re-written to python script* 


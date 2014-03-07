# -*- coding: utf-8 -*-
'''
Created on 17/07/2013

@author: Roque E. Lopez
'''
import re

def get_words(text):
    ''' Returns a word list of a text '''
    return [x for x in re.split("\s+", text) if len(x) > 0] 

def read_file(file_path):
    ''' Get the text of a file '''
    my_file = open(file_path,"r",encoding='latin1')#, errors='ignore')
    text = my_file.read()
    my_file.close()
    return text 

def clear_text(text):
    ''' Removes special symbols of text '''
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.lower()
    return text

def stop_words_list():
    ''' Creates a list of stopwords '''
    my_list = dict()
    file = open("../resource/lexical/stopwords_portugues.txt", 'r', encoding='latin1')
    while True:
        line = file.readline()
        if not line: break
        my_list[line.strip()] = None
    file.close()
    return my_list


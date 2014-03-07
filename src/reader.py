# -*- coding: utf-8 -*-
'''
Created on 17/07/2013

@author: Roque E. Lopez
'''
import os
import utils
from jing.cluster import Cluster
from bs4 import BeautifulSoup


class Reader(object):
    '''
    Class that reads a summary and the original documents in file format
    '''

    def read_alignments(self, folder_path):
        ''' Reads the xml files with the manual alignments '''
        cluster_list = dict()# contents the manual alignments: {'id_cluster':{'id_sentence':[doc1,...,docn]}}
        for file in os.listdir(folder_path):
            text_document = utils.read_file(os.path.join(folder_path, file))
            id_cluster = file.split('_')[0]
            cluster_list[id_cluster] = dict()
            soup = BeautifulSoup(text_document)
         
            for sentence in soup.findAll('align'):
                cluster_list[id_cluster][sentence.get('sent')] = list()
                for doc in sentence.findAll('doc'):
                    cluster_list[id_cluster][sentence.get('sent')].append((doc.get('name'), doc.get('sent')))
        
        return cluster_list
    
    def read_clusters(self, folder_path):
        ''' Reads the test files '''
        files = os.listdir(folder_path) 
        #files.sort()
        summaries = [x for x in files if x.find('_summary') > 0]
        cluster_list = dict()# cluster list
        
        for summary in summaries:
            id_cluster = summary.split('_')[0]
            raw_cluster = [x for x in files if x.find('_'+id_cluster) > 0] 

            cluster = Cluster(True)
            text = utils.read_file(os.path.join(folder_path, summary))
            cluster.add_summary(text)
            
            for document_name in raw_cluster:
                text = utils.read_file(os.path.join(folder_path, document_name))
                cluster.add_document(document_name, text)
                 
            cluster_list[id_cluster] = cluster
        return cluster_list
    

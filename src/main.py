'''
Created on 16/07/2013

@author: Roque E. Lopez
'''
from reader import Reader
      
if __name__ == '__main__':

    folder_cstnews_corpus = "../resource/data/corpus/"
    reader = Reader()
    cluster_list = reader.read_clusters(folder_cstnews_corpus)
       
    jing_alignments = dict()
           
    for id_cluster, cluster in cluster_list.items():
        cluster.create_pairs()
        cluster.create_hmms()
        jing_alignments[id_cluster] = cluster.get_alignment()

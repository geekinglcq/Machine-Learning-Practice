#-*- coding:utf-8 -*-   

from utility import *
from node import Node 

class Tree():

    def __init__(self, mode='Gain'):
        self.root = Node()
        self.queue = [self.root]
        self.mode = mode

    def train(self, data):
        i = 0
        print(i)
        self.root.dataID = data.index
        self.root.props = get_properties_dict(data)
        self.labels = list(data['label'].unique())  
        while i < len(self.queue):
            new_nodes = self.queue[i].split(data)
            if new_nodes is not None:
                self.queue.extend(new_nodes)
            i += 1

    def infer(self, sample):

        res = self.root 
        while res not in self.labels:
            
            res = res.infer(sample)
        print(res)
        return res
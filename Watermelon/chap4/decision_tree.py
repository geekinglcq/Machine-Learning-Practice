#-*- coding:utf-8 -*-   

from utility import *
from node import Node 

class Tree():

    def __init__(self, mode='Gain', prune='no'):
        assert mode in set(['Gain', 'Gini'])
        assert prune in set(['no', 'pre','post'])
        self.root = Node()
        self.queue = [self.root]
        self.mode = mode
        self.prune = prune

    def train(self, data):
        i = 0
        self.labels = list(data['label'].unique())  
        self.root.props = get_properties_dict(data)
        if self.prune != 'no' or len(data) >= 50 :
            msk = np.random.rand(len(data)) < 0.8
            val_data = data[~msk]
            data = data[msk]

        self.root.dataID = data.index
        
        
        while i < len(self.queue):
            if self.prune == 'pre':
                new_nodes = self.queue[i].split(data, val_data, self.prune, mode=self.mode)
            else:
                new_nodes = self.queue[i].split(data, mode=self.mode)
            
            if new_nodes is not None:
                self.queue.extend(new_nodes)
            i += 1

        if self.prune == 'post':
            for cur_node in self.queue[::-1]:
                
                flag = post_pruning(cur_node, data, val_data)
                if flag:
                    cur_node.split_prop = None
                    cur_node.label = data.loc[cur_node.dataID]['label'].value_counts().argmax()
                    for son in cur_node.sons:
                        son.label = None
                        son.split_prop = None
                    cur_node.sons = []

            new_queue = []
            for i in self.queue:
                if not(i.label == None and i.split_prop == None):
                    new_queue.append(i)
            self.queue = new_queue
        
        print('Training Done.')
        acc = 0
        for i in data.index:
            pred = self.infer(data.loc[i])
            if pred == data.loc[i]['label']:
                acc += 1
        print(acc, len(data))
        acc = acc / len(data)
        print('Acc in Training Set: %f'%(acc))
        
        if self.prune != 'no' or len(data) >= 50 :
            valacc = 0
            
            for i in val_data.index:
                pred = self.infer(val_data.loc[i])
                if pred == val_data.loc[i]['label']:
                    valacc += 1
            print(valacc, len(val_data))
            valacc = valacc / len(val_data)
            print('Acc in Validation Set: %f'%(valacc))
        return acc, valacc
    def infer(self, sample):
        res = self.root 
        while res not in self.labels:
            
            res = res.infer(sample)
        
        return res
#-*- coding:utf-8 -*-   

from utility import *  
from copy import deepcopy
class Node():
    """
    Format of props {name: {type:C(ontinuous)/D(iscrete), values:[a,b,c]}}
    """
    def __init__(self, label=None, dataID=set(), props=set(), father=None):
        self.label = None
        self.dataID = []
        self.props = set()
        self.split_prop = None
        self.father = father
        self.sons = []  

    def split(self, data, val_data=None, prune='no', mode='Gain'):  
        """
        If split successfully, return the new nodes,
        else return None (label self as leaf).
        """
        assert mode in ['Gain', 'Gini', 'Lr']   

        if len(self.dataID) == 0:
            return None    
        # print('aa',self.dataID)
        # print(data.loc[self.dataID])
        labels = check_data_label(data, self.dataID)
        
        # suitation 1  
        if len(labels) == 1:
            self.label = labels.most_common(1)[0][0]    
            return None
        
        # suitation 2 
        if len(self.props) == 0 or check_data_props(data, self.dataID, self.props):
            self.label = get_maj_label(data, self.dataID)
            return None

        # suitation 3  
    
        prop = select_best_prop(data, self.dataID, self.props, mode=mode)

        # pre-pruning 
        if prune == 'pre':
            if pre_pruning(data, self.dataID, val_data, self.props[prop]):
                self.label = data.loc[self.dataID]['label'].value_counts().argmax()
                return None

        left_props = deepcopy(self.props)
        del left_props[prop]
        self.split_prop = {'name':prop, 'type':self.props[prop]['type'], 'values':self.props[prop]['values']}


        if self.props[prop]['type'] == 'D':
            for v in self.props[prop]['values']:
                subsetID = get_subdata(data, self.dataID, prop, v).index
                son = Node()
                if len(subsetID) == 0:
                    son.label = labels.most_common(1)[0][0]
                son.father = self 
                son.dataID = subsetID
                son.props = left_props
                self.sons.append(son)

        return self.sons  

    def infer(self, sample):
        if self.label is not None:
            return self.label 
        if self.split_prop['type'] == 'D':
            sample_value = sample[self.split_prop['name']]
            for i, v in enumerate(self.split_prop['values']):
                if v == sample_value:
                    
                    return self.sons[i]


                


        







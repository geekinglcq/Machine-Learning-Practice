#-*- coding:utf-8  -*-

import math

import numpy as np
from collections import Counter

def check_data_label(data, dataID):
    """
    Return the Counter of data labels
    """
    # print(dataID)
    subdata = data.loc[dataID] 
    labels = Counter(subdata['label'])
    return labels

def check_data_props(data, dataID, props):
    """
    Check if the given properties of data are all the same
    """
    subdata = data.loc[dataID]
    for p in props:
        if len(data[p].unique()) > 1:
            return False
    return True

def get_maj_label(data, dataID):
    """
    Get the majority of label in given dataset
    """
    labels = check_data_label(data, dataID)
    label = labels.most_common(1)[0][0]
    return label  


def get_subdata(data, dataID, prop, v):
    
    subdata = data.loc[dataID]
    return subdata[subdata[prop] == v]

def select_best_prop(data, dataID, props, mode='Gain'):
    assert mode in ['Gain', 'Gini', 'Lr']
    if mode == 'Gain':
        return infogain_selector(data, dataID, props)
    if mode == 'Gini':
        return ginindex_selector(data, dataID, props)
    if mode == 'Lr':
        return logit_selector(data, dataID, props)

    return list(props)[0]

def get_properties_dict(data):
    
    prop_names = set(data.columns) - set(['label'])
    props = {}
    for name in prop_names:
        temp = {}   
        if len(data[name].unique()) == data[name].max() - data[name].min() + 1:
            temp['type'] = 'D'
            temp['values'] = list(data[name].unique())
        else:
            temp['type'] = 'C'
            temp['values'] = [data[name].min(), data[name].max()]
        temp['name'] = name
        props[name] = temp
    return props

def infogain_selector(data, dataID, props):
    subdata = data.loc[dataID]
    maxgain = -1024
    
    for prop in props.keys():
        infogain = cal_gain(subdata, props[prop])
        
        if infogain > maxgain:
            maxgain = infogain
            candinate = prop
    return candinate

def ginindex_selector(data, dataID, props):
    subdata = data.loc[dataID]
    minginindex = 1024
    
    for prop in props.keys():
        ginindex = cal_ginindex(subdata, props[prop])
        
        if ginindex < minginindex:
            minginindex = ginindex
            candinate = prop
    return candinate

def logit_selector(data, dataID, props):
    subdata = data.loc[dataID]

def cal_gain(data, prop):
    """
    Calcluate the infomation gain of given property in certain dataset
    """
    info_gain = 0
    global_ent = cal_entropy(data)
    total_count = len(data)
    for v in prop['values']:
        subdata = data[data[prop['name']] == v]
        count = len(subdata)
        info_gain -= count/total_count * cal_entropy(subdata)
    info_gain += global_ent
    return info_gain

def cal_entropy(data):
    """
    Calculate the infomation entropy. 
    """
    ent = 0
    total = len(data)
    for l in data['label'].unique():
        p = len(data[data['label'] == l]) / total
        ent -= p * math.log2(p)
    return ent 

def cal_ginindex(data, prop):
    """
    Calculate the gini index 
    """
    ginindex = 0
    total_count = len(data)
    for v in prop['values']:
        subdata = data[data[prop['name']] == v]
        count = len(subdata)
        ginindex += count/total_count * cal_gini(subdata)
    
    return ginindex

def cal_gini(data):
    """
    Calculate the gini
    """
    gini = 1
    total = len(data)
    for l in data['label'].unique():
        p = len(data[data['label'] == l]) / total
        gini -= p*p 
    return gini 

def pre_pruning(data, dataID, val_data, prop):
    subdata = data.loc[dataID]
    total_count = len(val_data)
    label = subdata['label'].value_counts().argmax()
    acc = len(val_data[val_data['label']==label]) / total_count
    correct_count = 0 
    
    for v in prop['values']:
        temp = subdata[subdata[prop['name']]==v]
        temp_val = val_data[val_data[prop['name']]==v]
        if len(temp) > 0:
            label = temp['label'].value_counts().argmax()
        correct_count += len(temp[temp['label'] == label])
    new_acc = correct_count / total_count  
    if new_acc >= acc:
        return False
    else:
        return True

def post_pruning(node, data, val_data):
    if node.split_prop == None:
        return False

    subdata = data.loc[node.dataID]
    total_count = len(val_data)
    label = subdata['label'].value_counts().argmax()
    acc = len(val_data[val_data['label']==label]) / total_count
    correct_count = 0 
    
    for v in node.split_prop['values']:
        temp = subdata[subdata[node.split_prop['name']]==v]
        temp_val = val_data[val_data[node.split_prop['name']]==v]
        if len(temp) > 0:
            label = temp['label'].value_counts().argmax()
        correct_count += len(temp[temp['label'] == label])
    new_acc = correct_count / total_count  
    if new_acc >= acc:
        return False
    else:
        return True
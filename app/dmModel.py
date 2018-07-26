import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydotplus
import collections
import pickle
import csv
# %matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from app.decTree import *
from sklearn import tree
from subprocess import check_call

def dmModel():
    # Generate model using predetermined training and test sets
    # trgdata= pd.read_csv('/home/alton/Documents/Cricdess Data/trgdataV1.csv',delimiter=',')
    # tstdata=pd.read_csv('/home/alton/Documents/Cricdess Data/testdataV1.csv',delimiter=',')
    # X=trgdata.drop('win_lose',axis=1)
    # Y=tstdata['win_lose']
    # x_test=tstdata.drop('win_lose',axis=1)
    # x_train=trgdata.drop('win_lose',axis=1)
    # y_train=trgdata['win_lose']
    # y_test=tstdata['win_lose']

    #Generate model using dynamic split
    file='working_model.sav'
    data=pd.read_csv('mod_data.csv',delimiter=',')
    X=data.drop('win_lose',axis=1)
    Y=data['win_lose']
    # print (Y)
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.20)
    x_test.to_csv('x_test.csv',mode='w+',header=True,index=False)
    y_test.to_csv('y_test.csv',mode='w+',header=True,index=False)
    # print("X_train")
    # print(x_train)
    # print("Y_train")
    # print(y_train)
    write(file,X,x_train,x_test,y_train,y_test)
    # print(decTree(file,x_test,y_test))

def write(file,X,x_train,x_test,y_train,y_test):
    classifier = tree.DecisionTreeClassifier(min_samples_split=7,min_samples_leaf=10,criterion='entropy')
    # print (classifier)
    classifier.fit(x_train,y_train)
    y_pred= classifier.predict(x_test)
    # print("X-matrix")
    # print (pd.DataFrame(confusion_matrix(y_test, y_pred),columns=['0','1'],index=['0','1']))
    # print (classification_report(y_test,y_pred))

    #Generate Tree and save to file
    dot_data=tree.export_graphviz(classifier,out_file=None,feature_names=X.columns,class_names=True)
    graph = pydotplus.graph_from_dot_data(dot_data)
    colors = ('turquoise', 'orange')
    edges = collections.defaultdict(list)
    for edge in graph.get_edge_list():
        edges[edge.get_source()].append(int(edge.get_destination()))
    for edge in edges:
        edges[edge].sort()
        for i in range(2):
            dest = graph.get_node(str(edges[edge][i]))[0]
            dest.set_fillcolor(colors[i])
    graph.write_png('tree.png')

    #Save model to disk
    pickle.dump(classifier,open(file,'wb'))

def decTree():
    file='./working_model.sav'
    x_test=pd.read_csv('x_test.csv')
    y_test=pd.read_csv('y_test.csv')
    model=pickle.load(open(file,'rb'))
    result=model.score(x_test,y_test)
    y_pred=model.predict(x_test)
    print ("THE Model")
    print (pd.DataFrame(confusion_matrix(y_test, y_pred),columns=['0','1'],index=['0','1']))
    matrix=pd.DataFrame(confusion_matrix(y_test, y_pred),columns=['0','1'],index=['0','1'])
    print (result)
    return ("Accuracy of the model: "+str(result))
    # return(result)

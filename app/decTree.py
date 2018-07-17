import pickle
def decTree(file):
    model=pickle.load(open(file,'rb'))
    print ("THE Model")
    print (model)
    result=model.score(x_test,y_test)
    return result

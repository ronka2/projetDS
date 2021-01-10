import pickle

infile = open('C:/Users/arons/Desktop/PythonforDS/projetDS/apiDS/prediction/modeleDecisionTree.pkl','rb')
modelDecisionTree = pickle.load(infile)
infile.close()

infileForest = open('C:/Users/arons/Desktop/PythonforDS/projetDS/apiDS/prediction/modeleRandomForest.pkl','rb')
modelRandomForest = pickle.load(infileForest)
infileForest.close()
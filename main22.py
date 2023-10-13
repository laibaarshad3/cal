import argparse

parser = argparse.ArgumentParser()

parser.add_argument('Pclass' , type = int)
parser.add_argument('Age', type = float)
parser.add_argument('SibSp'  , type = int)
parser.add_argument('Parch'  , type = int)
parser.add_argument('Fare' , type = float)
parser.add_argument('Sex'  , type = str)
parser.add_argument('Embarked' , type = str )

args = parser.parse_args()

list = [list] 

list.append(args.Pclass)
list.append(args.Age)
list.append(args.SibSp)
list.append(args.Parch)
list.append(args.Fare)

if args.Sex == "male":
    list.append(1)
    list.append(0)
elif args.Sex == "female":
    list.append(0)
    list.append(1)

if args.Embarked == "S":
    list.append(1)
    list.append(0)
    list.append(0)
elif args.Embarked == "C":
    list.append(0)
    list.append(1)
    list.append(0)
elif args.Embarked == "Q":
    list.append(0)
    list.append(0)
    list.append(1)


list = [list]
import pandas as pd
dfn = pd.DataFrame(list , columns=(["Pclass","Age",'SibSp','Parch','Fare','S', "C","Q","male","female"]))
import joblib
import numpy as np

model = joblib.load("joblib_model.pkl")
pred = model.predict(dfn)
pred=pred[0]
if pred == 1:
    print(list ," : survived")
else:
    print(list ," : non_survived")

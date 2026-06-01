import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import StratifiedShuffleSplit,train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score,classification_report)
import joblib

df = pd.read_csv('synthetic_tickets.csv')
print(df.head())
X = df['ticket_text']
Y = df['category']

X_train,X_test,Y_train,Y_test = train_test_split(
    X,Y,test_size=0.2,random_state=42,stratify=Y
)
# print(X_train.head())
pipeline = Pipeline([
    ('tfid',TfidfVectorizer(
        max_features=3000,
        ngram_range=(1,2)
        
    )),
    
    (
        'clf',LogisticRegression(max_iter=1000)
    )

])
pipeline.fit(
    X_train,Y_train
)
y_pred = pipeline.predict(
    X_test
)
print(f'Accuracy Score: {accuracy_score(Y_test,y_pred)}')
print(f'classification_report: {classification_report(Y_test,y_pred)}')
test_cases = [

    "Money was deducted twice from my bank account",

    "I cannot access my account after resetting password",

    "Please terminate my membership immediately",

    "Need help choosing the correct laptop",

    "I returned the product but still have not received my money"
]

for text in test_cases:

    print(text)

    print(pipeline.predict([text])[0])

    print()
    
joblib.dump(
    pipeline,
    "ticket_classifier.pkl"
)
import logging
import pandas as pd
import numpy as np
from numpy import random
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
import re
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import pymongo
import urllib3, json, praw
import pandas as pd
import datetime as dt
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
key="oHTDjY6PXRFS8Z1wBcDXELm5xy4" #(Secret)
user_key="OIO_pHHa-LQfHA"
username="divyamb29"
reddit = praw.Reddit(client_id=user_key,
                     client_secret=key,
                     user_agent=username)
subreddit = reddit.subreddit('india')
client = pymongo.MongoClient("mongodb+srv://admin:divyam@precog-z500c.mongodb.net/test?retryWrites=true&w=majority")
mydb = client.get_database("India")
database=mydb.reddit_india
posts=list(database.find())
df=pd.DataFrame(posts)
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
# STOPWORDS = set(stopwords.words('english'))

# def clean_text(text):
#     text = BeautifulSoup(text, "lxml").text
#     text = text.lower() 
#     text = REPLACE_BY_SPACE_RE.sub(' ', text) 
#     text = BAD_SYMBOLS_RE.sub('', text)
#     text = ' '.join(word for word in text.split() if word not in STOPWORDS)
#     return text
df=df[df['flair'].notnull()]
df=df[df['post'].notnull()]
# df['all'] = df['all'].apply(clean_text)
# df['all'].apply(lambda x: len(x.split(' '))).sum()
X_train = df.title
y_train = df.flair
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 10)
uni_flairs=df.flair.unique()

nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])
nb.fit(X_train, y_train)


logreg = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', LogisticRegression(n_jobs=1, C=1e5)),
               ])
logreg.fit(X_train, y_train)

sgd = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),
               ])
sgd.fit(X_train, y_train)
other=11
i_dontknow=other +10

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      r=result.to_dict()
      sub=reddit.submission(url=r["URL"])
      x=sub.title
      y=nb.predict([x])
      print(r['algo'])
      if r['algo']=='Naive Bayes':
      	y=nb.predict([x])
      	print("NB")
      if r['algo']=='Logistic Regression':
      	y=logreg.predict([x])
      	print("LR")
      if r['algo']=='Linear Support Vector Machine':
      	y=sgd.predict([x])
      	print("LSVM")

      return render_template("class.html",result = y[0])

if __name__ == '__main__':
   app.run(debug = True)

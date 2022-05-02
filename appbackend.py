from flask_ngrok import run_with_ngrok
from flask import Flask
from flask import request
from flask import jsonify
import pymongo
from flask_cors import CORS, cross_origin
import random
from pymongo import MongoClient
# import os

app = Flask(__name__)
CORS(app, support_credentials=True)
run_with_ngrok(app)
@app.route('/')
def home():
  return '<h1>Hello from Flask</h1>'

@app.route('/greeting')
def greeting():
  name=request.args.get('name')
  return '<h3>Hello '+name+'</h3>'

# @app.route('/insert')
# def insert():
#   name=request.args.get('name')
#   desc=request.args.get('desc')
#   ratings=request.args.get('ratings')
#   prange=request.args.get('prange')
#   tags=request.args.get('tags')
#   client=MongoClient("mongodb+srv://testuser:beam4456@cluster0.ntixl.mongodb.net/Demo1?retryWrites=true&w=majority")
#   db=client.landmarks_db
#   db.landmarks.insert_one({'name':name,'desc':desc,'ratings':int(ratings),'prange':float(prange),'tags':tags})
#   return '<h3>Finished</h3>'

@app.route('/insert', methods=['POST'])
def insert():
  client=MongoClient("mongodb+srv://testuser:beam4456@cluster0.ntixl.mongodb.net/Demo1?retryWrites=true&w=majority")
  db = client.landmarks_db.landmarks
  newData = request.json
  db.insert_one({
      'name': newData['name'],
      'desc': newData['desc'],
      'ratings': int(newData['ratings']),
      'prange': float(newData['prange']),
      'tags': newData['tags']
  })
  return {'status':'done'}, 200


@app.route('/get')
def get():
  id=request.args.get('id')
  client=MongoClient("mongodb+srv://testuser:beam4456@cluster0.ntixl.mongodb.net/Demo1?retryWrites=true&w=majority")
  db=client.landmarks_db
  res=db.landmarks.find_one({'name':id})
  ret=dict()
  res.pop('_id',None)
  ret['data']=res
  return jsonify(ret)

@app.route('/getRandom')
def getRandom():
  ret=dict()
  id=int(request.args.get('id'))
  client=MongoClient("mongodb+srv://testuser:beam4456@cluster0.ntixl.mongodb.net/Demo1?retryWrites=true&w=majority")
  db=client.landmarks_db
  doc=db.landmarks.find({})
  res=[]
  for docs in doc[id:id+10]:
    res.append({'name': docs['name'],'desc':docs['desc'],'ratings':docs['ratings'],'prange':docs['prange'],'tags':docs['tags']})
  ret['data']=res
  return jsonify(ret)

@app.route('/getAll')
def getAll():
  ret=dict()
  client=MongoClient("mongodb+srv://testuser:beam4456@cluster0.ntixl.mongodb.net/Demo1?retryWrites=true&w=majority")
  db=client.landmarks_db
  doc=db.landmarks.find({})
  res=[]
  rate0=[]
  rate1=[]
  rate2=[]
  rate3=[]
  rate4=[]
  rate5=[]
  rate6=[]
  rate7=[]
  rate8=[]
  rate9=[]
  rate10=[]
  # allratingstuple=[]
  allratings=[0 for i in range(11)]
  for docs in doc:
    res.append({'name': docs['name'],'desc':docs['desc'],'ratings':docs['ratings'],'prange':docs['prange'],'tags':docs['tags']})
    ret['data']=res
    for item in res:
      if (item['ratings'] == 0): rate0.append(item['prange'])
      if (item['ratings'] == 1): rate1.append(item['prange'])
      if (item['ratings'] == 2): rate2.append(item['prange'])
      if (item['ratings'] == 3): rate3.append(item['prange'])
      if (item['ratings'] == 4): rate4.append(item['prange'])
      if (item['ratings'] == 5): rate5.append(item['prange'])
      if (item['ratings'] == 6): rate6.append(item['prange'])
      if (item['ratings'] == 7): rate7.append(item['prange'])
      if (item['ratings'] == 8): rate8.append(item['prange'])
      if (item['ratings'] == 9): rate9.append(item['prange'])
      if (item['ratings'] == 10): rate10.append(item['prange'])
  tempsum=0
  for item in rate0:
    tempsum += item
  allratings[0]+=(tempsum/len(rate0))
  tempsum=0
  for item in rate1:
    tempsum += item
  allratings[1]+=(tempsum/len(rate1))
  tempsum=0
  for item in rate2:
    tempsum += item
  allratings[2]+=(tempsum/len(rate2))
  tempsum=0
  for item in rate3:
    tempsum += item
  allratings[3]+=(tempsum/len(rate3))
  tempsum=0
  for item in rate4:
    tempsum += item
  allratings[4]+=(tempsum/len(rate4))
  tempsum=0
  for item in rate5:
    tempsum += item
  allratings[5]+=(tempsum/len(rate5))
  tempsum=0
  for item in rate6:
    tempsum += item
  allratings[6]+=(tempsum/len(rate6))
  tempsum=0
  for item in rate7:
    tempsum += item
  allratings[7]+=(tempsum/len(rate7))
  tempsum=0
  for item in rate8:
    tempsum += item
  allratings[8]+=(tempsum/len(rate8))
  tempsum=0
  for item in rate9:
    tempsum += item
  allratings[9]+=(tempsum/len(rate9))
  tempsum=0
  for item in rate10:
    tempsum += item
  allratings[10]+=(tempsum/len(rate10))
  ret['data']=allratings
  return jsonify(ret)

app.run()

  client=MongoClient("mongodb+srv://testuser:beam4456@cluster0.ntixl.mongodb.net/Demo1?retryWrites=true&w=majority")
  db=client.landmarks_db
  doc=db.landmarks.find({})
  for docs in doc[0:2]:
    print(docs)

## DATA ANALYSIS

  import pymongo
  from pymongo import MongoClient

  client=MongoClient("mongodb+srv://testuser:beam4456@cluster0.ntixl.mongodb.net/Demo1?retryWrites=true&w=majority")
  db=client.landmarks_db
  document1=db.landmarks

document1.find_one({}).keys()

from collections import Counter

document2 = document1.find({})
ratings = []
prange = []
tags = []
for doc in document2:
  # print(doc['name'])
  # print(doc['ratings'])
  # print(doc['prange'])
  # print(doc['tags'])
  # print('===============')
  ratings.append(doc['ratings'])
  prange.append(doc['prange'])
  tags.append(doc['tags'])

points = [(ratings[i],prange[i]) for i in range(len(ratings))]
typelandmark = [tags[i][0] for i in range(len(tags))]
inout = [tags[i][1] for i in range(len(tags))]
subtags = [tags[i][2:] for i in range(len(tags))]
tags_df = [(typelandmark[i],inout[i],subtags[i]) for i in range(len(typelandmark))]
prange_type_df = [(typelandmark[i],prange[i]) for i in range(len(typelandmark))]
print(ratings)
print(prange)
print(points)
print(tags)
print(typelandmark)
print(inout)
print(subtags)
print(tags_df)
print(prange_type_df)

import plotly.express as px
import plotly.io
import plotly
# plotly.io.orca.config.executable = '/path/to/orca'
# plotly.io.orca.config.save()

df = points
fig1 = px.scatter(df, x=ratings, y=prange, trendline="ols",labels={'x':'ratings','y':'price($)'}, title='Graph showing correlation (trendline) between price and ratings of landmarks')
fig1.show()

fig1_json

import plotly.express as px
df = prange_type_df
fig2 = px.box(df, x=typelandmark, y=prange, labels={'x':'type of landmark','y':'price($)'}, title='Graph showing correlation between each type of landmarks and their respective prices')
fig.show()

ret=dict()
client=MongoClient("mongodb+srv://testuser:beam4456@cluster0.ntixl.mongodb.net/Demo1?retryWrites=true&w=majority")
db=client.landmarks_db
doc=db.landmarks.find({})
res=[]
rate0=[]
rate1=[]
rate2=[]
rate3=[]
rate4=[]
rate5=[]
rate6=[]
rate7=[]
rate8=[]
rate9=[]
rate10=[]
allratings=[0 for i in range(11)]
for docs in doc:
  res.append({'name': docs['name'],'desc':docs['desc'],'ratings':docs['ratings'],'prange':docs['prange'],'tags':docs['tags']})
ret['data']=res
for item in res:
  if (item['ratings'] == 0): rate0.append(item['prange'])
  if (item['ratings'] == 1): rate1.append(item['prange'])
  if (item['ratings'] == 2): rate2.append(item['prange'])
  if (item['ratings'] == 3): rate3.append(item['prange'])
  if (item['ratings'] == 4): rate4.append(item['prange'])
  if (item['ratings'] == 5): rate5.append(item['prange'])
  if (item['ratings'] == 6): rate6.append(item['prange'])
  if (item['ratings'] == 7): rate7.append(item['prange'])
  if (item['ratings'] == 8): rate8.append(item['prange'])
  if (item['ratings'] == 9): rate9.append(item['prange'])
  if (item['ratings'] == 10): rate10.append(item['prange'])
tempsum=0
for item in rate0:
  tempsum += item
allratings[0]+=(tempsum/len(rate0))
tempsum=0
for item in rate1:
  tempsum += item
allratings[1]+=(tempsum/len(rate1))
tempsum=0
for item in rate2:
  tempsum += item
allratings[2]+=(tempsum/len(rate2))
tempsum=0
for item in rate3:
  tempsum += item
allratings[3]+=(tempsum/len(rate3))
tempsum=0
for item in rate4:
  tempsum += item
allratings[4]+=(tempsum/len(rate4))
tempsum=0
for item in rate5:
  tempsum += item
allratings[5]+=(tempsum/len(rate5))
tempsum=0
for item in rate6:
  tempsum += item
allratings[6]+=(tempsum/len(rate6))
tempsum=0
for item in rate7:
  tempsum += item
allratings[7]+=(tempsum/len(rate7))
tempsum=0
for item in rate8:
  tempsum += item
allratings[8]+=(tempsum/len(rate8))
tempsum=0
for item in rate9:
  tempsum += item
allratings[9]+=(tempsum/len(rate9))
tempsum=0
for item in rate10:
  tempsum += item
allratings[10]+=(tempsum/len(rate10))
print(allratings)

##6c1dae2c00713f6c11aa7a1f9ed80718c1976edf
##price-monitoring-project
##Project number 
##227690852185
##Default GCP resource location 
##nam5 (us-central)
##Web API Key
##AIzaSyCY4UkpSL-aCQRVHum00c654-RDewMQCaA



##import pyrebase config = {
##
##  "apiKey": "AIzaSyCY4UkpSL-aCQRVHum00c654-RDewMQCaA",
##
##  "authDomain": "price-monitoring-project.firebaseapp.com",
##
##  "databaseURL": "https://console.firebase.google.com/u/0/project/price-monitoring-project/firestore/data~2Fphones~2F1",
##
##  "storageBucket": "price-monitoring-project.appspot.com",
##
##  "serviceAccount": "C:\\Users\\eiti mittal\\Downloads\\price-monitoring-project-firebase.json"
##
##}
##firebase = pyrebase.initialize_app(config)

import firebase_admin
from firebase_admin import credentials,firestore
import json

cd = credentials.Certificate("price-monitoring-pwa-firebase.json")

firebase_admin.initialize_app(cd)
db = firestore.client()

data = []
for line in open('search_results_output.json', 'r'):
    data.append(json.loads(line))

print(len(data))
for i in range(len(data)):
    doc_ref = db.collection(u'phones').document(data[i].get('title'))
    doc_ref.set(data[i])

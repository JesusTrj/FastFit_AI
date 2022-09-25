import json
import urllib

import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from fastai.vision.all import *
from fastai.imports import *

import pymysql
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

db_connect = pymysql.connect(
     host="10.22.190.73",
     port=3306,
     user="hack_mty",
     password="8VgYu9EHLb88GNW4tKCF",
     database="hackmty_fit")

my_cursor = db_connect.cursor()

type_dict = {    # category, formality, weather
"Anorak" :        (1, 1, 3),
"Blazer":         (1, 3, 2),
"Blouse":         (1, 2, 2),
"Bomber" :        (1, 2, 3),
"Button-Down":    (1, 2, 2 ),
"Cardigan" :      (1, 2, 3),
"Flannel" :       (1, 2, 3),
"Halter":         (1,2,2),
"Henley" :        (1, 2,3),
"Hoodie" :        (1, 2, 3),
"Jacket" :        (1, 2, 3),
"Jersey"  :       (1, 1, 2),
"Parka"   :       (1,2,3),
"Peacoat" :       (1,3,3),
"Poncho" :        (1,2,3),
"Sweater"  :      (1,2,3),
"Tank" :          (1,3,2),
"Tee" :           (1,2,2),
"Top"  :          (1,2,2),
"Turtleneck" :    (1,3,3),
"Capris" :        (2,2,2),
"Chinos"  :       (2,2,2),
"Culottes"  :     (2,2,2),
"Cutoffs" :       (2,2,2),
"Gauchos"  :      (2,2,2),
"Jeans" :         (2,2,2),
"Jeggings" :      (2,2,2),
"Jodhpurs"  :     (2,1,2),
"Joggers"  :      (2,1,3),
"Leggings"  :     (2,1,2),
"Sarong"  :       (2,2,2),
"Shorts"  :       (2,2,2),
"Skirt"   :       (2, 2,2),
"Sweatpants" :    (2, 1, 3),
"Sweatshorts" :   (2, 1, 2 ),
"Trunks"       :  (2, 1, 2),
"Caftan"       :  (4,3,2),
"Cape"         :  (4,3,3),
"Coat"         :  (4, 3, 3),
"Coverup"      :  (4, 2, 2),
"Dress"        :  (4, 2, 2),
"Jumpsuit"     :  (4, 2, 2),
"Kaftan"        : (4, 3, 2),
"Kimono"         :(4, 3, 2),
"Nightdress"     :(4, 2, 2),
"Onesie"         :(4, 2, 2),
"Robe"           :(4, 2, 2),
"Romper"       :  (4, 2, 2),
"Shirtdress"    : (4, 2, 2),
"Sundress"     :  (4, 2, 2),
"boots":(3, 2, 3) ,
"flip_flops":(3, 2, 3),
"loafers":(3, 3, 2),
"sandals":(3, 2, 2),
"sneakers":(3, 2, 2),
"soccer_shoes":(3,1,2)}

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_main():
    return {
        "routes": [
            {"method": "GET", "path": "/", "summary": "Landing"},
            {"method": "GET", "path": "/status", "summary": "App status"},
        ]
    }

@app.get("/status")
def get_status():
    return {"status": "ok"}

@app.get("/classification_prediction")
def get_classification(path:str):
    image_path = "C:/Users/jtruj/Desktop/IMG/garments/"+path
    print(image_path)
    learn = load_learner('../Model/stage-1_resnet34.pkl')
    prediction = learn.predict(image_path)[0]
    print(prediction)

    category, formality, weather = type_dict[prediction]

    db = "garments"
    sql = f"INSERT INTO garments (user_id, img_path, garment_type, garment_category, formality, weather) VALUES(%s, %s, %s, %s, %s, %s)"
    val = (1, path, prediction, category, formality, weather)
    my_cursor.execute(sql, val )
    print(db_connect.commit())

    return {"status": "ok"}

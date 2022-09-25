# import requirements
import pandas as pd
from typing import Tuple
import os

def load()-> pd.DataFrame:
    """
    Load data and returns dataframe
    """

    list_cloth_path = "../Dataset/DeepFashion_DS/DeepFashion_DS_TextFiles/list_category_cloth.txt"
    list_img_path = "../Dataset/DeepFashion_DS/DeepFashion_DS_TextFiles/list_category_img.txt"

    df_cloth=pd.read_csv(list_cloth_path,skiprows=1,delim_whitespace=True)
    df_img=pd.read_csv(list_img_path,skiprows=1,delim_whitespace=True)

    df_cloth.to_dict()
    category_map = df_cloth
    category_map["value"] = category_map.index + 1

    dict_category = category_map.set_index("value").to_dict()["category_name"]
    dict_cloth = category_map.set_index("category_name").to_dict()["category_type"]

    df = df_img
    df["category_label"] = df["category_label"].map(dict_category)
    df["garment_type"] = df["category_label"].map(dict_cloth)

    df["image_name"] = df["image_name"].str.replace("img/","DeepFashion_DS/DeepFashion_DS_IMG/")

    shoe_df = pd.DataFrame(columns = ['image_name', 'category_label'])

    root = "../Dataset/EdgeNet_Shoe_DS/training/"
    dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]

    for category_name in dirlist:
        route = root + category_name + "/"
        
        directory = os.fsencode(route)

        for file in os.listdir(directory): #for cycle to iterate over folder
            filename = os.fsdecode(file) #get file name
            if filename.endswith(".jpg"): #if ends with .jpg
                shoe_df = shoe_df.append({'image_name' : str("EdgeNet_Shoe_DS/training/"+category_name+"/"+filename), 'category_label' : category_name},ignore_index = True)

    with open('../Dataset/DeepFashion_DS/DeepFashion_DS_TextFiles/train.txt') as f:
        train_list = f.read().splitlines()

    train_list = [row.replace("img/","DeepFashion_DS/DeepFashion_DS_IMG/") for row in train_list]

    cloth_df = df[df["image_name"].isin(train_list)].drop("garment_type",axis=1)

    frames = [cloth_df,shoe_df]

    complete_df = pd.concat(frames)

    return (complete_df)

def garment_mapping()-> pd.DataFrame:
    """
    Realizes mapping and creates a dataframe with all the training image set and parameters per img
    """

    category_dict = {
        "top":      1,
        "bottom":   2, 
        "shoes":    3,
        "onepiece": 4   # ignored in the MVP version
    }

    formality_dict = {
        "formality":3,
        "casual":2, 
        "sport":1
    }

    weather_dict = {
        "cold":3,
        "sunny":2, 
        "rainny":1
    }

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

    inv_category_dict = dict(zip(category_dict.values(), category_dict.keys()))
    inv_formality_dict = dict(zip(formality_dict.values(), formality_dict.keys()))
    inv_weather_dict = dict(zip(weather_dict.values(), weather_dict.keys()))

    type_df = pd.DataFrame(type_dict).T
    type_df.columns = ['Garment_type', 'Formality', 'Weather']

    type_df["Garment_type"]=type_df["Garment_type"].map(inv_category_dict)
    type_df["Formality"]=type_df["Formality"].map(inv_formality_dict)
    type_df["Weather"]=type_df["Weather"].map(inv_weather_dict)

    return(type_df)

def whole_df(complete_df,type_df)-> pd.DataFrame:
    df = pd.DataFrame(columns=["image_name","category_label","garment_type","formality","weather"])
    df["image_name"] = complete_df["image_name"]
    df["category_label"] = complete_df["category_label"]

    return(df)
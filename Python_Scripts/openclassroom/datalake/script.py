import fastavro
import json

# Définition des plats
plat = [
    {
        "nom": "饺子",
        "ingredients": ["chou", "porc", "farine"],
        "origine": "北京",
        "prix": 4,
        "type": "plat"
    },
    {
        "nom": "方便面",
        "ingredients": ["piment", "nouilles"],
        "prix": 1.5,
        "type": "plat"
    },
    {
        "nom": "宫保鸡丁",
        "origine": "四川",
        "ingredients": ["poulet", "cacahuetes"],
        "prix": 8,
        "type": "plat"
    },
    {
        "nom": "米饭",
        "ingredients": ["riz"],
        "prix": 1,
        "type": "accompagnement"
    },
    {
        "nom": "冰水",
        "ingredients": ["riz"],
        "prix": 0.5,
        "type": "accompagnement"
    }
]

# Définition du schéma des données
schema = json.load(open("plat.avsc"))

# Ouverture d'un fichier binaire en mode écriture
with open("plat.avro", 'wb') as avro_file:
    # Ecriture des données
    fastavro.writer(avro_file, schema, plat)

# Test de lecture des données
with open("plat.avro", 'rb') as avro_file:
    reader = fastavro.reader(avro_file)
    #print(reader.schema)
    for plat in reader:
        print(plat)


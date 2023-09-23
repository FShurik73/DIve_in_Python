import csv
import json

def export_csv_to_json(csv_file:str, json_file: str):
    final_dict = {}
    with open(csv_file, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, items in enumerate(data):
        data[i] = data[i].strip().split('|')
        data[i][1] = data[i][1].zfill(10)
        final_dict[hash(data[i][0] + data[i][1])] = data[i]
    with open(json_file, 'w', encoding='UTF-8') as file:
        json.dump(final_dict, file, indent=4, ensure_ascii=False)        

export_csv_to_json('user_db.csv', 'new_user_db.json')        
import csv
import json
import pickle
import os

def read_pickle(path):
    with open(path, 'rb') as pickle_file:
        data = pickle.load(pickle_file)
    return data

data = read_pickle('Homework 8/u.pickle')


def create_csv_table(data_csv: dict):
    csv_headers = list(data_csv.keys())
    csv_table = list(data_csv.values())
    csv_table = list(zip(*csv_table))
    with open('example.csv', 'w', encoding='UTF-8') as file:
        csv_writer = csv.writer(file, dialect = 'excel', delimiter=',' )
        csv_writer.writerow(csv_headers)
        csv_writer.writerows(csv_table)


create_csv_table(data)


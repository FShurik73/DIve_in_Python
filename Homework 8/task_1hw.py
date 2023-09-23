# 📌 Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.

import csv
import pickle

def convert_csv(csv_file, filename):
    with (open(filename, 'bw') as file_pickle,
          open(csv_file, "r", newline='', encoding='utf-8', ) as csv_w,
          ):
        list_csv = []
        read = csv.reader(csv_w)
        for item in read:
            list_csv.append(item)
        pickle.dump(list_csv, file_pickle)
    with open(filename, 'br') as file_pickle:
        print(*file_pickle)


if __name__ == '__main__':
    convert_csv("example.csv", "example_csv.pickle")











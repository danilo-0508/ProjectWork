import csv
import numpy as np
with open("categories.csv", encoding= "utf-8") as f:
    lett = csv.reader(f)
    header = next(lett)
    colonna_1 = []
    colonna_2= []
    for elem in lett:
        colonna_1.append(int(elem[0]))
        colonna_2.append(elem[1])
        with open("../Progetto/categories_pulito.csv", "w", encoding="utf-8", newline="") as f1:
            scritt = csv.writer(f1)
            scritt.writerow(header)  # Scrivi l'intestazione
            for i in range(len(colonna_1)):
                scritt.writerow([colonna_1[i], colonna_2[i]])

            # print(type(colonna_1[0]))
            # print(type(colonna_2[0]))

with open("podcast.csv", encoding= "utf-8") as f:
    lett = csv.reader(f)
    header = next(lett)
    colonna_1 = []
    colonna_2= []
    colonna_3= []
    for elem in lett:
        print(elem[2])
        if elem[2] != "":
            colonna_1.append(int(elem[2]))
        elif elem[2] == "":
            colonna_1.append(26)
        colonna_2.append(elem[0])
        colonna_3.append(elem[1])
with open("../Progetto/podcast_pulito.csv", "w", encoding="utf-8", newline="") as f1:
    scritt = csv.writer(f1)
    scritt.writerow(header)  # Scrivener l'intestazione
    for i in range(len(colonna_1)):
        scritt.writerow([colonna_2[i], colonna_3[i], colonna_1[i]])
print(colonna_1)




#
# import pandas as pd
#
# df = pd.read_csv("categories.csv")
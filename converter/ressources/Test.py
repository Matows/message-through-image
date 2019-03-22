import csv

with open("valeurs_RGB.csv","r") as file:
    # for i in range(0,len(file.readlines())):
    #     vals_RGB = file.readlines()
    #     print(i , " => ")
    #     print(vals_RGB)
    lecteur_csv = csv.reader(file,delimiter=",")
    for line in lecteur_csv:
        print(line)

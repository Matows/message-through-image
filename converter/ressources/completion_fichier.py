with open("valeurs_RGB.csv","w") as file:
    for i in range (0,84):
        varToWrite = str(i) + "," + '\n'
        file.write(varToWrite)

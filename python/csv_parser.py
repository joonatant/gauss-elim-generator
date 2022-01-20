import pandas as pd
import re
import math

#toimii str-inputeille muotoa 'n' ja 'n/m', joissa n ja m ovat kokonaislukuja
def str_to_tuple(entry):
    entry = str(entry)
    if ("/" in entry):
        temp = entry.split("/")
        if (not len(temp)==2):
            raise Exception("Wrong type of input.")
        else:
            return (int(temp[0]), int(temp[1]))
    else:
        return (int(entry), 1)

def csv_to_matrix(fileName="gauss.csv"):
    df = pd.read_csv(fileName, header=None)
    data = df.values.tolist()
    allowed = "-0123456789/"
    for n in range(0, len(data)):
        for m in range(0, len(data[n])):
            """print(data[n][m])
            temp = re.sub("[^0-9\/\-]", '', str(data[n][m]))
            temp = data[n][m]
            print(temp)"""
            temp=""
            #print(data[n][m])
            for l in range(0, len(str(data[n][m]))):
                k = str(data[n][m])[l]
                if(k in allowed):
                    temp = temp + k
            data[n][m] = str_to_tuple(temp)

    return data
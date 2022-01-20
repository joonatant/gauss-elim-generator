import csv
import re

#toimii str-inputeille muotoa 'n' ja 'n/m', joissa n ja m ovat kokonaislukuja
def str_to_tuple(entry):
    if ("/" in entry):
        temp = entry.split("/")
        if (not len(temp)==2):
            raise Exception("Wrong type of input.")
        else:
            return (int(temp[0]), int(temp[1]))
    else:
        return int(entry)

def csv_to_matrix(fileName="gauss.csv"):
    with open(fileName, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    #muutetaan kaikki data haluttuu taulukko-tuple -muotoon

    for n in range(0, len(data)):
        for m in range(0, len(data[n])):
            temp = re.sub("[^0-9/]", '', data[n][m])
            data[n][m] = str_to_tuple(data[n][m])
import numpy as np
import pandas as pd

from sklearn import datasets, linear_model
import time
from tqdm import tqdm

def pridict_last(N, inputfilepath):

    data = pd.read_csv(inputfilepath)
    clf = linear_model.LinearRegression()
    results = []
    Ids = []


    for i in tqdm(range(len(data))):
        Id =  data["Id"][i]
        seq = np.fromstring(data['Sequence'][i], dtype=int, sep=",")
        number_of_points = N

        if 3 < len(seq) < number_of_points + 4:
            number_of_points = len(seq) - 3

        if len(seq) < 4:
            Ids.append(Id)
            results.append(seq[-1])
            continue

        clf.fit([seq[i:i + number_of_points]
                 for i in range(len(seq) - number_of_points)], seq[number_of_points:])

        result = clf.predict([seq[-number_of_points:]])[0]
        results.append(int(round(result)))
        Ids.append(Id)

    import csv
    df = pd.DataFrame({'"Id"':Ids,"\"Last\"":results})
    df.to_csv('new1.csv', index=False, quoting=csv.QUOTE_NONE)


def test_pridiction(inputfilepath):

    clf = linear_model.LinearRegression()
    data = pd.read_csv(inputfilepath)

    for N in range(6,20):
        corrects = 0
        issues = 0
        issues_5 = 0
        print("number_of_points = ", N)
        for i in tqdm(range(len(data))):
            train = np.fromstring(data['Sequence'][i], dtype=int, sep=",")
            number_of_points = N

            if 3< len(train) < number_of_points + 4:
                issues += 1
                number_of_points = len(train) - 2

            if len(train) < 4:
                issues_5 += 1
                continue

            last_integer = train[-1]
            seq = train[:-1]
            X = [seq[i:i + number_of_points]
                     for i in range(len(seq) - number_of_points)]

            Y = seq[number_of_points:]

            clf.fit(X, Y)

            results = clf.predict( [seq[-number_of_points:] ] )[0]
            score = clf.score([seq[i:i + number_of_points]
                               for i in range(len(seq) - number_of_points)], seq[number_of_points:])
            if int(round(results)) == last_integer:
                corrects += 1

        print("Number of issues = ", issues)
        print("length < 5 = ", issues_5)
        print("Percentage = ", corrects / len(data), "\n")

def main():

    start = time.time()
    pridict_last(12,'C:\\Users\\SID\\Desktop\\Python Codes\\Sequence\\test.csv')
    print('\nCSV Written\n')
    test_pridiction('C:\\Users\\SID\\Desktop\\Python Codes\\Sequence\\test.csv')


    end = time.time()
    print("time = {} s".format(end - start) )


if __name__ == "__main__":
    main()

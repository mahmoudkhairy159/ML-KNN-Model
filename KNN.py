import sys
import math

import pandas as pd
import scipy
import numpy
import matplotlib
import pandas
import sklearn
import matplotlib.pyplot as plt

names = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'y_train']
# trainDatafile
df1 = pd.read_csv("TrainData.txt", names=names)
X = df1.drop("y_train", axis="columns")
Y = df1["y_train"]


def euclidean_distance(r1, r2):
    distance = 0.0
    for i in range(0, len(r1)):
        distance += (r1[i] - r2[i]) ** 2
    return math.sqrt(distance)


def calc_neighbors(k, row0):
    # calc all distances between specific row and the data
    neighbors = []
    original_dis_list = []
    sorted_list = []  # sorted list
    for i in range(0, len(X)):
        row = X.iloc[i]
        dis = euclidean_distance(row0, row)
        original_dis_list.append(dis)
        sorted_list.append(dis)
    # print(dis)
    # print(original_dis_list)
    sorted_list.sort()
    # print(sorted_list)
    for i in range(0, k):
        neighbors.append(original_dis_list.index(sorted_list[i]))  # get rows  (neighbors) index in data
    # print(neighbors)
    return neighbors


def predict_y(k, row0):  # row0 is the tested record
    # predict
    neighbors = calc_neighbors(k, row0)
    y_training_neighbors = []
    for i in range(0, k):
        y_training_neighbors.append(Y.iloc[neighbors[i]])  # label values of neighbors
    # print(y_training_neighbors)
    myset = set(y_training_neighbors)  # to get unrepeated values in neighbors to i can use them to calc_majjority
    # print(myset)
    neighborsClasses = list(myset)
    list_majority = []
    for i in range(0, len(myset)):
        list_majority.append(y_training_neighbors.count(neighborsClasses[i]))  # calc_count of each class of neighbors
    # print(list_majority)
    # print(neighborsClasses)
    ## tie:
    first_occurance=[]
    Y_Train_list=list(Y)
    if (len(set(list_majority)) == 1):
        for i in range (0, len(neighborsClasses)):
            first_occurance.append(Y_Train_list.index(neighborsClasses[i]))
        index= first_occurance.index(min(first_occurance))
        y_pridected = neighborsClasses[index]
    else:
        index = list_majority.index(max(list_majority))  # index of bigger class
        # print(index)
        y_pridected = neighborsClasses[index]
        # print(y_pridected)
    return y_pridected


def main():
    # rint(X.iloc[0])
    ##
    # testing_data
    df2 = pd.read_csv("TestData.txt", names=names)
    X1 = df2.drop("y_train", axis="columns")
    Y1 = df2["y_train"]  # actual_class_label

    #row0 = X1.iloc[0]
    # k = 5
    # neighbors =calc_neighbors(k,row0)
    # predict_y(k, row0)
    # print(Y1.iloc[0])
    totalNumOfInstsnces = 445
    for k in range(1, 10):
        Accuracy = 0
        totalNumOfCorrect = 0
        print("K value :", k, "\n")
        for i in range(0, len(X1)):
            y_predicted = predict_y(k, X1.iloc[i])
            print("Row", i, "::", "predicted class : ", y_predicted, "\t", "actual class : ", Y1.iloc[i])
            if y_predicted == Y1.iloc[i]:
                totalNumOfCorrect += 1
        print("totalNumOfCorrect :", totalNumOfCorrect, "totalNumOfInstsnces", totalNumOfInstsnces)
        Accuracy = (totalNumOfCorrect / totalNumOfInstsnces) * 100  # *100 for percentage
        print("Accuracy is : ", Accuracy, " %")
        print("___________________________________________________________________________________________")


if __name__ == "__main__": main()

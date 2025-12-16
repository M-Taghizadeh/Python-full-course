"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


import math
import random

# START OF FUNCTION
def show_dataSet(dataSet):
    for i in range (0, len(dataSet)):
        print(dataSet[i][0] ,"\t" , dataSet[i][1])
    print("Number of Data Set : ", len(dataSet))

def show_testSet(testSet):
    for i in range(0, len(testSet)):
        print(testSet[i])
    print("number of Test Set : ", len(testSet))

def read_excel_files(loc):
    import xlrd 
    file = xlrd.open_workbook(loc) 
    sheet = file.sheet_by_index(0)
    return sheet


def get_std(class_list, avg):
    sum = 0
    for i in range(0, len(class_list)):
        sum += math.pow((float(class_list[i]) - float(avg)), 2)
    variance = sum/len(class_list)
    std = math.sqrt(variance)
    print("std : ", std)
    return std

def get_avg(class_list):
    sum = 0
    for i in range (0, len(class_list)):
        sum += float(class_list[i])
    avg = sum/len(class_list)
    print("avg : ", avg)
    return avg
    
    
def p_x_w(x, class_list):
    avg = get_avg(class_list)
    std = get_std(class_list, avg)
    p = (1/(math.sqrt(2*math.pi) * std)) * math.pow(math.e, (-1/2) * ( math.pow( ((x - avg)/std) , 2)))
    return p
    
# END OF FUNCTION

sheet = read_excel_files("C:/Users/Zanis/Desktop/AI Docs/AI01/BayesClassifier/DataSet.xlsx")
dataSet = []
for i in range(0, sheet.nrows):
    tmp_list = [sheet.cell_value(i, 0), sheet.cell_value(i, 1)]
    dataSet.append(tmp_list)
    
show_dataSet(dataSet)


class1 = [] # for 0
class2 = [] # for 1
for i in range (0, len(dataSet)):
    if(dataSet[i][1]==0):
        class1.append(dataSet[i][0])
    elif(dataSet[i][1]==1):
        class2.append(dataSet[i][0])

c1 = len(class1)/len(dataSet)
c2 = len(class2)/len(dataSet)
print("\nc1 : ", c1, " , c2 : ", c2)


# =============================================================================
# x = float(input('Enter IQ : '))
# p_x_w1 = p_x_w(x, class1) * c1
# print("p(w1|x) : ", p_x_w1)
# p_x_w2 = p_x_w(x, class2) * c2
# print("p(w2|x) : ", p_x_w2)
# 
# if(p_x_w1>p_x_w2):
#     print('0 -----> class 1 : not success!')
# elif(p_x_w2>p_x_w1):
#     print('1 -----> class 2 : success!')
# else:
#     print('0 or 1 is possible!')
# =============================================================================

    


# Test Set :
sheet_test = read_excel_files("C:/Users/Zanis/Desktop/AI Docs/AI01/BayesClassifier/DataSet.xlsx")
testSet = []
Label = []
for i in range(0, sheet_test.nrows):
    tmp_list1 = sheet_test.cell_value(i, 0)
    tmp_list2 = sheet_test.cell_value(i, 1)
    testSet.append(tmp_list1)
    Label.append(tmp_list2)
show_testSet(testSet)


Guess = []
for i in range (0, len(testSet)):
    input_test = testSet[i]
    p_x_w1 = p_x_w(input_test, class1) * c1
    p_x_w2 = p_x_w(input_test, class2) * c2
    
    if(p_x_w1>p_x_w2):
        Guess.append(0)
    elif(p_x_w2>p_x_w1):
        Guess.append(1)
    else:
        Guess.append(random.randint(0, 1))

# Calculation of Accuracy : 
sum_accuracy = 0
for i in range(0, len(testSet)):
    print("for IQ = ",testSet[i], " Guess : ", Guess[i], " ---> Label : ", Label[i])    
    if Guess[i] == Label[i]:
        sum_accuracy += 1

print("Accuracy of Baeys Classifier on Test Set is : ", sum_accuracy/len(testSet)*100, "%")
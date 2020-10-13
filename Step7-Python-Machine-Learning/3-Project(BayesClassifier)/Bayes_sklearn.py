from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import numpy as np 

def read_excel_files(loc):
    import xlrd 
    file = xlrd.open_workbook(loc) 
    sheet = file.sheet_by_index(0)
    return sheet

# DataSet 
sheet = read_excel_files("C:/Users/Zanis/Desktop/AI Docs/AI01/BayesClassifier/DataSet.xlsx")
dataSet = []
for i in range(0, sheet.nrows):
    tmp_list = [sheet.cell_value(i, 0), sheet.cell_value(i, 1)]
    dataSet.append(tmp_list)
x = []
y = []
for i in range (0, len(dataSet)):
    x.append(dataSet[i][0])
    y.append(dataSet[i][1])
X_train = np.array(x).reshape(-1, 1)  
Y_train = np.array(y).reshape(-1, 1)  

# Test Set
sheet = read_excel_files("C:/Users/Zanis/Desktop/AI Docs/AI01/BayesClassifier/TestSet.xlsx")
testSet = []
for i in range(0, sheet.nrows):
    tmp_list = [sheet.cell_value(i, 0), sheet.cell_value(i, 1)]
    testSet.append(tmp_list)
x = []
y = []
for i in range (0, len(testSet)):
    x.append(testSet[i][0])
    y.append(testSet[i][1])
X_test = np.array(x).reshape(-1, 1)  
Y_test = np.array(y).reshape(-1, 1) 

# Create Bayes Model
gnb = GaussianNB()
gnb.fit(X_train, Y_train.ravel())
y_pred = gnb.predict(X_test)
print(x, "\n", y_pred)
print("Accuracy:",metrics.accuracy_score(Y_test, y_pred))
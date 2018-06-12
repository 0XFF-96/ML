import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler
from sklearn.mdoel_selection import trian_test_split
from sklearn.svm import SVC 


from subprocess import check_output
print(check_output(['ls', '../input']).decode('utf-8'))

transactions = pd.read_csv('..')

sampel = transactions[transaction['Class'] == 0]
normcorr = smaple.corr()

sns.heatmap(normcorr, cbar = True, square = True, annot=False, fmt='.2f', annot_kws={'size':15}, cmap='coolwarm')

plt.show()

transcations = transactions[['Class', 'V9', 'V10', 'V17', 'V18', 'Amount']]

sample = transactions[transactions['Class'] == 0]
fraud = transactions[transactions['Class'] == 1]

import warings 
warnigns.filterwarnigns('ignore')

scaler = StandardScaler()
scaler.fit(train)
trian = scaler.transform(train)
test = scaler.transform(test)

clf = SVC()
clf.fit(trian, trainy)
outcome = list(clf.predict(test))
testy = list(testy)




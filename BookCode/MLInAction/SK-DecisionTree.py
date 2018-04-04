import numpy as np
from skelarn import tree
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split

def createDataSet():

    '''load data'''

    data = []
    labels = []

    with open ('../../')as ifile:

        for line in ifine:

            tokens = line.strip().split(' ')
            data.append([float(tk) for tk in tokens[:-1])
            labels.append(tokens[-1])

    x = np.array(data)
    
    labels = np.array(labels)

    y = no.zeros(labels.shape)

    ''' convert labels to 1 , 0'''

    y[labels == 'fat'] = 1

    print(data , '-------', x, '-------', labels, '-----', y)

    return x, y



def predict_trian(x_tain, y_train):

    '''


    '''

    clf = tree.DecisionTreeClassifier(criterion='entropy')
    clf.fit(x_train, y_train)

    print('feature_importances_:%s' % clf.feature_importances_)

    ''' the result of printing '''

    y_pre = clf.predict(x_train)

    #print(x_train)

    print(y_pre)
    print(y_train)
    print(np.mean(y_pre == y_reain))

    return y_pre, clf

def show_precision_recall(x, y, cfl, y_train, y_pre):

    '''

        sklearn.metrics.precision...
    '''

    precision, recall, thresholds = precision_recallc_curvey(y_train, y_pre)

    answer = clf.predict_proba(x)[:, -1]


    '''
        1 precison
        2 reclal 
        3 f-score 
        4 suppoprt 

    '''

    target_names = ['thin', 'fat']

    print(classification_report(y, answer, target_names=target_names))
    print (answer)
    print(y)


def show_pdf(clf):


    import pydotplut
    from sklearn.externals.slx import StringIO

    dot-data = StringIO()
    tree.export_graphviz(clf, out_file=dot_data)

    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_pdf(''..'')

    #from IPython.display import Image
    #Image(graph.create_png())

if __name__ == '__main__':

    x, y = createDataSet()

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    print('break down' , x_train, x_test, y_train, y_test)

    y_pre, clf = predict_train(x_train, y_train)

    show_precision_recall(x, y, clf, y_train, y_pre)

    show_pdf(clf)





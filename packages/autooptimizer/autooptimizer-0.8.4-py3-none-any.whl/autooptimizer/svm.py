from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import warnings
warnings.simplefilter("ignore")

def svc(x, y, scoring='roc_auc_ovo'):
    xtrain ,xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, random_state=4, shuffle=True)
    ss = StandardScaler()
    xtrain = ss.fit_transform(xtrain)
    xtest = ss.fit_transform(xtest)
    parameters={'kernel':['rbf','sigmoid','poly','linear'],
                'C':[np.arange(1,20,1),50,75,100,150,200,250,300,500,600,700,750,800,900,1e5],
                'degree':np.arange(0,20,0.5),
                'gamma':['scale','auto',np.arange(0.1,1,0.1), np.arange(1,10,1), np.arange(10,100,10)],
               'random_state':[4,12,20,22,40,42]}
    main_model = SVC(probability=True)
    scv_model = RandomizedSearchCV(main_model, parameters, scoring=scoring, cv=5)
    best_params = np.array([])
    best_score = np.array([])
    for cv in range(2, 20):
        scv_model.fit(xtrain,ytrain)
        if scv_model.best_score_ != 1.:
            best_params = np.append(best_params, scv_model.best_params_)
            best_score = np.append(best_score, scv_model.best_score_)
    best_index = np.argmax(best_score)
    print('The best possible accuracy in terms of {0} metric is {1}%'.format(scoring, round(best_score[best_index] * 100, 2)))
    hyperparameter =  best_params[best_index]
    return SVC(kernel=hyperparameter['kernel'], C=hyperparameter['C'], 
               degree=hyperparameter['degree'], gamma=hyperparameter['gamma'],
              random_state=hyperparameter['random_state'])
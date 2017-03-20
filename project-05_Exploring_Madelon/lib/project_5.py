import itertools
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split



def load_data_from_database():
    engine = create_engine('postgresql://dsi:correct horse battery staple@joshuacook.me:5432')
    madelon_df = pd.read_sql_table('madelon', con=engine, index_col='index')
    return madelon_df


def add_to_or_create_process_list(process, data_dict):
    if 'processes' in data_dict.keys():
        data_dict['processes'].append(process)
    else:
        data_dict['processes'] = [process]
        
    return data_dict


def make_data_dict(X, y, random_state=None):
    """
    splits into train/test, 
    returns data dictionary
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state)
    
    data_dict = {'X' : X,
                 'y' : y,
                 'X_train': X_train,
                 'X_test' : X_test,
                 'y_train': y_train,
                 'y_test' : y_test}
    
    return data_dict


def general_transformer(transformer, data_dict, random_state=None):
    """
    fits data dictionary to transformer,
    returns transformer and train/test
    """
    transformer.fit(data_dict['X_train'], data_dict['y_train'])
    
    data_dict['X_train'] = transformer.transform(data_dict['X_train'])
    data_dict['X_test'] = transformer.transform(data_dict['X_test'])
    data_dict['transformer'] = transformer
    
    add_to_or_create_process_list(transformer, data_dict)
    
    return data_dict


def general_model(model, data_dict, random_state=None):
    """
    fits data dictionary to model,
    returns model and train/test score
    """
    temp = model.fit(data_dict['X_train'], data_dict['y_train'])
    test_score = temp.score(data_dict['X_test'], data_dict['y_test'])
    train_score = temp.score(data_dict['X_train'], data_dict['y_train'])
    
    data_dict['scores'] = [("train score:", train_score), ("test score:", test_score)]
    data_dict['prediction'] = temp.predict(data_dict['X_test'])
    data_dict['train_score'] = train_score
    data_dict['test_score'] = test_score
    data_dict['model'] = model
    
    add_to_or_create_process_list(model, data_dict)
    
    return data_dict
    
    
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="black" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
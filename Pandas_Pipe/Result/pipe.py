import pandas as pd
from functools import wraps
import logging
import datetime as dt

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def log_msg(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = dt.datetime.now()
        result = func(*args, **kwargs)
        time_taken = str(dt.datetime.now() - start)
        logging.info(f"{func.__name__} took {time_taken}s and the size turned into {result.shape}.")
        return result
    return wrapper

@log_msg
def copying(data):
    return data.copy()

@log_msg
def dropping(data):
    return data.drop([0])

@log_msg
def new_data_types(data):
    data[['calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins', 'shelf', 'weight', 'cups']] = data[['calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins', 'shelf', 'weight', 'cups']].apply(pd.to_numeric)
    return data   

@log_msg
def mfr_group(data):
    gdata = data.groupby(['mfr'])
    return data['mfr'].value_counts()

@log_msg                     
def removing_low_mfr(data, min_products = 10):
    mfr_no_products = (data
                 .groupby('mfr')
                 .agg(n=('name', 'count'))
                 .loc[lambda d: d['n'] >= min_products]
                 .index)
    return (data
            .loc[lambda d: d['mfr'].isin(mfr_no_products)])

@log_msg                    
def indexing(data):
    return data.set_index(['type', 'mfr', 'name']).sort_index()

@log_msg                    
def nutrition_sieve(data, min_protein = 2, max_fat=2, max_sugars=7):
    mask = (data['protein'] >=min_protein) & (data['fat'] <= max_fat) & (data['sugars'] <= max_sugars)
    return data[mask]

@log_msg                    
def sorting(data):
    data1 = data.sort_values(['rating'], ascending=False)
    return data1.sort_values(['calories'])
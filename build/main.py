import csvparser
import numpy as np
import pandas as pd
import time

def timer(my_function):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = my_function(*args, **kwargs)
        t2 = time.time()
        print(f"{my_function.__name__} ran in {t2 - t1:.3f} sec")
        return result
    return wrapper


class CSVParserpy:
    def __init__(self, input_file):  
        # Create an instance of CSVParser
        self.c = csvparser.CSVParser(input_file)   
        self.c.read()
        self.dataset = pd.read_csv(input_file)

    @timer
    def mean_col(self, col):
        # Use the CSVParser instance to compute the mean
        return self.c.mean_col(col)
    
    @timer
    def mean_col_np(self, col):
        # Compute the mean using numpy   
        return np.mean(self.dataset.iloc[:, col]) 
    

df = CSVParserpy("../csv_examples/house.csv")
print(df.mean_col(1))
print(df.mean_col_py(1))

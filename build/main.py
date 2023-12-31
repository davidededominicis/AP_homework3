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
    
    @timer 
    def var_col(self, col):
        # Use the CSVParser instance to compute the variance
        return self.c.var_col(col)
    @timer 
    def var_col_np(self, col):
        return np.var(self.dataset.iloc[:, col])
    
    @timer
    def median_col(self, col):
        # Use the CSVParser instance to compute the median
        return self.c.median_col(col)
    @timer
    def median_col_np(self, col):
        return np.median(self.dataset.iloc[:, col])
    
    @timer
    def std_dev(self, col):
        # Use the CSVParser instance to compute the standard deviation
        return self.c.std_dev(col)
    @timer
    def std_dev_np(self, col):
        return np.std(self.dataset.iloc[:, col])
    
    @timer
    def correlation_analysis(self, col1, col2):
        # Use the CSVParser instance to compute the correlation
        return self.c.correlation_analysis(col1, col2)
    @timer
    def correlation_analysis_np(self, col1, col2):
        return np.corrcoef(self.dataset.iloc[:, col1], self.dataset.iloc[:, col2])
    
    @timer
    def countFrequency(self, col):
        # Use the CSVParser instance to compute the count frequency
        return self.c.countFrequency(col)
    @timer  
    def countFrequency_np(self, col):
        u, indices=np.unique(self.dataset.iloc[:, col], return_counts=True)
        #map comprehension to create a dictionary
        return {k:v for k,v in zip(u, indices)}
    
    @timer
    def summary(self, filename):
        # Use the CSVParser instance to compute the summary
        return self.c.summary(filename)
    @timer
    def summary_np(self, filename):
        with open('filename.txt', 'w') as file:

            for i, colname in enumerate(self.dataset.columns):
                file.write(f'Column {colname}:\n')
                file.write('-------------------------------------------------------------\n\n')
                file.write(f'Mean = {np.mean(self.dataset[colname])}\n')  
                file.write(f'Median = {np.median(self.dataset[colname])}\n')
                file.write(f'Standard Deviation = {np.std(self.dataset[colname])}\n')
                file.write(f'Variance = {np.var(self.dataset[colname])}\n')


        return 
    



#-------------------------------TEST-----------------------------------    
df = CSVParserpy("../csv_examples/house.csv")
print(df.mean_col(1))
print(df.mean_col_np(1))
#df.countFrequency(1)
print(df.countFrequency_np(1))
df.summary("test")
df.summary_np("testnp")

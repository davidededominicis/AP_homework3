import sys
sys.path.append('../build')
import csvparser 
import numpy as np
import pandas as pd
import time
import os
import matplotlib.pyplot as plt

if not os.path.exists("./plots_csv"):
    os.mkdir("./plots_csv")
if not os.path.exists("./solutions_csv"):
    os.mkdir("./solutions_csv")

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
        '''
        Use the CSVParser instance to compute the mean
        Parameters: col: index of column
        Return: the mean of the column
        '''
        return self.c.mean_col(col)
    
    @timer
    def mean_col_np(self, col):
        '''
        Compute the mean using numpy
        Parameters: col: index of column
        Return: the mean of the column
        ''' 
        return np.mean(self.dataset.iloc[:, col]) 
    
    @timer 
    def var_col(self, col):
        '''
        Use the CSVParser instance to compute the variance
        Parameters: col: index of column
        Return: the variance of the column
        '''
        return self.c.var_col(col)
    @timer 
    def var_col_np(self, col):
        '''
        Compute the variance using numpy
        Parameters: col: index of column
        Return: the variance of the column
        '''
        return np.var(self.dataset.iloc[:, col])
    
    @timer
    def median_col(self, col):
        '''
        Use the CSVParser instance to compute the median
        Parameters: col: index of column
        Return: the median of the column
        '''
        return self.c.median_col(col)
    @timer
    def median_col_np(self, col):
        ''' 
        Compute the median using numpy
        Parameters: col: index of column
        Return: the median of the column
        '''
        return np.median(self.dataset.iloc[:, col])
    
    @timer
    def std_dev(self, col):
        '''
        Use the CSVParser instance to compute the standard deviation
        Parameters: col: index of column
        Return: the standard deviation of the column
        '''
        return self.c.std_dev(col)
    
    @timer
    def std_dev_np(self, col):
        '''
        Compute the standard deviation using numpy
        Parameters: col: index of column
        Return: the standard deviation of the column
        '''
        return np.std(self.dataset.iloc[:, col])
    
    @timer
    def correlation_analysis(self, col1, col2):
        '''
        Use the CSVParser instance to compute the correlation
        Parameters: col1: index of column
                    col2: index of column
        Return: the correlation between the two columns
        '''
        try:
            data_col1 = pd.to_numeric(self.dataset.iloc[:, col1], errors='raise')
            data_col2 = pd.to_numeric(self.dataset.iloc[:, col2], errors='raise')
            correlation = data_col1.corr(data_col2)
            return correlation
        except Exception as e:
            print(f"correlation_analysis Error: {e}. One of the columns is not numeric")
            return None
    
    @timer
    def correlation_analysis_np(self, col1, col2):
        '''
        Compute the correlation using numpy
        Parameters: col1: index of column
                    col2: index of column
        Return: the correlation between the two columns
        '''
        try:
            data_col1 = pd.to_numeric(self.dataset.iloc[:, col1], errors='raise')
            data_col2 = pd.to_numeric(self.dataset.iloc[:, col2], errors='raise')
            return np.corrcoef(data_col1, data_col2)[0, 1]
        except Exception as e:
            print(f"correlation_analysis Error: {e}. One of the columns is not numeric")
            return None

    
    @timer
    def countFrequency(self, col):
        '''
        Use the CSVParser instance to compute the count frequency
        Parameters: col: index of column
        Return: the count frequency of the column
        '''
        return self.c.countFrequency(col)
    
    @timer  
    def countFrequency_np(self, col):
        '''
        Compute the count frequency using numpy
        Parameters: col: index of column
        Return: the count frequency of the column
        '''
        u, indices=np.unique(self.dataset.iloc[:, col], return_counts=True) 
        #map comprehension to create a dictionary
        return {k:v for k,v in zip(u, indices)}
    
    @timer
    def summary(self, filename):
        '''
        Use the CSVParser instance to compute the summary
        Parameters: filename: name of the file where to write the summary
        '''
        return self.c.summary(filename)
    
    @timer
    def summary_np(self, filename):
        '''
        Compute the summary using numpy
        Parameters: filename: name of the file where to write the summary
        '''
        with open(filename, 'w') as file:
            for colname in self.dataset.columns:
                file.write('-------------------------------------------------------------\n\n')
                file.write(f'Column: {colname}\n')
                file.write('-------------------------------------------------------------\n\n')
                
                if self.dataset[colname].dtype.kind not in 'iufc':  # Check if the column is numeric
                    file.write('Non numeric column\n\n')
                    continue  

                # Compute statistics if the column is numeric
                file.write(f'Mean = {self.mean_col_np(self.dataset.columns.get_loc(colname))}\n')  
                file.write(f'Median = {self.median_col_np(self.dataset.columns.get_loc(colname))}\n')
                file.write(f'Standard Deviation = {self.std_dev_np(self.dataset.columns.get_loc(colname))}\n')
                file.write(f'Variance = {self.var_col_np(self.dataset.columns.get_loc(colname))}\n')
                #write the count frequency done with countfrequency_np in the file
                frequency = self.countFrequency_np(self.dataset.columns.get_loc(colname))
                for k, v in frequency.items():
                    file.write(f' Element: {k} Frequency: {v}\n')
                

        print(f'Summary written to {filename}')

    def classification(self, wanted, col, filename):
        '''
        Use the CSVParser instance to classify the column
        Parameters: wanted: the value to classify
                    col: index of column
                    filename: name of the file where to write the classification
        Return: The classification of the column.
        '''
        return self.c.classification(wanted, col, filename)

    def plot_histogram(self, col_idx, filenamepng=None):
        '''
        Plot the histogram of the column
        Parameters: col_idx: index of column
        '''
        column_name = self.dataset.columns[col_idx]
        plt.figure(figsize=(8, 6))
        plt.hist(self.dataset.iloc[:, col_idx].dropna(), bins=20, edgecolor='black')
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.title('Histogram of ' + column_name)
        if filenamepng:
            plt.savefig(filenamepng)
            print(f"Plot saved as {filenamepng}")
        else:
            plt.show()

    def scatter_plot(self, col_idx1, col_idx2, filenamepng=None):
        '''
        Plot the scatter plot between two columns
        Parameters: col_idx1: index of column
                    col_idx2: index of column
        '''
        column_name1 = self.dataset.columns[col_idx1]
        column_name2 = self.dataset.columns[col_idx2]
        plt.figure(figsize=(8, 6))
        plt.scatter(self.dataset.iloc[:, col_idx1], self.dataset.iloc[:, col_idx2])
        plt.xlabel(column_name1)
        plt.ylabel(column_name2)
        plt.title('Scatter Plot between ' + column_name1 + ' and ' + column_name2)
        if filenamepng:
            plt.savefig(filenamepng)
            print(f"Plot saved as {filenamepng}")
        else:
            plt.show()


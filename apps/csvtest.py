import sys
sys.path.append('../build')
import csvparser 
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

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
        with open(filename, 'w') as file:
            for colname in self.dataset.columns:
                file.write('-------------------------------------------------------------\n\n')
                file.write(f'Column: {colname}\n')
                file.write('-------------------------------------------------------------\n\n')
                
                if self.dataset[colname].dtype.kind not in 'iufc':  # Check se la colonna non è numerica
                    file.write('Non numeric column\n\n')
                    continue  # Passa alla prossima colonna

                # Calcola statistiche solo se la colonna è numerica
                file.write(f'Mean = {self.mean_col_np(self.dataset.columns.get_loc(colname))}\n')  
                file.write(f'Median = {self.median_col_np(self.dataset.columns.get_loc(colname))}\n')
                file.write(f'Standard Deviation = {self.std_dev_np(self.dataset.columns.get_loc(colname))}\n')
                file.write(f'Variance = {self.var_col_np(self.dataset.columns.get_loc(colname))}\n')
                #write the count frequency done with countfrequency_np in the file
                # Calculate frequency once and reuse the result
                frequency = self.countFrequency_np(self.dataset.columns.get_loc(colname))
                for k, v in frequency.items():
                    file.write(f' Element: {k} Frequency: {v}\n')
                #file.write(f' Element: {frequency.keys()} Frequency: {frequency.values()}\n')

        print(f'Summary written to {filename}')

    
    def plot_histogram(self, col_idx):
        column_name = self.dataset.columns[col_idx]
        plt.figure(figsize=(8, 6))
        plt.hist(self.dataset.iloc[:, col_idx].dropna(), bins=20, edgecolor='black')
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.title('Histogram of ' + column_name)
        plt.show()

    def scatter_plot(self, col_idx1, col_idx2):
        column_name1 = self.dataset.columns[col_idx1]
        column_name2 = self.dataset.columns[col_idx2]
        plt.figure(figsize=(8, 6))
        plt.scatter(self.dataset.iloc[:, col_idx1], self.dataset.iloc[:, col_idx2])
        plt.xlabel(column_name1)
        plt.ylabel(column_name2)
        plt.title('Scatter Plot between ' + column_name1 + ' and ' + column_name2)
        plt.show()


#-------------------------------TEST-----------------------------------    
df = CSVParserpy("../csv_examples/Iris.csv")
print(df.mean_col(1))
print(df.mean_col_np(1))
#df.countFrequency(1)
#print(df.countFrequency_np(1))
df.summary("test")
df.summary_np("testnp")
#df.plot_histogram(1)  # Plot dell'istogramma della colonna 1
#df.scatter_plot(1, 2)  # Plot del diagramma a dispersione tra colonna 1 e 2

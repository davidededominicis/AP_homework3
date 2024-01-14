import csvparserpy
import time


# Create an instance of CSVParserpy
df = csvparserpy.CSVParserpy("../csv_examples/house.csv")
# compute and print the mean of the column 2 with both methods
print(f"Mean: {df.mean_col(2)}")

t1 = time.time()
sol=df.mean_col_np(2)
t2 = time.time()
print(f"mean_col_np ran in {t2 - t1:.3f} sec")
print(f"Mean with numpy: {sol} \n")

# compute and print the variance of the column 2 with both methods
print(f"Variance: {df.var_col(2)}")

t1 = time.time()
sol=df.var_col_np(2)
t2 = time.time()
print(f"var_col_np ran in {t2 - t1:.3f} sec")
print(f"Variance with numpy: {sol} \n")

# compute and print the count frequency of the column 2 with both methods
print(f"Count frequency: {df.countFrequency(2)}")

t1 = time.time()
sol=df.countFrequency_np(2)
t2 = time.time()
print(f"countFrequency_np ran in {t2 - t1:.3f} sec")
print(f"Count frequency with numpy: {sol} \n")

# compute and print the median of the column 2 with both methods
print(f"Median: {df.median_col(2)}")

t1 = time.time()
sol=df.median_col_np(2)
t2 = time.time()
print(f"median_col_np ran in {t2 - t1:.3f} sec")
print(f"Median with numpy: {sol} \n")

# compute and print the standard deviation of the column 2 with both methods
print(f"Standard deviation: {df.std_dev(2)}")

t1 = time.time()
sol= df.std_dev_np(2)
t2 = time.time()
print(f"std_dev_np ran in {t2 - t1:.3f} sec")
print(f"Median with numpy: {sol} \n")

# compute and print the correlation between column 2 and 3 with both methods
print(f"Correlation analysis: {df.correlation_analysis(2, 1)}")

t1 = time.time()
sol=df.correlation_analysis_np(2, 1)
t2 = time.time()
print(f"correlation_analysis_np ran in {t2 - t1:.3f} sec")
print(f"Correlation analysis with numpy: {sol} \n")

# compute and print the classification of the column 2
print("Classification: ")
df.classification("Urban", 3, "./solutions_csv/classification")

# compute and print the summary of the dataset with both methods
print("\nSummary: ")
df.summary("./solutions_csv/summary")
df.summary_np("./solutions_csv/summary_np")
# plot the histogram of the column 2
df.plot_histogram(2, "./plots_csv/histogram.png") 
# plot the scatter plot between column 1 and 2
df.scatter_plot(1, 2, "./plots_csv/scatter_plot.png")

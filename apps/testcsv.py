import csvparserpy


# Create an instance of CSVParserpy
df = csvparserpy.CSVParserpy("../csv_examples/house.csv")
# compute and print the mean of the column 2 with both methods
print(df.mean_col(2))
print(df.mean_col_np(2))
# compute and print the variance of the column 2 with both methods
print(df.var_col_np(2))
print(df.var_col(2))
# compute and print the count frequency of the column 2 with both methods
print(df.countFrequency(2))
print(df.countFrequency_np(2))
# compute and print the median of the column 2 with both methods
print(df.median_col(2))
print(df.median_col_np(2))
# compute and print the standard deviation of the column 2 with both methods
print(df.std_dev(2))
print(df.std_dev_np(2))
# compute and print the correlation between column 2 and 3 with both methods
print(df.correlation_analysis(2, 1))
print(df.correlation_analysis_np(2, 1))
# compute and print the classification of the column 2
df.classification("Urban", 3, "./solutions_csv/classification")
# compute and print the summary of the dataset with both methods
df.summary("./solutions_csv/summary")
df.summary_np("./solutions_csv/summary_np")
# plot the histogram of the column 2
df.plot_histogram(2, "./plots_csv/histogram.png") 
# plot the scatter plot between column 1 and 2
df.scatter_plot(1, 2, "./plots_csv/scatter_plot.png")

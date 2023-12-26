import csvparser


c = csvparser.CSVParser("../csv_examples/Iris.csv")
c.read()
c.summary("output")


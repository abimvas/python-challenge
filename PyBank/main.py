#dependencies
import os
import csv

data1_csv = os.path.join("budget_data_1.csv")

#total number of months
with open(data1_csv, newline="") as csvreader:
    next(csvreader)
    total_months = len(list(csvreader))
    print("Financial Analysis")
    print("---------------------")
    print("Total Months: " + str(total_months))

#total amount of revenue gained    
with open(data1_csv, newline="") as csvreader:
    next(csvreader)
    total = sum(int(r[1]) for r in csv.reader(csvreader))
    print("Total Revenue: $" + str(total))
    
#average change in revenue    
    average = total/total_months
    print("Average Revenue Change: $" + str(average))
    
#greatest increase
with open(data1_csv, newline="") as csvreader:
    next(csvreader)
    increase_month = max((r[0]) for r in csv.reader(csvreader))
    
with open(data1_csv, newline="") as csvreader:
    next(csvreader)
    increase_amt = max(int(r[1]) for r in csv.reader(csvreader)) 
    
    print("Greatest Increase in Revenue: " + str(increase_month)+ " " + "($" + str(increase_amt) + ")")

#greatest decrease
with open(data1_csv, newline="") as csvreader:
    next(csvreader)
    decrease_amt = min(int(r[1]) for r in csv.reader(csvreader))
    
with open(data1_csv, newline="") as csvreader:
    next(csvreader)
    decrease_month = min((r[0]) for r in csv.reader(csvreader))
    
    print("Greatest Decrease in Revenue: " + str(increase_month)+ " " + "($" + str(increase_amt) + ")")
import csv

load = "/Users/hugogarcia/Desktop/Data BootCamp/python-challenge/PyBank/budget_data.csv"
output = "/Users/hugogarcia/Desktop/Data BootCamp/python-challenge/PyBank/analysis.txt"

total_months = 0
prev_revenue = 0
change_month = []
revenue_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]
total_revenue = 0

with open(load) as data:
    reader = csv.DictReader(data)

    for row in reader:

        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        revenue_change_update = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change = revenue_change + ["revenue_change_update"]
        change_month = change_month + [row["Date"]]

        if (revenue_change_update > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change_update

        if(revenue_change_update < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change_update

revenue_avg = sum(revenue_change) / len(revenue_change)

output = (
    f"\nFinancial Analysis\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: {revenue_avg}\n"
    f"Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})\n"

)

print(output)

with open(output, "w") as txt_file:
    txt_file.write(output)

    
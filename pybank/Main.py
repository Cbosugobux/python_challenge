import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("..", "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("..", "Analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
m2mNetChangeList = []
greatest_increase = ["", float('-inf')]
greatest_decrease = ["", float('inf')]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    firstDataRow = next(reader)
    total_months += 1
    total_net += float(firstDataRow[1])
    prev_net = float(firstDataRow[1])

    # Process each row of data
    for row in reader:
        # Track Total Months
        total_months += 1

        # Track the total
        current_net = float(row[1])
        total_net += current_net

        # Track the net change
        m2mChange = current_net - prev_net
        m2mNetChangeList.append(m2mChange)
        prev_net = current_net

        # Calculate the greatest increase in profits (month and amount)
        if m2mChange > greatest_increase[1]:
            greatest_increase = [row[0], m2mChange]

        # Calculate the greatest decrease in losses (month and amount)
        if m2mChange < greatest_decrease[1]:
            greatest_decrease = [row[0], m2mChange]

# Calculate the average net change across the months
average_net_change = sum(m2mNetChangeList) / len(m2mNetChangeList) if m2mNetChangeList else 0

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------------------------\n"
    f"\n"
    f"Total Months: {total_months}\n"
    f"\n"
    f"Total: ${total_net:.2f}\n"
    f"\n"
    f"Average Change: ${average_net_change:.2f}\n"
    f"\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:.2f})\n"
    f"\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:.2f})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

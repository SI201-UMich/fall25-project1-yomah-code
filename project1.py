# SI 201 Project 1 
# Name:  Katia Hemphill
# Student ID: 47379841
# Email: katiah@umich.edu
# Collaborators: Myself
# AI Tools Used: ChatGPT was used to help debug, guide structure, and explain functions, had to understand what UTF-8 encoding meant

#PART 2: Read and Analyze the File
import csv
def load_superstore(filename): #reads a CSV file and returns a list of dictionaries
    with open(filename, newline='', encoding ='utf-8') as csvfile: #Ensures that the file is read using UTF-8 encoding, which supports most characters (like accented letters, emojis, etc.).
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data 

#PART 3: DECIDE WHAT TO CALCULATE
#Calculation 1 - "What is the average profit margin on Office Supplies?"
def calc_average_profit_margin_office_supplies(data):  #Category, Profit, Quantity
    total_margin = 0
    count = 0
    for row in data: 
        if row["Category"] == "Office Supplies":
            profit = float(row["Profit"])
            sales = float(row["Sales"])
            margin = profit / sales

            total_margin += margin     # accumulate!
            count += 1                 # count rows
            
    average_margin = total_margin / count #add up all margins and divide by count 
    return average_margin

#calculation 2 - Which postal code in the United States has the highest total sales? 
def calc_sales_by_postal_code(data): # Postal Code, Country, Sales
    sales_totals = {}  # key = postal code, value = total sales

    for row in data:
        if row["Country"] == "United States":
            state = row["State"]             # New column added!
            postal_code = row["Postal Code"]
            sales = float(row["Sales"])

            key = (state, postal_code)       # group by BOTH state & postal
            if key in sales_totals:
                sales_totals[key] += sales
            else:
                sales_totals[key] = sales

    highest = max(sales_totals, key=sales_totals.get)
    return highest, sales_totals[highest]  # returns (state, postal), total sales
#PART 4

def generate_results_to_text(result1, result2, filename="results.txt"):
    with open(filename, "w") as file:
        file.write("PROJECT RESULTS\n")
        file.write("---------------------\n") # Write a separator line to make the output easier to read.
        file.write(f"1. Average Profit Margin for Office Supplies: {result1:.4f}\n") # formats result1 to 4 decimal places. Example: 0.157264 -> 0.1573
        file.write(f"2. Highest Total Sales by Postal Code (United States):\n")         # result2 is expected to be a tuple like ("12345", 50000.25)
        file.write(f"Postal Code: {result2[0]}\n") # This line writes the postal code (first item in the tuple).
        file.write(f"Total Sales: ${result2[1]:.2f}\n") # This line writes the total sales (second item in the tuple).


#PART 5: Problem decomposition - Google Drawing

#Part 6 - Test Functions

def test_calc_average_profit_margin_office_supplies():
    # General case 1
    # Profit margin for each:
    #   10/100 = 0.1
    #   20/200 = 0.1
    # Average = (0.1 + 0.1) / 2 = 0.1
    # abs() is used to handle floating-point rounding differences.
    data = [
        {"Category": "Office Supplies", "Profit": "10", "Sales": "100"},
        {"Category": "Office Supplies", "Profit": "20", "Sales": "200"},
    ]
    result = calc_average_profit_margin_office_supplies(data)
    assert abs(result - 0.1) < 0.0001  # (0.1 + 0.1) / 2

    # General case 2
    data = [
        {"Category": "Office Supplies", "Profit": "5", "Sales": "50"},
        {"Category": "Furniture", "Profit": "100", "Sales": "200"},  # ignored
    ]
    result = calc_average_profit_margin_office_supplies(data)
    assert abs(result - 0.1) < 0.0001

    # Edge case 1: zero sales (avoid division by zero)
    data = [{"Category": "Office Supplies", "Profit": "5", "Sales": "0"}]
    try:
        calc_average_profit_margin_office_supplies(data)
    except ZeroDivisionError: #Error when trying to divide by 0
        pass  # acceptable edge handling

    # Edge case 2: no Office Supplies rows
    data = [{"Category": "Technology", "Profit": "10", "Sales": "100"}]
    try:
        calc_average_profit_margin_office_supplies(data)
    except ZeroDivisionError:
        pass


def test_calc_sales_by_postal_code():
    # General case 1
    data = [
        {"Country": "United States", "State": "California", "Postal Code": "12345", "Sales": "100"},
        {"Country": "United States", "State": "California", "Postal Code": "12345", "Sales": "200"},
    ]
    result = calc_sales_by_postal_code(data)
    assert result == (("California", "12345"), 300.0)

    # General case 2
    data = [
        {"Country": "United States", "State": "Texas", "Postal Code": "11111", "Sales": "50"},
        {"Country": "United States", "State": "Florida", "Postal Code": "22222", "Sales": "200"},
    ]
    result = calc_sales_by_postal_code(data)
    assert result == (("Florida", "22222"), 200.0)

    # Edge case 1: no U.S. rows
    data = [{"Country": "Canada", "State": "Ontario", "Postal Code": "99999", "Sales": "100"}]
    try:
        calc_sales_by_postal_code(data)
    except ValueError:
        pass  # acceptable edge behavior

    # Edge case 2: missing sales values
    data = [{"Country": "United States", "State": "Ohio", "Postal Code": "11111", "Sales": ""}]
    try:
        calc_sales_by_postal_code(data)
    except ValueError:
        pass

# Run tests
test_calc_average_profit_margin_office_supplies()
test_calc_sales_by_postal_code()
print("All tests passed!")

#fixed debugging error in main

def main():
    filename = "SampleSuperstore.csv"
    data = load_superstore(filename)

    result1 = calc_average_profit_margin_office_supplies(data)
    result2 = calc_sales_by_postal_code(data)
    generate_results_to_text(result1, result2)
    print("Results written to results.txt")

if __name__ == "__main__":
    main()

#testing for git commits


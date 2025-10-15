# SI 201 Project 1 
# Your Name: Katia Hemphill
# Your UMich Email: Katiah@umich.edu
# Collaborators (if any): 

import csv
def read_csv_file(filename): #reads a CSV file and returns a list of dictionaries
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
            postal_code = row["Postal Code"]
            sales = float(row["Sales"])

            if postal_code in sales_totals:
                sales_totals[postal_code] += sales
            else:
                sales_totals[postal_code] = sales

    highest_postal_code = max(sales_totals, key=sales_totals.get)
    return highest_postal_code, sales_totals[highest_postal_code]
#PART 4

def write_results_to_file(result1, result2, filename="results.txt"):
    with open(filename, "w") as file:
        file.write("PROJECT RESULTS\n")
        file.write("---------------------\n")
        file.write(f"1. Average Profit Margin for Office Supplies: {result1:.4f}\n")
        file.write(f"2. Highest Total Sales by Postal Code (United States):\n")
        file.write(f"   Postal Code: {result2[0]}\n")
        file.write(f"   Total Sales: ${result2[1]:.2f}\n")

def main():
    filename = "SampleSuperstore.csv"
    data = read_csv_file(filename)

    result1 = calc_average_profit_margin_office_supplies(data)
    result2 = calc_sales_by_postal_code(data)
    write_results_to_file(result1, result2)
    print("Results written to results.txt")

if __name__ == "__main__":
    main()

#PART 5: Problem decomposition - Google Drawing


#Part 6 - Test Functions

def test_calc_average_profit_margin_office_supplies():
    # General case 1
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
    except ZeroDivisionError:
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
        {"Country": "United States", "Postal Code": "12345", "Sales": "100"},
        {"Country": "United States", "Postal Code": "12345", "Sales": "200"},
    ]
    result = calc_sales_by_postal_code(data)
    assert result == ("12345", 300.0)

    # General case 2
    data = [
        {"Country": "United States", "Postal Code": "11111", "Sales": "50"},
        {"Country": "United States", "Postal Code": "22222", "Sales": "200"},
    ]
    result = calc_sales_by_postal_code(data)
    assert result == ("22222", 200.0)

    # Edge case 1: no U.S. rows
    data = [{"Country": "Canada", "Postal Code": "99999", "Sales": "100"}]
    try:
        calc_sales_by_postal_code(data)
    except ValueError:
        pass  # acceptable edge behavior

    # Edge case 2: missing sales values
    data = [{"Country": "United States", "Postal Code": "11111", "Sales": ""}]
    try:
        calc_sales_by_postal_code(data)
    except ValueError:
        pass


# Run tests
test_calc_average_profit_margin_office_supplies()
test_calc_sales_by_postal_code()
print("All tests passed!")

#fixed debugging error in main



#testing for git commits


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

#PART 2

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

#calculation 2 - "Highest total shipping cost by postal code in a country"
def calc_highest_total_shipping_cost_by_postal_code(data): #Postal Code, Country, Shipping Cost
    shipping_totals = {}  # key = postal code, value = total shipping cost
    for row in data:
        if row["Country"] == "United States":
            postal_code = row["Postal Code"]

            shipping_cost = float(row["Shipping Cost"]) # Convert shipping cost from string to float
            if postal_code in shipping_totals:  # if we've seen this postal code before
                shipping_totals[postal_code] += shipping_cost
            else:
                shipping_totals[postal_code] = shipping_cost  
    # Step 4: Find the postal code with the highest total shipping cost
    highest_postal_code = None
    highest_cost = 0

    for postal_code, total_cost in shipping_totals.items():
        if total_cost > highest_cost:
            highest_cost = total_cost
            highest_postal_code = postal_code

    # Step 5: Return the result clearly
    return highest_postal_code, highest_cost

#PART 4

def write_results_to_file(result1, result2, filename="results.txt"):
    with open(filename, "w") as file:
        file.write("PROJECT RESULTS\n")
        file.write("---------------------\n")
        file.write(f"1. Average Profit Margin for Office Supplies: {result1:.4f}\n")
        file.write(f"2. Highest Total Shipping Cost by Postal Code (United States):\n")
        file.write(f"   Postal Code: {result2[0]}\n")
        file.write(f"   Total Shipping Cost: ${result2[1]:.2f}\n")

def main():
    filename = "SampleSuperstore.csv"
    data = read_csv_file(filename)
    result1 = calc_average_profit_margin_office_supplies(data)
    result2 = calc_highest_total_shipping_cost_by_postal_code(data)
    write_results_to_file(result1, result2)
    print("Results written to results.txt")

if __name__ == "__main__":
    main()





    



# def main():
#     filename = "SampleSuperstore.csv"  # don't use input() like that
#     data = read_csv_file(filename)
#
#     # Call your calculations
#     result1 = calc_average_profit_margin_office_supplies(data)
#     result2 = calc_second_calculation(data)
#
#     # Save results
#     results = [result1, result2]
#     write_results_to_file(results, "results.txt")
#
#
# if __name__ == "__main__":
#     main()


#testing for git commits
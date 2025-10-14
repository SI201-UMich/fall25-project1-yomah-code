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
# --- MAIN PROGRAM ---
#PART 2
def main():
    filename = input("SampleSuperstore.csv")
    try:
        data = read_csv_file(filename)
        print("File loaded successfully!")
        print("Number of rows:", len(data))
        print("Column names:", list(data[0].keys()))
        print("Sample row:", data[0])
    except FileNotFoundError:
        print("File not found. Make sure the CSV is in this folder and name is correct.")

# Run main
if __name__ == "__main__":
    main()

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
    return total_margin

#calculation 2 - "Highest total shipping cost by postal code in a country"
def calc_second_calculation(data): #Postal Code, Country, Shipping Cost


#Part 4: OUTPUT FUNCTION
def write_results_to_file(results, output_filename):
    # Placeholder function body to avoid indentation error
    pass





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
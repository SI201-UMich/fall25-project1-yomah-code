# -----------------------------------------
# SI 201 Project 1 
# Your Name: Katia Hemphill
# Your UMich Email: Katiah@umich.edu
# Collaborators (if any)
# -----------------------------------------

import csv
def read_csv_file(filename): #reads a CSV file and returns a list of dictionaries
    with open(filename, newline='', encoding ='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data 
# --- MAIN PROGRAM ---
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


#testing for git commits
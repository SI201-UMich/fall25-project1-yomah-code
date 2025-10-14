fname = input('Enter the file name: ')
fhand = open(fname)
with open("SampleSuperstore.csv") as inFile: 
    lines = inFile.readlines() 


#testing for git commits
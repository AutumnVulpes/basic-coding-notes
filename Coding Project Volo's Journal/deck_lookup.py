import csv

deck = []

# Turn single column csv into list of card names
with open('decklist.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        deck.append(row[0])
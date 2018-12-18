## Twelve Days of Christmas
## Author: nmessa
## Date: 12/20/2016

#create a dictionary that maps numbers to words
day = {1:'first', 2:'second', 3:'third', 4:'fourth', 5:'fifth', 6:'sixth',
       7:'seventh', 8:'eighth', 9:'ninth', 10:'tenth', 11:'eleventh',
       12:'twelfth'}

#print the song and pause after each verse
for i in range(1, 13):
    print('On the', day[i], 'day of Christmas, my true love gave to me')

    if i >= 12:
       print("Twelve Drummers Drumming")
    if i >= 11:
       print("Eleven Pipers Piping")
    if i >= 10:
       print("Ten Lords a Leaping")
    if i >= 9:
       print("Nine Ladies Dancing")
    if i >= 8:
       print("Eight Maids a Milking")
    if i >= 7:
       print("Seven Swans a Swimming")
    if i >= 6:
       print("Six Geese a Laying")
    if i >= 5:
       print("Five Golden Rings")
    if i >= 4:
       print("Four Calling Birds")
    if i >= 3:
       print("Three French Hens")
    if i >= 2:
       print("Two Turtle Doves")
    if i >= 1:
        if i != 1:
            print('and', end = ' ')
        print("a Partridge in a Pear Tree")
    input()

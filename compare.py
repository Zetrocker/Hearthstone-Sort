__author__ = 'Zetrocker'

import requests
import csv
import re
import os.path
import time

file = "data.csv"
url = "https://docs.google.com/spreadsheet/pub?key=0AsKyuF-d-OHadEJQYjlPbzByclBXZUNZcE1PcXdydXc&output=csv"

def update(file, url):
    download = requests.get(url).text
    csv_text = requests.get(url).text
    open(file, 'wb+').write(bytes(download, 'UTF-8'))


if os.path.isfile(file) is False:
    update(file, url)


print("last modified: %s" % time.ctime(os.path.getmtime(file)))
print("created: %s" % time.ctime(os.path.getctime(file)))
# up_x = input('Download update file from LiquidHearth? Y/N ')
# up_x = up_x.lower()
# if up_x == 'y':
#
# file = "data.csv"
#     download = requests.get(url).text
#     open(file, 'r+b').write(bytes(download, 'UTF-8'))
#     print("Downloaded update from: ", url, '\n')
# if up_x == 'n':
#     print('Skipping download\n')
# else:
#     print('invalid selection\n')


card1 = input('First card: ')
# card1 = "Cairne Bloodhoof"
card2 = input('Second Card: ')
# card2 = 'Ysera'

# http://graphemica.com/%E2%B1%A1
# Need to replace *, -, and latin small l with double bar with ""
card_dict = dict(
    [('Best', []), ('Excellent', []), ('Good', []), ('Average', []), ('Poor', []), ('Terrible', [])])
class_ranking = ['rank', 'Best', 'Excellent', 'Good', 'Average', 'Poor', 'Terrible']
with open('data.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    data.__next__()
    for x in data:
        for y in range(1, 7):
            quality = class_ranking[y]
            card_dict[quality].append(x[y])


def find(c):
    """
    this will find the given cards, and return a quality for the best and so forth
    :rtype : int
    """
    global card_quality
    global quality

    for quality in card_dict:
        for card in card_dict[quality]:
            if homogenize(c) == homogenize(card):
                if quality == 'Best':
                    card_quality = 5
                elif quality == 'Excellent':
                    card_quality = 4
                elif quality == 'Good':
                    card_quality = 3
                elif quality == 'Average':
                    card_quality = 2
                elif quality == 'Poor':
                    card_quality = 1
                elif quality == 'Terrible':
                    card_quality = 0
                else:
                    print('could not find card', c)
                return card_quality


def compare(a, b):
    """
    this will rate the cards input by best excellent.. if there is a tie it will pass the cards to a tiebreaker function
    :param a:
    :param b:
    :return:
    """

    c1_quality = find(a)
    c2_quality = find(b)
    if c1_quality > c2_quality:
        print(a, "is better than", b)
    elif c2_quality > c1_quality:
        print(b, "is better than", a)
    else:
        tiebreaker(a, b)


def tiebreaker(a, b):
    global breaker1
    global breaker2
    # breaker1, breaker2 = int, int
    for quality in card_dict:
        for card in card_dict[quality]:
            if homogenize(a) == homogenize(card):
                breaker1 = card_dict[quality].index(card)
            if homogenize(b) == homogenize(card):
                breaker2 = card_dict[quality].index(card)
    if breaker1 == breaker2:
        print("Those are the same card sillypants!")
    if breaker1 < breaker2:
        print(a, "is better than", b)
    if breaker2 < breaker1:
        print(b, "is better than", a)


def homogenize(a):
    return a.lower()


# def purge(x):
#     """
#     removes special characters
#     :type x: str
#     :return z: str
#     """
#     global fixed
#     y = True if re.search('[0-9A-Za-z]', x) else False
#     if y:
#         fixed = ''.join([word.group() for word in re.finditer(r'[0-9A-Za-z\s]+', x)])
#     return fixed
compare(card1, card2)

# True if re.search('[0-9A-Fa-f]', 'g') else False

# print(''.join([word.group() for word in re.finditer(r'[0-9A-Za-z\s]+', '!@#HI DaVE!@#!@# THERE')]))
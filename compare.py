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

#TODO: make update prompt for file, and show last update
print("last modified: %s" % time.ctime(os.path.getmtime(file)))
print("created: %s" % time.ctime(os.path.getctime(file)))
# up_x = input('Download update file from LiquidHearth? Y/N ')
# up_x = up_x.lower()
# if up_x == 'y':
#
# file = "data.csv"
# download = requests.get(url).text
#     open(file, 'r+b').write(bytes(download, 'UTF-8'))
#     print("Downloaded update from: ", url, '\n')
# if up_x == 'n':
#     print('Skipping download\n')
# else:
#     print('invalid selection\n')

def ask_Clean(card1, card2):
    """

    :param card1:
    :param card2:
    :return:
    """

card1 = input('First Card: ')
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

# for i in reversed(class_ranking):
#     rank_quality = i
#     print(i)


def rate(c):
    """
    this will find the given cards, and return a quality for the best and so forth
    :rtype : int, False if no other return
    """
    rank = class_ranking[::-1]
    global card_quality
    global quality
    for quality in card_dict:
        for cards in card_dict[quality]:
            if c.lower() == cards.lower():
                card_quality = rank.index(quality)
                return card_quality
    return False



def compare(a, b):
    """
    this will rate the cards input by best excellent.. if there is a tie it will pass the cards to a tiebreaker function
    :param a:
    :param b:
    :return:
    """

    if rate(a) and rate(b) is not False:
        c1_quality = rate(a)
        c2_quality = rate(b)
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
            if a.lower() == card.lower():
                breaker1 = card_dict[quality].index(card)
            if b.lower() == card.lower():
                breaker2 = card_dict[quality].index(card)
    if breaker1 == breaker2:
        print("Those are the same card sillypants!")
    if breaker1 < breaker2:
        print(a, "is better than", b)
    if breaker2 < breaker1:
        print(b, "is better than", a)

#TODO: make regular expression for this, and refactor this for regex
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
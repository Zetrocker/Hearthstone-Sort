__author__ = 'Zetrocker'

import requests
import csv
import re
import os.path
import time
import datetime

file = "data.csv"
url = "https://docs.google.com/spreadsheet/pub?key=0AsKyuF-d-OHadEJQYjlPbzByclBXZUNZcE1PcXdydXc&output=csv"


def update(file, url):
    download = requests.get(url).text
    csv_text = requests.get(url).text
    open(file, 'wb+').write(bytes(download, 'UTF-8'))


if os.path.isfile(file) is False:
    update(file, url)


def update_prompt():
    """
    asks for update if data is older than a day
    """
    now = datetime.datetime.now()
    fileage = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    tdelta = now - fileage
    t_in_seconds = tdelta.total_seconds()
    if t_in_seconds > 86400:
        print("Current data is older than one day")
        update_ask = input('Download update file from LiquidHearth? Y/N ')
        update_ask.lower()
        if update_ask == 'y':
            update(file, url)
            # download = requests.get(url).text
            # open(file, 'r+b').write(bytes(download, 'UTF-8'))
            # print("Downloaded update from: ", url, '\n')
        else:
            print("Skipping Download\n")

update_prompt()








card1 = "Cairne Bloodhoof"
# card1 = input('First Card: ')

card2 = 'Ysera'
# card2 = input('Second Card: ')




def regex(str):
    """
     removes special characters
     :type x: str
     :return z: str
     """
    garbage = True if re.search('[0-9A-Za-z]', str) else False
    if garbage:
        fixed = ''.join([word.group() for word in re.finditer(r'[0-9A-Za-z\s]+', str)])
        return fixed




card_dict = dict(
    [('Best', []), ('Excellent', []), ('Good', []), ('Average', []), ('Poor', []), ('Terrible', [])])
# card_dict = dict(lambda x: x for class_ranking[range(1, 7)])

class_ranking = ['rank', 'Best', 'Excellent', 'Good', 'Average', 'Poor', 'Terrible']

with open('data.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    data.__next__()
    for x in data:
        for y in range(1, 7):
            card = regex(x[y])
            quality = class_ranking[y]
            card_dict[quality].append(card)


def rate(c):
    """
    this will find the given cards, and return a quality for the best and so forth
    :rtype : list [Card, int for class, row number
    """
    rank = class_ranking[::-1]
    for qualities in card_dict:
        for cards in card_dict[qualities]:
            if cards is not None and c.lower() == cards.lower():
                trump_rank = rank.index(qualities)
                row_rank = card_dict[qualities].index(cards)
                card_tuple = (cards, trump_rank, row_rank)
                card_rating = list(card_tuple)
                return card_rating
    return print("could not find card", c)


def compare(a, b):
    """
    this will rate the cards input by best excellent.. if there is a tie it will pass the cards to a tiebreaker function
    :rtype : string describing winner
    :param a:
    :param b:
    :return:
    """
    c1_quality = rate(a)
    c2_quality = rate(b)
    if type(c1_quality) is list and type(c2_quality) is list:
        card1wins = c1_quality[0], "is better than", c2_quality[0]
        card2wins = c2_quality[0], "is better than", c1_quality[0]
        if c1_quality[1] > c2_quality[1]:
            print(card1wins)
        elif c1_quality[1] < c2_quality[1]:
            print(card2wins)
        elif c1_quality[1] == c2_quality[1]:
            #tiebreaker
            if c1_quality[2] < c2_quality[2]:
                print(card1wins)
            elif c1_quality[2] > c2_quality[2]:
                print(card2wins)
            elif c1_quality[2] == c2_quality[2]:
                print("Those are the same card sillypants!")
    else:
        print("I can't believe you've done this!")






# def tiebreaker(a, b):
#     global breaker1
#     global breaker2
#     # breaker1, breaker2 = int, int
#     for quality in card_dict:
#         for card in card_dict[quality]:
#             if a.lower() == card.lower():
#                 breaker1 = card_dict[quality].index(card)
#             if b.lower() == card.lower():
#                 breaker2 = card_dict[quality].index(card)
#     if breaker1 == breaker2:
#         print("Those are the same card sillypants!")
#     if breaker1 < breaker2:
#         print(a, "is better than", b)
#     if breaker2 < breaker1:
#         print(b, "is better than", a)


compare(card1, card2)



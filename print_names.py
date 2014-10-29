import json

__author__ = 'ben'

with open('AllSets.json', 'r') as f:
    card_data = json.load(f)

names = []
costs = {}
for set in card_data.values():
    costs.update({card['name']: card['id'] for card in set})


print(costs)

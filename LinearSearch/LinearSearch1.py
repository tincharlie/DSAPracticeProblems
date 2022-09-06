"""
Locate Card
"""

def locate_cards(cards, query):
    position = 0
    while True:
        if cards[position] == query:
            return position
        position += 1

        if position == len(cards):
            return -1


card = [2,1,3,4,5,7]
query = 4
print(f"Position of your query {query} is in {locate_cards(card, query)} index")
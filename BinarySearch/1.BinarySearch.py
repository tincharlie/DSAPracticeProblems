"""
Binary Search
"""


def test_location(cards, query, mid):
    mid_number = cards[mid]

    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'Left'
        else:
            return 'found'
    elif mid_number < query:
        return 'Left'
    else:
        return 'Right'



def locate_card_binary(cards, query):
    start = 0
    end = len(cards) - 1
    while start <= end:
        mid = (start + end) // 2
        result = test_location(cards, query, mid)
        if result == "found":
            return mid
        elif result == 'Left':
            start = mid - 1
        elif result == "Right":
            end = mid + 1
    return -1


query = 6
card = [2, 4, 5, 7, 9, 11]
print(locate_card_binary(card, query))


import random
import collections

KIND = ['diamond' , 'hearth' , 'club suit' , 'spade suit']
VALUES = ['A' , '2' , '3' , '4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'J', 'Q', 'K']

def create_cards():
    cards = []
    for kind in KIND:
        for value in VALUES:
            cards.append((kind, value))

    return cards

def get_hand(cards, hand_size):
    hand = random.sample(cards, hand_size)

    return hand

def main(hand_size, attemps):
    cards = create_cards()

    hands = []

    for _ in range(attemps):
        hand = get_hand(cards, hand_size)
        hands.append(hand)

    pairs = 0
    straight = 0
    for hand in hands:
        values = []
        for card in hand:
            values.append(card[1])

        counter = dict(collections.Counter(values))
        if is_straight(counter):
            straight +=1

        for val in counter.values():
            if val == 2:
                pairs += 1
                break
    pairs_stats = pairs / attemps
    straight_stats = straight / attemps

    print(f'The probability of get a straight with a size hand of {hand_size} is {pairs_stats}')
    print(f'The probability of get a straight with a size hand of {hand_size} is {straight_stats}')

def map_card_letter_to_value(value):
    switcher = {
        'J': '10',
        'Q': '11',
        'K': '12',
        'A': '1'
    }

    return switcher.get(value, value)

def map_value_to_card_letter(value):
    switcher = {
        '10': 'J',
        '11': 'Q',
        '12': 'K',
        '1': 'A',
        '13': 'K'
    }

    return switcher.get(value, value)

def is_straight(counter):
    for x in counter:
        next_value = int(map_card_letter_to_value(x)) + 1
        if not map_value_to_card_letter(str(next_value)) in counter:
            return False

    return True

if __name__ == '__main__':
    hand_size = int(input('Hand size? '))
    attemps = int(input('Attemps? '))

    main(hand_size, attemps)

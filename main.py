import random
import collections

KIND = ['diamond' , 'hearth' , 'club suit' , 'spade suit']
VALUES = ['ace' , '2' , '3' , '4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'J', 'Q', 'K']

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
    for hand in hands:
        values = []
        for card in hand:
            values.append(card[1])

        counter = dict(collections.Counter(values))
        print(counter)


if __name__ == '__main__':
    hand_size = int(input('Hand size? '))
    attemps = int(input('Attemps? '))

    main(hand_size, attemps)

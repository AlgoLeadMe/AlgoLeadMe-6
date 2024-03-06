import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
card_deck =  deque([card for card in range(1,N+1)])

while len(card_deck) != 1 : 
    card_deck.popleft()
    card_deck.rotate(-1)

print(card_deck[0])

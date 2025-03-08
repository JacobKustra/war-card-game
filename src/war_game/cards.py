"""Need to import all the cards from json card asset file and set them up."""
from pathlib import Path
import json

path = Path("assets/cards.json")

contents = path.read_text()
cards = json.loads(contents)

deck = cards["deck"]

print(cards)
print(deck)
print(deck[0])
print(deck[0]['suit'])
print(deck[0]['value'])

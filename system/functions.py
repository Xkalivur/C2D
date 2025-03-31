from json import JSONDecodeError
import json
import sys
import random as ran
from collections import Counter

files = [
  "settings.json",
  "play_progress.json"
]

def save(key,factor,location,func):
  try:
    with open(location, 'r') as f:
      acc = json.load(f)
  except (JSONDecodeError, IOError):
    acc = dict()

  with open(location, func) as f:
    acc[key] = factor
    f.seek(0)
    json.dump(acc, f,indent=6)


def load(loader,location):
  with open(location) as f:
    try:
      if f.read().strip() == '':
        return 'No data exist'
      else:
        f.seek(0)
        loadlist = json.load(f)
        data = loadlist[loader]
    except Exception as error:
      return error
  return data

game_set = load("game_data",files[0])

class gameplay:
  def __init__(self):
    data = {}
    with open(files[1],'w') as f:
      json.dump(data,f)
    while True:
      try:
        number_player = int(input("Enter number of player will join\nHost: "))
        if number_player < 2:
          print("\nminimum number of player is 2")
        elif number_player > 10:
          print("\nmaximum number of player is 10")
        else:
          break
      except ValueError:
        print("\nUnable to read. Please retry")
    self.number_player = number_player
    for i in range(1,self.number_player+1):
      save(f"player{i}",[],files[1],'w')

  def __str__(self):
    return f"current player number: {self.number_player}"

  def selection(self,lower,upper):
    while True:
        try:
            response = int(input("User: "))
            if response < lower or response > upper:
                print("option doesn't exist")
            else:
                break
        except:
            print("option doesn't exist")
    return response

  def actions(self):
    print("\nSelect action")
    actions = game_set["actions"]
    act_list = actions["action_list"]["normal"]
    for i in range(1,len(act_list.keys())+1):
      print(f"{i}) {act_list[str(i)]}")
    lower = int(min(act_list.keys()))
    upper = int(max(act_list.keys()))
    while True:
        try:
            response = int(input("User: "))
            if response < lower or response > upper:
                print("\noption doesn't exist")
            else:
                break
        except:
            print("\noption doesn't exist")
    

class cards(gameplay):
  def shuffle(self):
    deck = game_set["characters"]
    with open(files[1],'r+') as f:
      data = json.load(f)
      for i in range(1,self.number_player+1):
        player_cards = []
        for _ in range(3):
          if deck:
            card_types = list(deck.keys())
            selected_card = ran.choice(card_types)
            if deck[selected_card] > 0:
              player_cards.append(selected_card)
              deck[selected_card] -= 1
            else:
              while True:
                card_types.remove(selected_card)
                selected_card = ran.choice(card_types)
                if deck[selected_card] > 0:
                  player_cards.append(selected_card)
                  deck[selected_card] -= 1
                  break
        data[f"player{i}"] = player_cards

      f.seek(0)
      f.truncate()
      json.dump(data, f, indent=6)
      json.dump(deck,f,indent=6)
      print("\nYour influences")
      print(data["player1"])
      


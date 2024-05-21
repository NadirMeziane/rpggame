import random

def showInstructions():
  #print a main menu and the commands
  print('''
  Welcome to your own RPG Game
  ============================

  Get to the Garden with a key and a potion.
  Avoid the monsters!

  Commands:
    go [direction]
    get [item]
  ''')


def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

# an inventory, which is initially empty
inventory = []

# start the player in the Hall
currentRoom = 'Hall'
rooms = {
            'Hall' : { 'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },        
            'Kitchen' : { 'north' : 'Hall',
                },
            'Dining Room' : { 'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'potion'
                },             
            'Garden' : { 'north' : 'Dining Room' },
            'library' :{'item'  : 'BookOfLife'},
            'office' :{},
            'laboratory' :{'item'  : 'Beam-O-Mat'},
         }

# select rooms random to put the monster
roomslist = ["Hall", "Kitchen", "Dining Room", "Garden", "library", "office", "laboratory"]
random_string = random.choice(roomslist)
rooms[random_string]["item"] = "monster"


showInstructions()
while True:
  showStatus()
  move = ""
  while move == "":
      move = input(">")
      move = move.lower().split()
      if move[0] == "exit":
          break
      if move[0] == "go":
          if move[1] in rooms[currentRoom]:
              currentRoom = rooms[currentRoom][move[1]]
          else:
              print("You can't go that way!")
      if move[0] == "get":
          if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
              inventory += [move[1]]
              print(move[1] + ' got!')
              del rooms[currentRoom]['item']
          else:
              print('Can\'t get ' + move[1] + '!')
  if (currentRoom == "Garden" and "key" in inventory and "potion" in inventory) or ("BookOfLife" in rooms["laboratory"]["item"] and "Beam-O-Mat" in rooms["laboratory"]["item"]): 
    print("You escaped the house... YOU WIN!")
    break
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
from random import choice
#Allows us to use choice to randomize responses

def get_game_bot_response(user_response):
  bot_response_story = ["Try What Remains of Edith Finch!", "Try Nier:Automata!", "I recommend Firewatch!", "Check out Last of Us!"]
  bot_response_shooter = ["Check out Valorant!", "The Halo Collection for PC is out! Give it a shot!", "Try out Overwatch!"]
  bot_response_top = ["Breath of the Wild is an amazing game! You should check it out", "Everyone's been playing Amoung Us. Go see what the hype is all about!", "You should try Undertale!"]
  bot_response_other = ["Tic-tac-toe is always a good bet", "Whadda 'bout ball and cup?", "I ran out of suggestions!"]

  if "story" in user_response:
    return choice(bot_response_story)
#If the users response contains the string, it will return a response in that list at random
  elif "shooter" in user_response:
    return choice(bot_response_shooter)
  elif "top" in user_response:
    return choice(bot_response_top)
  else:
    return choice(bot_response_other)
#When the user responds with a word the bot doesn't recognize, it chooses from a list of silly responses




print("Welcome to Gamer Bot")
print("I'll help you pick out a game to play based on a genre!")

user_response = ""
while True:
  user_response = input("What type of game do you want to play?: ")

  if user_response == 'stop':
    break
#This is a loop. It calls on the function on line 4 continuously, until the user says "stop", then it will end.
  
  bot_response = get_game_bot_response(user_response)
  print(bot_response)
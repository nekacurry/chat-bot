from random import choice

def get_game_bot_response(user_response):
  bot_response_story = ["Try What Remains of Edith Finch!", "Try Nier:Automata!", "I recommend Firewatch!", "Check out Last of Us!"]
  bot_response_shooter = ["Check out Valorant!", "The Halo Collection for PC is out! Give it a shot!", "Try out Overwatch!"]
  bot_response_top = ["Breath of the Wild is an amazing game! You should check it out", "Everyone's been playing Amoung Us. Go see what the hype is all about!", "You should try Undertale!"]

  if "story" in user_response:
    return choice(bot_response_story)
  elif user_response == "shooter":
    return choice(bot_response_shooter)
  elif user_response == "top":
    return choice(bot_response_top)
  else:
    return "Tic-tac-toe is always a good bet"




print("Welcome to Gamer Bot")

user_response = ""
while True:
  user_response = input("What type of game do you want to play?: ")

  if user_response == 'done':
    break

  
  bot_response = get_game_bot_response(user_response)
  print(bot_response)
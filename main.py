import art 
import game_data
import random



# TODO: #2 Create a function that returns a random item from game data
def get_game_item():
	"""Returns a random dictionary item from the game data list"""
	item = random.choice(game_data.data)
	return item


# TODO: #1 Create the game start to print out logo and a random item from game data. 
def game_start():

	
	print(art.logo)
	print(f"Your first item is: {get_game_item()}")




game_start()
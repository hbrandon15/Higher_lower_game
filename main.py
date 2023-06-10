import art 
import game_data
import random




def get_game_item():
	"""Returns a random dictionary item from the game data list"""
	item = random.choice(game_data.data)
	return item



def game_start():

	
	print(art.logo)
	print(f"Your first item is: {get_game_item()}")




game_start()
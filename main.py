import art 
import game_data
import random




def get_game_item():
	"""Returns a random dictionary item from the game data list"""
	item = random.choice(game_data.data)
	return item


def get_values(selected_dict):
	"""Returns a list of the values from a provided dictionary"""
	value_list = []
	name = selected_dict["name"]
	followers = selected_dict["follower_count"]
	desc = selected_dict["description"]
	country = selected_dict["country"]
	value_list = [name, followers, desc, country]
	return value_list

def game_start():

	# TODO: #3 item needs to be redacted to hide the follow count. 
	# TODO: #4 follow count needs to be saved in a separate variable
	print(art.logo)
	item1 = get_game_item()
	item_values = get_values(item1)
	follow_count_A = item_values[1]
	print(f"Compare A: {item_values[0]}, a {item_values[2]} from {item_values[3]}")




game_start()
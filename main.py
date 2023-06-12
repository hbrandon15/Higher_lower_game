import art 
import game_data
import random




def get_game_items():
	"""Returns a random dictionary item from the game data list"""
	return random.choices(game_data.data, k =2)


def get_values(selected_dict):
	"""Returns a list of the values from a provided dictionary"""
	value_list = []
	name = selected_dict["name"]
	followers = selected_dict["follower_count"]
	desc = selected_dict["description"]
	country = selected_dict["country"]
	value_list = [name, followers, desc, country]
	return value_list

def compare_followers(A_followers, B_followers, user_ans):
	"""This function compares two follow counts. If the user guessed the correct option, the function returns 1 otherwise 0."""
	if(A_followers > B_followers and user_ans == "A"):
		return 1
	elif(B_followers > A_followers and user_ans == "B"):
		return 1 
	else: 
		return 0


def guess(A_followers, B_followers):
	user_guess = input("Who has more followers?").upper()
	comparison_results = compare_followers(A_followers, B_followers, user_guess)
	if(comparison_results == 1):
		print("You are correct")
	else: 
		print("You are not correct")


def game_start():


	print(art.logo)
	item1 = get_game_items()[0]
	item2 = get_game_items()[1]
	print(f"item 1 is {item1}")
	print(f"item 2 is {item2}")
	

	# while(item1 == item2):
	# 	item2 = get_game_item()
	# else:
	# 	item1_values = get_values(item1)
	# 	item2_values  = get_values(item1)
	# 	follow_count_A = item1_values[1]
	# 	follow_count_B = item2_values[1]
	# 	print(f"Compare A: {item1_values[0]}, a {item1_values[2]} from {item1_values[3]}\n")
	# 	print(art.vs)
	# 	print(f"Compare B: {item2_values[0]}, a {item2_values[2]} from {item2_values[3]}\n")
	# 	guess(follow_count_A, follow_count_B)
		





game_start()
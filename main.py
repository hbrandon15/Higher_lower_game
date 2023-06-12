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

def compare_followers(list1, list2, user_ans):
	"""This function compares two follow counts. If the user guessed the correct option, the function returns 1 otherwise 0."""
	if(A_followers > B_followers and user_ans == "A"):
		print(f"{A_followers} is greater than {B_followers}!")
		return 1, user_ans
	elif(B_followers > A_followers and user_ans == "B"):
		print(f"{B_followers} is greater than {A_followers}!")
		return 1, user_ans
	else: 
		return 0

def game_continue(user_correct, current_score):
	"""Accepts a boolean and the current score to see if the user got the correct answer and calculates score. If user correct, add 1 to score. Else, return current score."""
	if user_correct:
		current_score  += 1
		print(f"Current score is {current_score}")
		return current_score
	else:
		print(f"Game over! You finished the game with an overall score of {current_score}")
		return current_score



def guess(A_list, B_list):
	"""Accepts two list items and asks the user to guess which item has the larger number. If user is correct return 1 for True AND correct list, else False"""
	user_guess = input("Who has more followers?\n").upper()
	A_follower = A_list[1]
	B_follower = B_list[1]
	if(A_follower > B_follower and user_guess == "A"):
		print(f"{A_follower} is greater than {B_follower}!")
		return 1, A_list
	elif(B_follower > A_follower and user_guess == "B"):
		print(f"{B_follower} is greater than {A_follower}!")
		return 1, B_list
	else: 
		return 0



def game_start():
	score = 0
	print(art.logo)
	item1 = get_game_items()[0]
	item2 = get_game_items()[1]

	item1_values = get_values(item1)
	item2_values  = get_values(item2)

	follow_count_A = item1_values[1]
	follow_count_B = item2_values[1]
	print(f"Compare A: {item1_values[0]}, a {item1_values[2]} from {item1_values[3]}\n")
	print(art.vs)
	print(f"Compare B: {item2_values[0]}, a {item2_values[2]} from {item2_values[3]}\n")

		

		





game_start()
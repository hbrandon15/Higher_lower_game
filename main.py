import art
import game_data
import random




def get_game_item():
	"""Returns 1 random dictionary items from the game data list"""
	return random.choice(game_data.data)


def format_data(selected_dict):
	"""Prints out the values from a provided dictionary"""
	
	name = selected_dict["name"]
	desc = selected_dict["description"]
	country = selected_dict["country"]
	return (f"{name}, a {desc} from {country}.\n")
	



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
	item_a = get_game_item()
	item_b = get_game_item()
	if item_a == item_b:
		item_b = random.choice(game_data.data)
	

	print(f"Compare A: {format_data(item_a)}")
	print(f"Compare B: {format_data(item_b)}")
	# print(art.vs)
	# print(f"Compare B: {item2_values[0]}, a {item2_values[2]} from {item2_values[3]}\n")

	# is_user_correct = True
	# if guess(item1_values,item2_values)[0] == 1:
	# 	print("You are correct")
	# 	while(is_user_correct):
	# 		score += 1
	# 		print(f"Your score is {score}.")
	# 		compare_A = guess(item1_values,item2_values)[1] # list
	# 		new_compare = get_game_items[0]
	# 		new_compare_items = get_values(new_compare)

	# 		print(f"Compare A: {compare_A[0]}, a {compare_A[2]} from {compare_A[3]}\n")
	# 		print(art.vs)
	# 		print(f"Compare B: {new_compare_items[0]}, a {new_compare_items[2]} from {new_compare_items[3]}\n")
	# 		if guess(compare_A, new_compare_items) != 1:
	# 			print(f"Your final score is {score}")
	# 			break
	# 		else:
	# 			continue




			
			
	# else: 
	# 	print("You are not correct")

		

		





game_start()
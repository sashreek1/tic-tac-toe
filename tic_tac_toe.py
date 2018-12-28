


#global player_list


win_stat = None# holds the place for the wining player

print ("player 1 is always 'x' and player 2 is always'o'" )



#function  definition begins here



def grid_maker(input):#function to print the tic-tac-toe board

	print("\n"*100)
	print(f"   {input[7]}| {input[8]}  |   {input[9]}")
	print("==============")
	print(f"   {input[4]}| {input[5]}  |   {input[6]}")
	print("==============")
	print(f"   {input[1]}| {input[2]}  |   {input[3]}")


def ask_inputs_x(game1_list):#player 2's move request
	while True:#using while loops to to prevent oerwriting 
		x_pos = int(input('player1 where would you like to place "x"'))
		if game1_list[x_pos] == '':
			game1_list[x_pos] = "X"
			break
		else:
			print('that space is taken :) ')
			continue


def ask_inputs_o(game_list):#player 1's move request
	while True:
		o_pos = int(input('player2 where would you like to place "O"'))
		if game_list[o_pos] == '':
			game_list[o_pos] = "O"
			break
		else:
			print("that place is taken :)")
			continue
		

def check_win(new_list):# checks for all possible methods to win
	if (new_list[1]==new_list[2]==new_list[3]==('X'or'O')or
		new_list[4]==new_list[5]==new_list[6]==('X'or'O')or
		new_list[7]==new_list[8]==new_list[9]==('X'or'O')or
		new_list[7]==new_list[4]==new_list[1]==('X'or'O')or
		new_list[8]==new_list[5]==new_list[2]==('X'or'O')or
		new_list[9]==new_list[6]==new_list[3]==('X'or'O')or
		new_list[7]==new_list[5]==new_list[3]==('X'or'O')or
		new_list[9]==new_list[5]==new_list[1]==('X'or'O'))== True:
		return True
	else:
		return False

def main():
	while True:
		player_list = ['#','','','','','','','','','']
		for i in range(1,10):
			if i%2 == 0:
				ask_inputs_o(player_list)
				grid_maker(player_list)
				if check_win(player_list)== True:
					win_stat = 'player2'
					print(f'the winner is {win_stat}')
					break

			else:
				ask_inputs_x(player_list)
				grid_maker(player_list)
				if check_win(player_list)== True:
					win_stat = 'player1'
					print(f'the winner is {win_stat}')
					break
		else:
			print("therfore it is a tie goodluck next time!!!!!")
		x = input("would you like to play again(y/n)?")
		if x == 'y':
			pass
		else:
			break
			print('thanks for playing')

main()
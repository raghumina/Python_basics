# Searching in the list 
# players = ['Messi','Neymar','Xavi','Inesta','Pique']
# print(players[1])
 
# print(players.index('lenglet'))  # langlet is not in the list so it will give a value error 

# using a loop for this 
# for steps in range(4):  # this will print the whole list upto the steps is given
#     print(players[steps])
# players.remove('Messi')
# print(players[0])

# find out how many enteries are there in the list 

# nbrEnteries = len(players)
# for steps in range(nbrEnteries):  # this will print the whole list upto the steps is given
#     print(players[steps])

# # another way for this is 
# for allPlayers in players:
#     print(allPlayers)


# Sort names in alphabstical orders 
players.sort()
for players in players:
    print(players)
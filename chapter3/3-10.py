games = ["Halo", "Minecraft", "The Sims", "Call of Duty", "Grand Theft Auto V"]
print('My favorite games are: ', games)

print('Favorite game: ', games[0].lower())

games[0] = 'Pokemon'
print('No,its not my favorite game.My favorite game is: ', games[0].lower())

games.append('Mario Kart Wii')
print ('Add new game: ',games[-1])
games.insert(2, 'Super Mario Bros.')
print('Insert new game: ',games[2])
print('Now my favorite games are: ', games)
print('-------------------------------------') 

removed_game = 'The Sims'
games.remove(removed_game)
print('I dont like:',removed_game,'and i will delete it from my list.')
print('Now my favorite games are: ', games)
removed_game2 = games.pop(1)
print('I also dont like:',removed_game2,'and it will delete itself .')
print('Now my favorite games are: ', games)
print('-------------------------------------') 

#games_copy = games#这行代码并不会创建一个副本，而是让 games_copy 引用同一个列表，这意味着对 games_copy 的修改会影响到 games。如果需要创建一个真正的副本，可以使用：
games_copy = games.copy()
games_copy.sort()
print('My favorite games in alphabetical order are: ',games_copy)
print('original list: ',games) 
games.reverse()
print('reverse order: ',games)
games.reverse()
print('reverse again: ',games)

print('Now I have',len(games),'games in my list.')
import random 
import words_list
hangman=['''
   +----+
   |    |
   O    |
  /|\   | 
  / \   |
        | 
==========   
''','''
   +----+
   |    |
   O    |
  /|\   | 
  /     |
        | 
==========   
''','''
   +----+
   |    |
   O    |
  /|\   | 
        |
        | 
==========   
''','''
   +----+
   |    |
   O    |
  /|    | 
        |
        | 
==========   
''','''
   +----+
   |    |
   O    |
   |    | 
        |
        | 
==========   
''','''
   +----+
   |    |
   O    |
        | 
        |
        | 
==========   
''','''
   +----+
   |    |
        |
        | 
        |
        | 
==========   
''' ]

print("Let's Play Hangman!!")
print("You have only 6 lives so try to guess the word within 6 attemps!Good Luck")
player1=random.choice(words_list.words)
print(player1)
blanks=["_"]*(len(player1))

print(blanks)

lives=6
game_over=False
while not game_over:
    guessed_word=input("Guess the letter:").lower()
    for pos in range(0,len(player1)):
        if guessed_word==player1[pos]:
            blanks[pos]=player1[pos]
    print(blanks)
    if guessed_word not in player1:
        lives=lives-1
        if lives==0:
            game_over=True
            print("You loose!!")
    if '_' not in blanks:
        game_over=True
        print("You win!!")
    print(hangman[lives])


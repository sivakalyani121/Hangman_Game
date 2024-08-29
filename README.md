Here's a README file for your Hangman game:

---

# Hangman Game

Welcome to the Hangman game! This is a simple command-line version of the classic word-guessing game where you try to guess a word one letter at a time. You have a limited number of incorrect guesses, so choose wisely!
## Introduction

Hangman is a word-guessing game where you need to guess a hidden word by suggesting letters within a certain number of guesses. This version of the game is implemented in Python.

## Game Rules

1. The computer randomly selects a word from a predefined list.
2. You need to guess the word by entering one letter at a time.
3. For every incorrect guess, a part of the hangman figure is drawn.
4. You have 6 incorrect guesses (lives) before the game ends.
5. If you guess all the letters in the word correctly, you win.
6. If you run out of lives before guessing the word, you lose.

## Requirements

To play this game, you need Python installed on your system. You also need a module named `words_list` that contains a list of words to choose from.

### Example `words_list.py`

```python
words = ['python', 'java', 'kotlin', 'javascript', 'typescript', 'hangman', 'coding']
```

## How to Play

1. Clone or download this repository to your local machine.
2. Make sure you have the `words_list.py` file in the same directory as the game script.
3. Run the game script using Python:

   ```bash
   python hangman_game.py
   ```

4. Follow the on-screen instructions to start guessing the word.

## Game Walkthrough

1. **Start the Game**: Run the script, and the game will display a welcome message and instructions.
   
2. **Word Selection**: A random word from `words_list` is selected, and the player will see blank spaces representing each letter of the word.

3. **Guessing Letters**: Enter a letter you think might be in the word. If the letter is correct, it will fill in the blanks. If incorrect, you will lose a life, and part of the hangman figure will be drawn.

4. **Game End**: The game ends when you either guess the word correctly (you win) or you run out of lives (you lose).

5. **Visual Feedback**: The hangman figure is displayed to show the number of incorrect guesses left.

### Sample Game Output

```
Let's Play Hangman!!
You have only 6 lives so try to guess the word within 6 attempts! Good Luck
_ _ _ _ _ _ _
Guess the letter: a
['_', '_', '_', 'a', '_', '_', '_']
+----+
|    |
O    |
     |
     |
     |
==========
```

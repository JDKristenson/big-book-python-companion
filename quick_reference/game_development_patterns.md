# Game Development Patterns - Quick Reference

Common patterns used across the game projects in The Big Book of Small Python Projects.

## Table of Contents
- [Game Loop Structure](#game-loop-structure)
- [Input Validation](#input-validation)
- [Game State Management](#game-state-management)
- [Win Condition Detection](#win-condition-detection)
- [AI and Random Behavior](#ai-and-random-behavior)
- [Turn-Based Games](#turn-based-games)
- [Betting and Score Systems](#betting-and-score-systems)

---

## Game Loop Structure

### Basic Game Loop
The fundamental pattern for interactive games:

```python
def main():
    print("Welcome to the Game!")
    
    while True:  # Main game loop
        # Set up new round/game
        setup_game()
        
        # Play one round
        while not is_game_over():
            display_game_state()
            player_move = get_player_input()
            update_game_state(player_move)
            check_win_condition()
        
        # Show results
        display_results()
        
        # Ask to play again
        if not play_again():
            break
    
    print("Thanks for playing!")
```

**Examples:** Blackjack, Hangman, Tic-Tac-Toe

### Infinite Loop Pattern
For continuous animations or simulations:

```python
import sys

try:
    while True:  # Loop forever
        update_animation()
        display_frame()
        time.sleep(0.1)  # Control speed
except KeyboardInterrupt:
    print("\nProgram stopped.")
    sys.exit()
```

**Examples:** Conway's Game of Life, Bouncing DVD Logo

---

## Input Validation

### Validated Input Loop
Keep asking until valid input is received:

```python
def get_player_move():
    """Get and validate player input."""
    while True:
        response = input('> ').upper().strip()
        
        if response in VALID_MOVES:
            return response
        
        print(f"Invalid input. Please enter one of: {', '.join(VALID_MOVES)}")
```

**Examples:** Blackjack (H/S/D), Tic-Tac-Toe (board positions)

### Number Range Validation
```python
def get_bet(max_bet):
    """Get a valid bet amount."""
    while True:
        print(f'How much do you bet? (1-{max_bet}, or QUIT)')
        bet = input('> ').upper().strip()
        
        if bet == 'QUIT':
            sys.exit()
        
        if not bet.isdecimal():
            continue
        
        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet
        
        print(f"Please enter a number between 1 and {max_bet}")
```

**Examples:** Blackjack, Cho-Han

### Yes/No Confirmation
```python
def play_again():
    """Ask if player wants to play again."""
    print('Do you want to play again? (yes or no)')
    response = input('> ').lower()
    return response.startswith('y')
```

**Examples:** Bagels, Guessthenumber

---

## Game State Management

### Dictionary with Coordinate Keys
Perfect for board games and grids:

```python
# Initialize empty board
board = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        board[(x, y)] = EMPTY

# Access and modify
board[(3, 5)] = PLAYER_PIECE
if board[(x, y)] == EMPTY:
    # Space is available
```

**Examples:** Conway's Game of Life, Four-in-a-Row, Tic-Tac-Toe

### List-Based Board
```python
# Create 3x3 board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Access: board[row][col]
board[1][1] = 'X'

# Display
for row in board:
    print('|'.join(row))
```

**Examples:** Tic-Tac-Toe (alternative), Sudoku

### Game State Dict
```python
game_state = {
    'player_hp': 100,
    'score': 0,
    'level': 1,
    'inventory': ['sword', 'shield'],
    'position': (5, 10)
}

# Easy to pass around and modify
def update_score(state, points):
    state['score'] += points
```

---

## Win Condition Detection

### Check After Each Move
```python
def check_winner(board):
    """Return winner symbol or None."""
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None  # No winner yet
```

**Examples:** Tic-Tac-Toe, Four-in-a-Row

### Value Comparison Wins
```python
def determine_winner(player_value, dealer_value):
    """Determine winner in Blackjack-style game."""
    if dealer_value > 21:
        return 'player'
    elif player_value > 21:
        return 'dealer'
    elif player_value > dealer_value:
        return 'player'
    elif dealer_value > player_value:
        return 'dealer'
    else:
        return 'tie'
```

**Examples:** Blackjack, Cho-Han

---

## AI and Random Behavior

### Random AI Choice
```python
import random

def computer_move(board):
    """Simple AI: choose random valid move."""
    valid_moves = []
    for position in board:
        if board[position] == EMPTY:
            valid_moves.append(position)
    
    if valid_moves:
        return random.choice(valid_moves)
    return None
```

**Examples:** Tic-Tac-Toe, Four-in-a-Row

### Weighted Random Choice
```python
import random

def choose_action():
    """AI with weighted probabilities."""
    actions = ['attack', 'defend', 'heal']
    weights = [50, 30, 20]  # 50% attack, 30% defend, 20% heal
    
    return random.choices(actions, weights=weights)[0]
```

### Simple Heuristic AI
```python
def smart_move(board):
    """AI that looks for winning moves."""
    # First, check if AI can win
    for position in get_empty_positions(board):
        board[position] = AI_PIECE
        if check_winner(board) == AI_PIECE:
            return position
        board[position] = EMPTY
    
    # Second, block player from winning
    for position in get_empty_positions(board):
        board[position] = PLAYER_PIECE
        if check_winner(board) == PLAYER_PIECE:
            board[position] = AI_PIECE
            return position
        board[position] = EMPTY
    
    # Otherwise, random move
    return random.choice(get_empty_positions(board))
```

**Examples:** Tic-Tac-Toe (advanced version)

---

## Turn-Based Games

### Player Alternation
```python
def main():
    current_player = 'X'
    
    while not game_over():
        display_board()
        print(f"Player {current_player}'s turn")
        
        move = get_move(current_player)
        make_move(move, current_player)
        
        if check_winner() == current_player:
            print(f"Player {current_player} wins!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'
```

**Examples:** Tic-Tac-Toe, Four-in-a-Row

### Player vs Computer
```python
PLAYER_TURN = 'player'
COMPUTER_TURN = 'computer'

def main():
    turn = PLAYER_TURN
    
    while not game_over():
        if turn == PLAYER_TURN:
            move = get_player_move()
        else:
            move = get_computer_move()
        
        apply_move(move, turn)
        
        # Switch turns
        turn = COMPUTER_TURN if turn == PLAYER_TURN else PLAYER_TURN
```

---

## Betting and Score Systems

### Money Management
```python
def main():
    money = 5000  # Starting money
    
    while True:
        if money <= 0:
            print("You're broke!")
            sys.exit()
        
        print(f'Money: ${money}')
        bet = get_bet(money)
        
        # Play round
        result = play_round()
        
        if result == 'win':
            print(f'You won ${bet}!')
            money += bet
        elif result == 'lose':
            print(f'You lost ${bet}!')
            money -= bet
        else:  # tie
            print('Push! Bet returned.')
```

**Examples:** Blackjack, Cho-Han

### Score Tracking
```python
def main():
    high_score = 0
    
    while True:
        score = play_game()
        
        print(f'Your score: {score}')
        
        if score > high_score:
            high_score = score
            print(f'New high score: {high_score}!')
        else:
            print(f'High score: {high_score}')
        
        if not play_again():
            break
```

**Examples:** 2048, Sliding Tile Puzzle

### Lives System
```python
def main():
    lives = 3
    score = 0
    
    while lives > 0:
        print(f'Lives: {lives} | Score: {score}')
        
        result = play_round()
        
        if result == 'success':
            score += 100
        else:
            lives -= 1
            print('Lost a life!')
    
    print(f'Game Over! Final score: {score}')
```

---

## Common Helper Functions

### Display Board
```python
def display_board(board):
    """Display game board with borders."""
    print('\n+---+---+---+')
    for row in range(3):
        print('|', end='')
        for col in range(3):
            print(f' {board[row][col]} |', end='')
        print('\n+---+---+---+')
```

### Clear Screen
```python
def clear_screen():
    """Clear the terminal screen."""
    print('\n' * 50)  # Simple method
    
    # Or use OS-specific commands:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
```

### Pause for Player
```python
def wait_for_player():
    """Pause until player presses Enter."""
    input('Press Enter to continue...')
```

---

## Complete Game Template

```python
#!/usr/bin/env python3
"""
Game Name - Your Description
"""

import random
import sys

# Constants
PLAYER_WINS = 'player'
COMPUTER_WINS = 'computer'
TIE = 'tie'

def main():
    """Main game loop."""
    print("Welcome to the Game!")
    print("=" * 40)
    
    while True:  # Main game loop
        # Set up round
        game_state = setup_game()
        
        # Play round
        while not is_round_over(game_state):
            display_game(game_state)
            player_move = get_player_move(game_state)
            update_game(game_state, player_move)
        
        # Determine winner
        winner = get_winner(game_state)
        display_results(winner)
        
        # Play again?
        if not play_again():
            break
    
    print("Thanks for playing!")

def setup_game():
    """Initialize game state."""
    return {
        'score': 0,
        'round': 1
    }

def display_game(state):
    """Show current game state."""
    print(f"\nRound {state['round']}")
    print(f"Score: {state['score']}")

def get_player_move(state):
    """Get validated player input."""
    while True:
        move = input('Your move: ').upper().strip()
        if is_valid_move(move, state):
            return move
        print("Invalid move. Try again.")

def is_valid_move(move, state):
    """Check if move is legal."""
    # Implement validation logic
    return True

def update_game(state, move):
    """Apply move to game state."""
    # Implement game logic
    pass

def is_round_over(state):
    """Check if round is finished."""
    # Implement win/lose condition
    return False

def get_winner(state):
    """Determine round winner."""
    # Implement winner logic
    return PLAYER_WINS

def display_results(winner):
    """Show round results."""
    if winner == PLAYER_WINS:
        print("You win!")
    elif winner == COMPUTER_WINS:
        print("Computer wins!")
    else:
        print("It's a tie!")

def play_again():
    """Ask to play another round."""
    response = input('Play again? (yes or no): ').lower()
    return response.startswith('y')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit()
```

---

## Tips for Game Development

1. **Start Simple** - Get basic gameplay working before adding features
2. **Use Constants** - Define magic numbers as named constants at the top
3. **Validate Input** - Always validate and sanitize user input
4. **Handle Exit Gracefully** - Catch KeyboardInterrupt (Ctrl+C)
5. **Test Edge Cases** - What happens when the board is full? When there's no valid move?
6. **Add Quit Option** - Let players type "QUIT" to exit
7. **Clear Instructions** - Tell players what inputs are valid
8. **Save High Scores** - Consider persisting scores to a file

---

## Related Projects

- **Simple Games:** Guessthenumber, Cho-Han, Rock Paper Scissors
- **Board Games:** Tic-Tac-Toe, Four-in-a-Row, Mancala
- **Card Games:** Blackjack
- **Logic Puzzles:** Bagels, Hangman, Sudoku
- **Advanced:** 2048, Tower of Hanoi, Water Bucket

---

## Additional Resources

- **PROJECTS_OVERVIEW.md** - Full list of all game projects
- **dictionary_coordinates.md** - Using (x,y) tuples for boards
- **random_generation.md** - Random number patterns

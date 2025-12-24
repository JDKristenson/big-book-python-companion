# Random Generation - Quick Reference

Common patterns for randomness in Python games and simulations.

## Table of Contents
- [Basic Random Operations](#basic-random-operations)
- [Random Choices](#random-choices)
- [Random Sequences](#random-sequences)
- [Weighted Randomness](#weighted-randomness)
- [Random Text Generation](#random-text-generation)
- [Game-Specific Patterns](#game-specific-patterns)

---

## Basic Random Operations

### Import Random Module
```python
import random
```

### Random Integers
```python
# Random int from 1 to 6 (inclusive)
die_roll = random.randint(1, 6)

# Random int from 0 to 9
digit = random.randint(0, 9)

# Random even number from 0 to 100
even_num = random.randrange(0, 101, 2)
```

**Projects Using This:** Cho-Han, Dice Roller, Snail Race

### Random Floats
```python
# Random float from 0.0 to 1.0
probability = random.random()

# Random float in a range
temperature = random.uniform(20.0, 30.0)
```

**Projects Using This:** Forest Fire Sim, Birthday Paradox

---

## Random Choices

### Pick Random Element
```python
# Choose one item from list
colors = ['red', 'green', 'blue']
color = random.choice(colors)

# Choose from string
letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Choose from dictionary keys
player_pos = random.choice(list(valid_positions.keys()))
```

**Examples:**
```python
# Random direction
directions = ['north', 'south', 'east', 'west']
move = random.choice(directions)

# Random response
responses = ['Yes', 'No', 'Maybe', 'Ask again later']
answer = random.choice(responses)
```

**Projects Using This:** Magic Fortune Ball, Rock Paper Scissors

### Pick Multiple Random Elements
```python
# Choose 5 unique items
cards = random.sample(deck, 5)

# Can't pick more items than available
lottery_numbers = random.sample(range(1, 50), 6)
```

**Projects Using This:** Blackjack (dealing cards), Powerball

### Pick With Replacement
```python
# Can pick same item multiple times
choices = random.choices(['A', 'B', 'C'], k=10)
# Might get ['A', 'A', 'B', 'C', 'A', 'C', ...]
```

---

## Random Sequences

### Shuffle List
```python
# Shuffle in place
deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
random.shuffle(deck)

# Create shuffled copy
import random
original = [1, 2, 3, 4, 5]
shuffled = random.sample(original, len(original))
```

**Example: Shuffle Deck of Cards**
```python
def get_deck():
    """Create and shuffle a deck of cards."""
    deck = []
    for suit in ['♥', '♦', '♠', '♣']:
        for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck
```

**Projects Using This:** Blackjack, Three-Card Monte

### Generate Random Sequence
```python
# Random list of integers
numbers = [random.randint(1, 100) for _ in range(10)]

# Random string
import string
random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
# Example: 'X3K9P2M7'
```

---

## Weighted Randomness

### Weighted Choice
```python
# Choose with different probabilities
outcomes = ['common', 'uncommon', 'rare', 'legendary']
weights = [70, 20, 9, 1]  # Percentages

result = random.choices(outcomes, weights=weights, k=1)[0]
```

**Example: Loot Drop System**
```python
def get_loot():
    """Generate random loot with rarities."""
    items = ['Gold Coin', 'Magic Sword', 'Dragon Egg', 'Legendary Armor']
    weights = [50, 30, 15, 5]
    return random.choices(items, weights=weights, k=1)[0]
```

### Probability-Based Events
```python
# 25% chance of event happening
if random.random() < 0.25:
    print("Event triggered!")

# More readable with percentage
def chance(percent):
    """Return True percent% of the time."""
    return random.randint(1, 100) <= percent

if chance(75):
    print("75% chance event!")
```

**Example from Forest Fire Sim:**
```python
TREE_GROWTH_CHANCE = 0.01
FIRE_SPREAD_CHANCE = 0.10

# Grow new tree
if random.random() < TREE_GROWTH_CHANCE:
    forest[(x, y)] = TREE

# Spread fire
if random.random() < FIRE_SPREAD_CHANCE:
    forest[(x, y)] = FIRE
```

**Projects Using This:** Forest Fire Sim, Snail Race

---

## Random Text Generation

### Random Words
```python
# Generate random sentence
subjects = ['The cat', 'A dog', 'My friend']
verbs = ['runs', 'jumps', 'sleeps']
objects = ['quickly', 'loudly', 'peacefully']

sentence = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."
# "The cat jumps loudly."
```

**Example: Clickbait Generator**
```python
templates = [
    "You won't believe what {noun} did!",
    "{number} reasons why {noun} is amazing!",
    "This {adjective} {noun} will change your life!"
]

nouns = ['cat', 'teacher', 'robot']
adjectives = ['weird', 'shocking', 'incredible']

headline = random.choice(templates).format(
    noun=random.choice(nouns),
    adjective=random.choice(adjectives),
    number=random.randint(5, 20)
)
```

**Projects Using This:** Clickbait Generator, J'ACCUSE!

### Random Names
```python
first_names = ['Alice', 'Bob', 'Charlie', 'Diana']
last_names = ['Smith', 'Jones', 'Williams', 'Brown']

full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
```

---

## Game-Specific Patterns

### Random Player Starting Positions
```python
def get_random_position(width, height):
    """Get random position on grid."""
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return (x, y)

# Ensure position is valid (not a wall)
while True:
    pos = get_random_position(WIDTH, HEIGHT)
    if grid[pos] != WALL:
        break
```

### Random AI Behavior
```python
def ai_move(valid_moves):
    """AI chooses random valid move."""
    if not valid_moves:
        return None
    return random.choice(valid_moves)

# Smarter AI with weighted preferences
def smart_ai_move(valid_moves, preferences):
    """AI prefers certain moves."""
    if not valid_moves:
        return None
    
    # Weight moves by preference
    weights = [preferences.get(move, 1) for move in valid_moves]
    return random.choices(valid_moves, weights=weights, k=1)[0]
```

**Projects Using This:** Tic-Tac-Toe, Four-in-a-Row

### Random Maze Generation
```python
def generate_random_maze(width, height):
    """Create maze with random walls."""
    maze = {}
    for x in range(width):
        for y in range(height):
            # 30% chance of wall
            if random.random() < 0.3:
                maze[(x, y)] = '#'
            else:
                maze[(x, y)] = ' '
    return maze
```

### Random Enemy Placement
```python
def place_enemies(grid, num_enemies):
    """Place enemies in random empty positions."""
    empty_cells = [(x, y) for (x, y), val in grid.items() if val == ' ']
    enemy_positions = random.sample(empty_cells, min(num_enemies, len(empty_cells)))
    
    for pos in enemy_positions:
        grid[pos] = 'E'  # Enemy
```

**Projects Using This:** Hungry Robots

---

## Dice Rolling Patterns

### Single Die
```python
def roll_die(sides=6):
    """Roll a die with specified sides."""
    return random.randint(1, sides)

# Standard dice
d6 = roll_die(6)
d20 = roll_die(20)
```

### Multiple Dice
```python
def roll_dice(num_dice, sides=6):
    """Roll multiple dice and return results."""
    return [random.randint(1, sides) for _ in range(num_dice)]

# Roll 3 six-sided dice
rolls = roll_dice(3, 6)  # [4, 2, 6]
total = sum(rolls)  # 12
```

### Dice with Advantage/Disadvantage
```python
def roll_with_advantage():
    """Roll twice, take higher (D&D style)."""
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20)
    return max(roll1, roll2)

def roll_with_disadvantage():
    """Roll twice, take lower."""
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20)
    return min(roll1, roll2)
```

**Projects Using This:** Dice Roller, Dice Math

---

## Card Game Patterns

### Create and Shuffle Deck
```python
def create_deck():
    """Create standard 52-card deck."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    
    random.shuffle(deck)
    return deck

# Deal cards
deck = create_deck()
player_hand = [deck.pop() for _ in range(5)]
```

### Draw Random Card Without Replacement
```python
def draw_card(deck):
    """Draw card from deck."""
    if deck:
        return deck.pop()
    return None
```

**Projects Using This:** Blackjack, Three-Card Monte

---

## Simulation Patterns

### Random Walk
```python
def random_walk_2d(start_pos, steps):
    """Perform 2D random walk."""
    x, y = start_pos
    path = [(x, y)]
    
    for _ in range(steps):
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        path.append((x, y))
    
    return path
```

### Monte Carlo Simulation
```python
def monte_carlo_simulation(trials):
    """Run simulation many times to estimate probability."""
    successes = 0
    
    for _ in range(trials):
        # Run one trial
        if random.random() < 0.5:  # 50% chance
            successes += 1
    
    probability = successes / trials
    return probability

# Example: Birthday Paradox
def birthday_simulation(people, trials):
    """Estimate probability of shared birthday."""
    matches = 0
    
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(people)]
        if len(birthdays) != len(set(birthdays)):
            matches += 1
    
    return matches / trials
```

**Projects Using This:** Birthday Paradox, Monty Hall Problem, Million Dice Roll

---

## Random Number Generation Utilities

### Seeding (Reproducible Random)
```python
# Set seed for reproducible results
random.seed(42)
print(random.randint(1, 100))  # Always same result with same seed

# Reset to truly random
import time
random.seed(time.time())
```

### Random Without Duplicates
```python
def random_unique_numbers(count, min_val, max_val):
    """Generate unique random numbers."""
    if count > (max_val - min_val + 1):
        raise ValueError("Can't generate that many unique numbers")
    
    return random.sample(range(min_val, max_val + 1), count)

# Example: Lottery numbers
lottery = random_unique_numbers(6, 1, 49)
```

**Projects Using This:** Powerball, Bagels

### Random Boolean
```python
# Simple coin flip
coin = random.choice([True, False])

# More readable
def coin_flip():
    """Return heads (True) or tails (False)."""
    return random.random() < 0.5
```

---

## Common Gotchas and Tips

### 1. Don't Forget to Import
```python
import random  # Always needed!
```

### 2. Inclusive vs Exclusive
```python
# randint is INCLUSIVE on both ends
random.randint(1, 6)  # Can return 1, 2, 3, 4, 5, or 6

# randrange is EXCLUSIVE on upper bound
random.randrange(1, 6)  # Can return 1, 2, 3, 4, or 5 (NOT 6)
```

### 3. Modifying Lists While Shuffling
```python
# WRONG - shuffles in place
original = [1, 2, 3]
deck = original
random.shuffle(deck)  # original is also shuffled!

# CORRECT - make a copy first
original = [1, 2, 3]
deck = original.copy()
random.shuffle(deck)  # original unchanged
```

### 4. Empty Sequence Error
```python
# WRONG - error if list is empty
choice = random.choice([])  # IndexError!

# CORRECT - check first
if my_list:
    choice = random.choice(my_list)
else:
    choice = None
```

### 5. Random Is Not Cryptographically Secure
```python
# For games and simulations, random is fine
game_number = random.randint(1, 100)

# For security/cryptography, use secrets module
import secrets
secure_token = secrets.token_hex(16)
```

---

## Complete Examples

### Random Dungeon Generator
```python
def generate_dungeon(width, height):
    """Generate random dungeon layout."""
    dungeon = {}
    
    for x in range(width):
        for y in range(height):
            # 70% floor, 20% wall, 10% treasure
            roll = random.random()
            if roll < 0.70:
                dungeon[(x, y)] = '.'  # Floor
            elif roll < 0.90:
                dungeon[(x, y)] = '#'  # Wall
            else:
                dungeon[(x, y)] = '$'  # Treasure
    
    return dungeon
```

### Random Event System
```python
class RandomEventSystem:
    def __init__(self):
        self.events = {
            'treasure': {'weight': 10, 'message': 'You found treasure!'},
            'monster': {'weight': 30, 'message': 'A monster appears!'},
            'trap': {'weight': 20, 'message': 'You triggered a trap!'},
            'nothing': {'weight': 40, 'message': 'Nothing happens.'}
        }
    
    def trigger_event(self):
        """Trigger weighted random event."""
        events = list(self.events.keys())
        weights = [self.events[e]['weight'] for e in events]
        
        event = random.choices(events, weights=weights, k=1)[0]
        return self.events[event]['message']
```

---

## Related Projects

- **Dice Games:** Cho-Han, Dice Math, Dice Roller, Lucky Stars
- **Card Games:** Blackjack, Three-Card Monte
- **Simulations:** Birthday Paradox, Million Dice Roll, Monty Hall, Forest Fire
- **Text Generation:** Clickbait Generator, J'ACCUSE!
- **Board Games:** Snail Race, Mancala (dice for starting)

---

## Additional Resources

- **game_development_patterns.md** - Using randomness in games
- **string_manipulation.md** - Random text generation
- **PROJECTS_OVERVIEW.md** - All projects using random generation

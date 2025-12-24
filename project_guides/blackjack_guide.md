# Blackjack - Project Guide

**Project #4 from The Big Book of Small Python Projects**

## Overview

Blackjack (also known as 21) is a classic card game where players try to get as close to 21 as possible without going over. This project implements a fully-featured Blackjack game with betting, doubling down, and proper dealer behavior.

**Difficulty:** Large project (200+ lines)  
**Concepts:** Card games, game state, dictionaries, tuples, game loops  
**Book Chapter:** https://inventwithpython.com/bigbookpython/project4.html

---

## What You'll Learn

- **Card representation** using tuples
- **Hand evaluation** with special ace handling
- **Betting systems** and money management
- **Game state** tracking across multiple rounds
- **Input validation** for player moves
- **Dealer AI** following house rules

---

## How to Run

```bash
python project_runner.py --run blackjack
# or
python book_resources/blackjack.py
```

---

## Code Walkthrough

### 1. Card Representation

Cards are represented as tuples with (rank, suit):

```python
HEARTS   = chr(9829)  # ♥
DIAMONDS = chr(9830)  # ♦
SPADES   = chr(9824)  # ♠
CLUBS    = chr(9827)  # ♣

# Example cards
card1 = ('A', HEARTS)   # Ace of Hearts
card2 = ('K', SPADES)   # King of Spades
card3 = ('7', DIAMONDS) # 7 of Diamonds
```

**Why tuples?** Immutable and can be easily unpacked: `rank, suit = card`

### 2. Creating and Shuffling the Deck

```python
def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Number cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  # Face cards and Ace
    random.shuffle(deck)
    return deck
```

**Key Points:**
- Uses `range(2, 11)` for cards 2-10
- Converts numbers to strings for consistency
- Shuffles in place with `random.shuffle()`
- Returns ready-to-use deck

### 3. Hand Value Calculation

The trickiest part is handling Aces (worth 1 or 11):

```python
def getHandValue(cards):
    """Returns the value of the cards."""
    value = 0
    numberOfAces = 0
    
    # Add the value for the non-ace cards
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
    
    # Add the value for the aces
    value += numberOfAces  # Start by counting each ace as 1
    for i in range(numberOfAces):
        # If another 10 can be added without busting, do so
        if value + 10 <= 21:
            value += 10
    
    return value
```

**Why this works:**
1. Count all aces initially as 1
2. Try to make each ace worth 11 if it doesn't cause a bust
3. Automatically handles multiple aces correctly

**Example:**
- Hand: A, A, 9 → 1 + 1 + 9 = 11, can add 10 → **21** (perfect!)
- Hand: A, A, A, 8 → 1 + 1 + 1 + 8 = 11, can add 10 → **21**
- Hand: A, K → 1 + 10 = 11, can add 10 → **21** (Blackjack!)

### 4. Player Move Input

```python
def getMove(playerHand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for
    stand, and 'D' for double down."""
    while True:
        # Determine valid moves
        moves = ['(H)it', '(S)tand']
        
        # Can only double down on first move with enough money
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        
        # Get input
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper().strip()
        
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move
```

**Smart validation:**
- Only shows valid options
- Double down only available on first move
- Requires enough money to double
- Keeps asking until valid input

### 5. Game Loop Structure

```python
def main():
    money = 5000
    
    while True:  # Main game loop
        # Check if broke
        if money <= 0:
            print("You're broke!")
            sys.exit()
        
        # Get bet
        bet = getBet(money)
        
        # Deal cards
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        
        # Player's turn
        while True:
            displayHands(playerHand, dealerHand, False)
            
            if getHandValue(playerHand) > 21:
                break  # Player busted
            
            move = getMove(playerHand, money - bet)
            
            if move == 'D':
                additionalBet = getBet(min(bet, money - bet))
                bet += additionalBet
            
            if move in ('H', 'D'):
                playerHand.append(deck.pop())
                
                if getHandValue(playerHand) > 21:
                    continue
            
            if move in ('S', 'D'):
                break  # Player stands
        
        # Dealer's turn (if player didn't bust)
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                
                if getHandValue(dealerHand) > 21:
                    break
                input('Press Enter to continue...')
        
        # Determine winner and adjust money
        # [winner determination code]
```

---

## Key Concepts Explained

### Why Hide Dealer's First Card?

```python
def displayHands(playerHand, dealerHand, showDealerHand):
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        displayCards([BACKSIDE] + dealerHand[1:])  # Hide first card
```

This follows real Blackjack rules - player makes decisions without knowing dealer's full hand.

### Dealer AI (House Rules)

```python
while getHandValue(dealerHand) < 17:
    dealerHand.append(deck.pop())
```

**The dealer must:**
- Hit on 16 or less
- Stand on 17 or more
- No choices - completely automatic

This is standard casino rules and makes the game fair.

### Double Down Feature

```python
if move == 'D':
    additionalBet = getBet(min(bet, (money - bet)))
    bet += additionalBet
    print('Bet increased to {}.'.format(bet))
```

**Double down rules:**
- Can only do on first turn (2 cards)
- Can bet up to original bet amount
- Must hit exactly once more
- Increases risk and reward

---

## Common Pitfalls

### 1. Forgetting to Handle Aces

❌ **Wrong:** Treating aces as always 11 or always 1

✅ **Right:** Dynamic ace value based on current hand

### 2. Not Checking for Bust After Each Card

❌ **Wrong:** Only checking at end of turn

✅ **Right:** Check after each hit to end turn immediately

### 3. Dealer Hitting After Player Busts

❌ **Wrong:** Dealer plays even when player already lost

✅ **Right:** Skip dealer turn if player busted

```python
if getHandValue(playerHand) <= 21:
    # Only then does dealer play
```

### 4. Allowing Invalid Moves

❌ **Wrong:** Letting player double down any time

✅ **Right:** Only on first move with 2 cards

---

## Modifications to Try

### Easy Modifications

1. **Change starting money**
   ```python
   money = 10000  # Start with more
   ```

2. **Adjust minimum bet**
   ```python
   def getBet(maxBet):
       # Change minimum from 1 to 5
       if 5 <= bet <= maxBet:
           return bet
   ```

3. **Add card counting hints**
   ```python
   def countHighCards(deck):
       return sum(1 for rank, suit in deck if rank in ('10', 'J', 'Q', 'K', 'A'))
   ```

### Intermediate Modifications

1. **Add insurance bet**
   - When dealer shows an Ace, offer insurance
   - Pays 2:1 if dealer has Blackjack

2. **Track wins/losses statistics**
   ```python
   stats = {'wins': 0, 'losses': 0, 'pushes': 0}
   ```

3. **Multiple hands (split pairs)**
   - If dealt matching cards, can split into two hands
   - Play each hand separately

### Advanced Modifications

1. **Add surrender option**
   - Forfeit half the bet and end hand immediately
   - Only available as first move

2. **Multi-deck shoe**
   - Use 6 decks shuffled together
   - More realistic casino experience

3. **Basic strategy advisor**
   - Show optimal move based on probability
   - Teaching tool for learning Blackjack strategy

---

## Testing Your Understanding

Try to answer these without looking at the code:

1. Why are cards stored as tuples instead of strings?
2. How does the ace value calculation prevent busting unnecessarily?
3. Why does the dealer HAVE to hit on 16?
4. What happens if both player and dealer have 21?

**Answers:**
1. Tuples are immutable and easily unpacked into rank and suit
2. Aces start at 1, only become 11 if it doesn't cause bust
3. House rules - standardizes gameplay and sets the house edge
4. It's a "push" (tie) - bet is returned to player

---

## Related Projects

- **Cho-Han** - Simpler betting game with dice
- **Three-Card Monte** - Another card game with visual elements
- **Royal Game of Ur** - Complex board game with similar turn structure

---

## Going Further

### Study Topics
- Probability in Blackjack
- Card counting techniques (for learning, not cheating!)
- Optimal Blackjack strategy charts
- House edge calculation

### Code Challenges
1. Add save/load game state
2. Implement tournament mode
3. Create AI player that learns from games
4. Add graphical card display using ASCII art
5. Track and display playing statistics

---

## Quick Reference

**Run the game:**
```bash
python book_resources/blackjack.py
```

**Key functions:**
- `getDeck()` - Creates shuffled deck
- `getHandValue(cards)` - Calculates hand value
- `getBet(maxBet)` - Gets player bet
- `getMove(hand, money)` - Gets player action
- `displayHands()` - Shows cards

**Game flow:**
1. Place bet
2. Deal 2 cards to player and dealer
3. Player decides: Hit, Stand, or Double Down
4. Dealer plays (hits until 17+)
5. Compare hands, adjust money
6. Repeat

---

## Resources

- **Book chapter:** https://inventwithpython.com/bigbookpython/project4.html
- **Quick references:**
  - game_development_patterns.md - Game loops and input validation
  - random_generation.md - Shuffling and dealing
  - string_manipulation.md - Card display formatting

# Conway's Game of Life - Project Guide

**Project #13 from The Big Book of Small Python Projects**

## Overview

Conway's Game of Life is a cellular automaton where simple rules create complex, emergent patterns. Cells on a grid live, die, or reproduce based on their neighbors, creating mesmerizing patterns that can evolve indefinitely.

**Difficulty:** Short project (~90 lines)  
**Concepts:** Cellular automata, 2D grids, dictionaries with tuple keys, simulation  
**Book Chapter:** https://inventwithpython.com/bigbookpython/project13.html

---

## What You'll Learn

- **Dictionary coordinates** using (x, y) tuple keys
- **Cellular automata** rules and behavior
- **Double buffering** to prevent state corruption
- **Grid wrapping** for toroidal topology
- **Emergent complexity** from simple rules
- **Animation** with time delays

---

## How to Run

```bash
python project_runner.py --run conwaysgameoflife
# or
python book_resources/conwaysgameoflife.py
```

Press Ctrl+C to stop the simulation.

---

## The Rules

Conway's Game of Life has beautifully simple rules:

1. **Survival:** Live cell with 2 or 3 neighbors stays alive
2. **Death:** Live cell with < 2 or > 3 neighbors dies
3. **Birth:** Dead cell with exactly 3 neighbors becomes alive

That's it! Yet these rules create incredible patterns.

---

## Code Walkthrough

### 1. Grid Representation

Uses dictionary with (x, y) tuple keys:

```python
WIDTH = 79
HEIGHT = 20

ALIVE = 'O'
DEAD = ' '

# Initialize with random cells
nextCells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD
```

**Why dictionary coordinates?**
- Natural (x, y) indexing
- Easy neighbor checking
- Efficient for sparse grids
- Wrapping edges is simple

### 2. Displaying the Grid

```python
# Print cells on the screen
for y in range(HEIGHT):
    for x in range(WIDTH):
        print(cells[(x, y)], end='')
    print()  # Newline at end of row
```

**Key points:**
- Nested loops: outer for Y (rows), inner for X (columns)
- `end=''` prevents automatic newline after each cell
- Manual `print()` after each row

### 3. Counting Neighbors

The core of the simulation:

```python
# Get neighboring coordinates (with wrapping)
left = (x - 1) % WIDTH
right = (x + 1) % WIDTH
above = (y - 1) % HEIGHT
below = (y + 1) % HEIGHT

# Count living neighbors
numNeighbors = 0
if cells[(left, above)] == ALIVE:
    numNeighbors += 1
if cells[(x, above)] == ALIVE:
    numNeighbors += 1
if cells[(right, above)] == ALIVE:
    numNeighbors += 1
# ... check all 8 neighbors
```

**Why use modulo (%) for wrapping?**
```python
# At x=0, left edge:
left = (0 - 1) % 79  # = 78 (wraps to right edge)

# At x=78, right edge:
right = (78 + 1) % 79  # = 0 (wraps to left edge)
```

This creates a toroidal (donut-shaped) grid where edges connect.

### 4. Applying the Rules

```python
# Set cell based on Conway's Game of Life rules
if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
    # Living cells with 2 or 3 neighbors stay alive
    nextCells[(x, y)] = ALIVE
elif cells[(x, y)] == DEAD and numNeighbors == 3:
    # Dead cells with 3 neighbors become alive
    nextCells[(x, y)] = ALIVE
else:
    # Everything else dies or stays dead
    nextCells[(x, y)] = DEAD
```

**Why so clear?** Each rule is explicitly stated, making the logic obvious.

### 5. Double Buffering

**Critical concept:**

```python
while True:
    cells = copy.deepcopy(nextCells)  # Copy current state
    
    # Display current state
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')
        print()
    
    # Calculate next state
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Calculate based on cells, store in nextCells
            numNeighbors = countNeighbors(cells, x, y)
            nextCells[(x, y)] = applyRules(cells, x, y, numNeighbors)
```

**Why is this necessary?**

❌ **Without double buffering:**
```python
# BAD - modifying while reading
for x in range(WIDTH):
    for y in range(HEIGHT):
        if shouldDie(x, y):
            cells[(x, y)] = DEAD  # Changes affect later cells!
```

✅ **With double buffering:**
- Read from `cells` (current generation)
- Write to `nextCells` (next generation)
- After full calculation, swap them
- Ensures all cells update simultaneously

---

## Key Concepts Explained

### Cellular Automata

A **cellular automaton** is:
- Grid of cells
- Each cell has a state (alive/dead)
- State changes based on neighbors
- All cells update simultaneously
- Simple rules → complex behavior

**Examples of patterns:**
- **Still lifes:** Don't change (block, beehive)
- **Oscillators:** Repeat after N steps (blinker, toad)
- **Spaceships:** Move across grid (glider, lightweight spaceship)
- **Methuselahs:** Take many generations to stabilize

### Emergent Behavior

The Game of Life demonstrates **emergence**:
- Simple local rules
- No central control
- Complex global patterns emerge
- Unpredictable long-term behavior

This is similar to:
- Flocking birds
- Traffic jams
- Economic markets
- Evolution itself

### Toroidal Topology

The grid wraps around like a donut:

```
Top edge connects to bottom:
   ↓
[Grid]
   ↑

Left edge connects to right:
→ [Grid] →
```

This means:
- No special edge cases
- Patterns can move indefinitely
- Mathematical simplicity

---

## Common Patterns to Try

### Still Lifes (Never Change)

**Block:**
```
OO
OO
```

**Beehive:**
```
 OO
O  O
 OO
```

### Oscillators (Repeat)

**Blinker (period 2):**
```
Generation 1:    Generation 2:
   O                
   O             OOO
   O                
```

**Toad (period 2):**
```
Generation 1:    Generation 2:
 OOO             O
OOO               OOO
                   O
```

### Spaceships (Move)

**Glider (moves diagonally):**
```
 O
  O
OOO
```

After 4 generations, moved one cell diagonally!

---

## Common Pitfalls

### 1. Not Using Double Buffering

❌ **Wrong:** Modifying grid while reading it
```python
if should_die:
    cells[(x, y)] = DEAD  # Affects neighbor counts!
```

✅ **Right:** Read from one, write to another
```python
nextCells[(x, y)] = calculate_next_state(cells, x, y)
```

### 2. Forgetting Edge Wrapping

❌ **Wrong:** Crash at edges
```python
neighbor = cells[(x + 1, y)]  # Error when x = WIDTH-1!
```

✅ **Right:** Use modulo for wrapping
```python
neighbor = cells[((x + 1) % WIDTH, y)]
```

### 3. Counting Center Cell as Neighbor

❌ **Wrong:** Cell is its own neighbor
```python
for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
        count += 1  # Counts center!
```

✅ **Right:** Skip center cell
```python
for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
        if dx == 0 and dy == 0:
            continue
        count += 1
```

### 4. Wrong Coordinate Order

❌ **Wrong:** Mixing up x and y
```python
for x in range(HEIGHT):  # Wrong!
    for y in range(WIDTH):  # Wrong!
        cells[(x, y)] = ...
```

✅ **Right:** X is width, Y is height
```python
for x in range(WIDTH):
    for y in range(HEIGHT):
        cells[(x, y)] = ...
```

---

## Modifications to Try

### Easy Modifications

1. **Change cell characters**
   ```python
   ALIVE = '█'  # Solid block
   DEAD = '░'   # Light shade
   ```

2. **Adjust grid size**
   ```python
   WIDTH = 120  # Wider
   HEIGHT = 30  # Taller
   ```

3. **Change animation speed**
   ```python
   time.sleep(0.5)  # Slower (0.5 seconds per generation)
   time.sleep(0.05) # Faster
   ```

### Intermediate Modifications

1. **Add generation counter**
   ```python
   generation = 0
   while True:
       generation += 1
       print(f'Generation: {generation}')
       # ... rest of loop
   ```

2. **Track population**
   ```python
   alive_count = sum(1 for cell in cells.values() if cell == ALIVE)
   print(f'Population: {alive_count}')
   ```

3. **Different starting patterns**
   ```python
   # Glider
   cells[(5, 5)] = ALIVE
   cells[(6, 6)] = ALIVE
   cells[(4, 7)] = ALIVE
   cells[(5, 7)] = ALIVE
   cells[(6, 7)] = ALIVE
   ```

### Advanced Modifications

1. **Color based on age**
   - New cells are bright
   - Old cells fade over time
   - Use ANSI color codes

2. **Multiple states**
   - Not just alive/dead
   - Different species that interact
   - Predator-prey dynamics

3. **Different rules**
   - HighLife (B36/S23)
   - Day & Night (B3678/S34678)
   - Seeds (B2/S)

4. **Pattern detection**
   - Detect when pattern stabilizes
   - Identify known patterns (gliders, etc.)
   - Stop when nothing changes

---

## Understanding Check

Answer these questions:

1. Why is double buffering necessary?
2. What happens to a cell with 1 neighbor?
3. What happens to a cell with 4 neighbors?
4. Why does the grid wrap around?
5. What makes the glider pattern special?

**Answers:**
1. Ensures all cells update simultaneously, not sequentially
2. Dies from loneliness (underpopulation)
3. Dies from overcrowding (overpopulation)
4. Avoids edge cases and creates toroidal topology
5. It moves across the grid over time

---

## Experiments to Try

1. **R-pentomino**
   - Start with this pattern:
     ```
      OO
     OO
      O
     ```
   - Takes over 1100 generations to stabilize!

2. **Acorn**
   - Tiny pattern that produces 633 cells
   - One of the smallest "methuselahs"

3. **Gosper Glider Gun**
   - Produces infinite stream of gliders
   - First discovered pattern to grow infinitely

4. **All dead start**
   - What happens?
   - How quickly does it occur?

5. **All alive start**
   - Watch population crash
   - What patterns emerge?

---

## Going Further

### Study Topics
- Other cellular automata (Langton's Ant, Rule 30)
- Turing completeness in Game of Life
- Universal constructor patterns
- Life-like cellular automata (B/S notation)

### Code Challenges
1. Implement pattern library that loads famous patterns
2. Add pause/resume and step-forward controls
3. Create pattern editor to draw starting configurations
4. Implement Hashlife algorithm for speed
5. Add 3D Game of Life (26 neighbors instead of 8)

---

## Quick Reference

**Run simulation:**
```bash
python book_resources/conwaysgameoflife.py
```

**Constants to modify:**
```python
WIDTH = 79    # Grid width
HEIGHT = 20   # Grid height
ALIVE = 'O'   # Living cell character
DEAD = ' '    # Dead cell character
```

**Rules:**
- Alive + 2-3 neighbors → stays alive
- Dead + 3 neighbors → becomes alive
- Everything else → dies/stays dead

**Stop simulation:** Press Ctrl+C

---

## Resources

- **Book chapter:** https://inventwithpython.com/bigbookpython/project13.html
- **Quick references:**
  - dictionary_coordinates.md - Grid representation explained
  - terminal_graphics.md - Display and animation techniques
- **Learn more:**
  - Wikipedia: Conway's Game of Life
  - LifeWiki: Comprehensive pattern library
  - Golly: Fast Game of Life simulator

---

## Related Projects

- **Langton's Ant** - Another cellular automaton
- **Forest Fire Sim** - Similar grid-based simulation
- **Hourglass** - Physics simulation on grid

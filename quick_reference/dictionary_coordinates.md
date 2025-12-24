# Dictionary Coordinates - Quick Reference

Using dictionaries with (x, y) tuple keys for 2D grids and game boards.

## Why Use Dictionary Coordinates?

**Advantages:**
- Sparse grids (only store non-empty cells)
- Easy neighbor checking
- Natural coordinate system
- Flexible grid sizes
- Wrapping edges is simple

**Projects Using This Pattern:**
- Conway's Game of Life
- Langton's Ant
- Forest Fire Simulation
- Hourglass
- And many more!

---

## Basic Setup

### Initialize Empty Grid
```python
WIDTH = 10
HEIGHT = 10

# Create empty grid
grid = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        grid[(x, y)] = ' '  # Empty cell
```

### Initialize with Values
```python
import random

# Random alive/dead cells
grid = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            grid[(x, y)] = 'O'  # Alive
        else:
            grid[(x, y)] = ' '  # Dead
```

---

## Accessing Cells

### Basic Access
```python
# Get value at position
cell_value = grid[(5, 3)]

# Set value at position
grid[(5, 3)] = 'X'

# Check if position exists
if (x, y) in grid:
    print(f"Cell ({x}, {y}) exists")
```

### Safe Access with Default
```python
# Get with default value if key doesn't exist
value = grid.get((x, y), ' ')

# Or use setdefault
value = grid.setdefault((x, y), ' ')
```

---

## Displaying Grids

### Simple Display
```python
def display_grid(grid, width, height):
    """Display grid top-to-bottom."""
    for y in range(height):
        for x in range(width):
            print(grid[(x, y)], end='')
        print()  # Newline after each row
```

**Output:**
```
O O    O
  O O O
O   O
  O O O
```

### With Borders
```python
def display_grid_with_border(grid, width, height):
    """Display grid with border."""
    print('+' + '-' * width + '+')
    for y in range(height):
        print('|', end='')
        for x in range(width):
            print(grid[(x, y)], end='')
        print('|')
    print('+' + '-' * width + '+')
```

**Output:**
```
+----------+
|O O    O  |
|  O O O   |
|O   O     |
+----------+
```

### With Coordinates
```python
def display_with_coords(grid, width, height):
    """Display grid with coordinate labels."""
    # Top numbers
    print('  ', end='')
    for x in range(width):
        print(x % 10, end='')
    print()
    
    # Grid with row numbers
    for y in range(height):
        print(f'{y:2}', end='')
        for x in range(width):
            print(grid[(x, y)], end='')
        print()
```

**Output:**
```
  0123456789
 0O O    O
 1  O O O
 2O   O
```

---

## Neighbor Operations

### Get All 8 Neighbors
```python
def get_neighbors(x, y):
    """Return list of all 8 neighbor coordinates."""
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # Skip center cell
            neighbors.append((x + dx, y + dy))
    return neighbors

# Usage
neighbors = get_neighbors(5, 5)
# Returns: [(4,4), (4,5), (4,6), (5,4), (5,6), (6,4), (6,5), (6,6)]
```

### Get 4 Cardinal Neighbors
```python
def get_cardinal_neighbors(x, y):
    """Return 4 orthogonal neighbors (no diagonals)."""
    return [
        (x, y - 1),  # Above
        (x, y + 1),  # Below
        (x - 1, y),  # Left
        (x + 1, y),  # Right
    ]
```

### Count Neighbor Values
```python
def count_neighbors(grid, x, y, value):
    """Count how many neighbors have specific value."""
    count = 0
    for neighbor_x, neighbor_y in get_neighbors(x, y):
        if (neighbor_x, neighbor_y) in grid:
            if grid[(neighbor_x, neighbor_y)] == value:
                count += 1
    return count

# Example: Count living neighbors in Conway's Game of Life
living_neighbors = count_neighbors(grid, x, y, 'O')
```

---

## Edge Handling

### Wrapping Edges (Toroidal Grid)
```python
def get_wrapped_neighbors(x, y, width, height):
    """Get neighbors with wrapping (Pac-Man style)."""
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            
            # Wrap coordinates
            nx = (x + dx) % width
            ny = (y + dy) % height
            neighbors.append((nx, ny))
    return neighbors
```

**Example from Conway's Game of Life:**
```python
# Get neighbor coordinates with wrapping
left = (x - 1) % WIDTH
right = (x + 1) % WIDTH
above = (y - 1) % HEIGHT
below = (y + 1) % HEIGHT

# Count living neighbors
num_neighbors = 0
if cells[(left, above)] == ALIVE:
    num_neighbors += 1
if cells[(x, above)] == ALIVE:
    num_neighbors += 1
# ... etc
```

### Bounded Grid (No Wrapping)
```python
def is_valid_position(x, y, width, height):
    """Check if position is within bounds."""
    return 0 <= x < width and 0 <= y < height

def get_bounded_neighbors(x, y, width, height):
    """Get neighbors, excluding out-of-bounds positions."""
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            
            nx, ny = x + dx, y + dy
            if is_valid_position(nx, ny, width, height):
                neighbors.append((nx, ny))
    return neighbors
```

---

## Common Patterns

### Conway's Game of Life Update
```python
def update_game_of_life(cells, width, height):
    """Calculate next generation."""
    next_cells = {}
    
    for x in range(width):
        for y in range(height):
            # Count living neighbors
            living_neighbors = 0
            for nx, ny in get_neighbors(x, y):
                if cells.get((nx, ny), DEAD) == ALIVE:
                    living_neighbors += 1
            
            # Apply rules
            if cells[(x, y)] == ALIVE:
                # Cell is alive
                if living_neighbors in (2, 3):
                    next_cells[(x, y)] = ALIVE
                else:
                    next_cells[(x, y)] = DEAD
            else:
                # Cell is dead
                if living_neighbors == 3:
                    next_cells[(x, y)] = ALIVE
                else:
                    next_cells[(x, y)] = DEAD
    
    return next_cells
```

### Flood Fill Algorithm
```python
def flood_fill(grid, start_x, start_y, old_value, new_value):
    """Fill connected region with new value."""
    if grid[(start_x, start_y)] != old_value:
        return
    
    # Use stack for iterative approach
    stack = [(start_x, start_y)]
    
    while stack:
        x, y = stack.pop()
        
        if grid[(x, y)] != old_value:
            continue
        
        grid[(x, y)] = new_value
        
        # Add cardinal neighbors to stack
        for nx, ny in get_cardinal_neighbors(x, y):
            if (nx, ny) in grid and grid[(nx, ny)] == old_value:
                stack.append((nx, ny))
```

### Path Finding (Neighbors)
```python
def find_path(grid, start, goal):
    """Simple breadth-first search path finding."""
    from collections import deque
    
    queue = deque([start])
    came_from = {start: None}
    
    while queue:
        current = queue.popleft()
        
        if current == goal:
            break
        
        for neighbor in get_cardinal_neighbors(*current):
            if neighbor not in grid:
                continue
            if grid[neighbor] == '#':  # Wall
                continue
            if neighbor in came_from:
                continue
            
            queue.append(neighbor)
            came_from[neighbor] = current
    
    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    return path
```

---

## Movement and Updates

### Moving Objects
```python
# Object position
player_pos = (5, 5)

# Move player
direction = 'right'
if direction == 'up':
    player_pos = (player_pos[0], player_pos[1] - 1)
elif direction == 'down':
    player_pos = (player_pos[0], player_pos[1] + 1)
elif direction == 'left':
    player_pos = (player_pos[0] - 1, player_pos[1])
elif direction == 'right':
    player_pos = (player_pos[0] + 1, player_pos[1])

# Check collision
if grid[player_pos] == 'WALL':
    print("Can't move there!")
    player_pos = old_pos  # Undo move
```

### Direction Vectors
```python
DIRECTIONS = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0)
}

def move(position, direction):
    """Move position in given direction."""
    dx, dy = DIRECTIONS[direction]
    x, y = position
    return (x + dx, y + dy)

# Usage
player_pos = (5, 5)
player_pos = move(player_pos, 'right')  # (6, 5)
```

---

## Updating Grid State

### Double Buffering
**Problem:** Don't modify grid while reading it for calculations

```python
# WRONG - modifying while reading
for x in range(WIDTH):
    for y in range(HEIGHT):
        if should_change(x, y):
            grid[(x, y)] = new_value  # Changes affect later cells!

# CORRECT - use next_grid
next_grid = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        # Calculate based on current grid
        next_grid[(x, y)] = calculate_new_value(grid, x, y)

# Replace grid
grid = next_grid
```

### Copying Grids
```python
import copy

# Shallow copy (fast, works for simple values)
new_grid = dict(grid)

# Deep copy (needed for nested structures)
new_grid = copy.deepcopy(grid)
```

---

## Sparse Grids

### Only Store Non-Empty Cells
```python
# Instead of this (stores everything):
grid = {}
for x in range(1000):
    for y in range(1000):
        grid[(x, y)] = ' '  # 1 million entries!

# Do this (only store what's needed):
grid = {}
# Only add cells when they have a value
grid[(100, 200)] = 'X'
grid[(100, 201)] = 'O'

# Use .get() with default for missing cells
def get_cell(grid, x, y):
    return grid.get((x, y), ' ')  # Empty if not in dict
```

### Iterating Sparse Grids
```python
# Only process cells that exist
for (x, y), value in grid.items():
    if value == 'X':
        print(f"Found X at ({x}, {y})")

# Get bounding box of non-empty cells
if grid:
    min_x = min(x for x, y in grid.keys())
    max_x = max(x for x, y in grid.keys())
    min_y = min(y for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())
```

---

## Advanced Patterns

### Distance Calculations
```python
def manhattan_distance(pos1, pos2):
    """Distance in cardinal moves only."""
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)

def euclidean_distance(pos1, pos2):
    """Straight-line distance."""
    x1, y1 = pos1
    x2, y2 = pos2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def chebyshev_distance(pos1, pos2):
    """King's move distance (includes diagonals)."""
    x1, y1 = pos1
    x2, y2 = pos2
    return max(abs(x1 - x2), abs(y1 - y2))
```

### Find All Cells Matching Condition
```python
def find_cells(grid, condition):
    """Find all cells matching a condition."""
    return [(x, y) for (x, y), value in grid.items() 
            if condition(value)]

# Examples
empty_cells = find_cells(grid, lambda v: v == ' ')
player_cells = find_cells(grid, lambda v: v == 'P')
non_wall_cells = find_cells(grid, lambda v: v != '#')
```

### Cell Transformations
```python
def transform_cells(grid, transform_func):
    """Apply transformation to all cells."""
    return {pos: transform_func(value) 
            for pos, value in grid.items()}

# Example: Invert all cells
def invert(value):
    return 'O' if value == ' ' else ' '

grid = transform_cells(grid, invert)
```

---

## Complete Example: Simple Grid Game

```python
WIDTH = 10
HEIGHT = 10

def create_grid():
    """Initialize grid with walls and empty space."""
    grid = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Walls on edges
            if x == 0 or x == WIDTH - 1 or y == 0 or y == HEIGHT - 1:
                grid[(x, y)] = '#'
            else:
                grid[(x, y)] = ' '
    return grid

def display(grid, player_pos):
    """Display grid with player."""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == player_pos:
                print('@', end='')
            else:
                print(grid[(x, y)], end='')
        print()

def main():
    grid = create_grid()
    player_pos = (5, 5)
    
    while True:
        display(grid, player_pos)
        move = input('Move (w/a/s/d): ').lower()
        
        # Calculate new position
        new_pos = player_pos
        if move == 'w':
            new_pos = (player_pos[0], player_pos[1] - 1)
        elif move == 's':
            new_pos = (player_pos[0], player_pos[1] + 1)
        elif move == 'a':
            new_pos = (player_pos[0] - 1, player_pos[1])
        elif move == 'd':
            new_pos = (player_pos[0] + 1, player_pos[1])
        
        # Check if move is valid
        if grid.get(new_pos, '#') != '#':
            player_pos = new_pos
        else:
            print("Can't move there!")

if __name__ == '__main__':
    main()
```

---

## Tips and Best Practices

1. **Consistent Coordinate System** - Decide on (x, y) order and stick to it
2. **Use Constants** - Define WIDTH, HEIGHT, EMPTY, WALL, etc.
3. **Validate Positions** - Always check bounds or use .get() with defaults
4. **Double Buffer Updates** - Use separate current/next grids for simultaneous updates
5. **Clear Naming** - Use descriptive names like `player_pos` not `p`
6. **Document Coordinate System** - Comment whether (0,0) is top-left or bottom-left
7. **Consider Wrapping** - Decide early if edges wrap or are boundaries

---

## Related Projects

- **Conway's Game of Life** - Classic cellular automaton
- **Langton's Ant** - Emergent behavior simulation
- **Forest Fire Sim** - Probabilistic spread
- **Four-in-a-Row** - Board game with dictionary coordinates
- **Tic-Tac-Toe** - Simple board game

---

## Additional Resources

- **game_development_patterns.md** - Game loop and state management
- **PROJECTS_OVERVIEW.md** - All simulation and game projects

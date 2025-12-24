# Terminal Graphics - Quick Reference

Techniques for creating visual effects and animations in the terminal.

## Table of Contents
- [Basic Output](#basic-output)
- [Unicode Characters](#unicode-characters)
- [ANSI Escape Codes](#ansi-escape-codes)
- [Bext Module](#bext-module)
- [Animation Techniques](#animation-techniques)
- [Seven-Segment Displays](#seven-segment-displays)

---

## Basic Output

### Print Without Newline
```python
# Print on same line
print('Hello', end='')
print(' World')  # Output: Hello World

# Print with custom separator
print('A', 'B', 'C', sep='-')  # Output: A-B-C
```

### Clear Screen
```python
# Simple method - print many newlines
print('\n' * 50)

# OS-specific clearing
import os
os.system('cls' if os.name == 'nt' else 'clear')
```

**Projects Using This:** Bouncing DVD Logo, Digital Stream

### Control Output Speed
```python
import time

for i in range(10):
    print(i, end=' ', flush=True)
    time.sleep(0.5)  # Wait half a second
```

---

## Unicode Characters

### Common Symbols
```python
# Shapes
SQUARE = '█'
CIRCLE = '●'
DIAMOND = '◆'
STAR = '★'

# Arrows
UP = '↑'
DOWN = '↓'
LEFT = '←'
RIGHT = '→'

# Card suits
HEARTS = '♥'    # chr(9829)
DIAMONDS = '♦'  # chr(9830)
SPADES = '♠'    # chr(9824)
CLUBS = '♣'     # chr(9827)

# Box drawing
TOP_LEFT = '┌'
TOP_RIGHT = '┐'
BOTTOM_LEFT = '└'
BOTTOM_RIGHT = '┘'
HORIZONTAL = '─'
VERTICAL = '│'
```

**Example: Draw Box**
```python
def draw_box(width, height):
    print('┌' + '─' * width + '┐')
    for _ in range(height):
        print('│' + ' ' * width + '│')
    print('└' + '─' * width + '┘')
```

**Projects Using This:** Blackjack (card suits), Fish Tank, Rotating Cube

### ASCII Art Characters
```python
# Block characters for pixel art
FULL_BLOCK = '█'
LIGHT_SHADE = '░'
MEDIUM_SHADE = '▒'
DARK_SHADE = '▓'

# Example: Draw progress bar
def progress_bar(percent):
    filled = int(percent / 10)
    empty = 10 - filled
    print('[' + '█' * filled + '░' * empty + ']')
```

**Projects Using This:** Progress Bar, Bitmap Message

### Emoji and Special Characters
```python
# Emoji (may not display on all terminals)
print('🎮 🎲 🃏 🎯')

# Math symbols
INFINITY = '∞'
PI = 'π'
DEGREE = '°'
```

---

## ANSI Escape Codes

### Basic Colors
```python
# Foreground colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'  # Reset to default

# Usage
print(f"{RED}Error!{RESET}")
print(f"{GREEN}Success!{RESET}")
```

### Background Colors
```python
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_BLUE = '\033[44m'

print(f"{BG_RED}Red background{RESET}")
```

### Text Styles
```python
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
REVERSE = '\033[7m'

print(f"{BOLD}Bold text{RESET}")
print(f"{UNDERLINE}Underlined{RESET}")
```

### Cursor Control
```python
# Move cursor
CURSOR_UP = '\033[1A'
CURSOR_DOWN = '\033[1B'
CURSOR_RIGHT = '\033[1C'
CURSOR_LEFT = '\033[1D'

# Clear operations
CLEAR_SCREEN = '\033[2J'
CLEAR_LINE = '\033[2K'

# Position cursor
def move_cursor(row, col):
    print(f'\033[{row};{col}H', end='')
```

**Note:** ANSI codes may not work on all terminals (especially older Windows terminals).

---

## Bext Module

The **Bext** module provides cross-platform terminal colors and positioning.

### Installation
```bash
pip install Bext
```

### Basic Usage
```python
import bext

# Set foreground color
bext.fg('red')
print('Red text')

# Set background color
bext.bg('blue')
print('Blue background')

# Reset colors
bext.fg('reset')
bext.bg('reset')
```

### Available Colors
```python
# Standard colors
colors = [
    'black', 'red', 'green', 'yellow',
    'blue', 'purple', 'cyan', 'white',
    'reset', 'random'
]

for color in colors:
    bext.fg(color)
    print(f'This is {color}')
```

### Cursor Positioning
```python
import bext

# Move cursor to specific position
bext.goto(10, 5)  # Column 10, Row 5
print('Text here')

# Clear screen
bext.clear()
```

### Complete Bext Example
```python
import bext
import time

bext.clear()

# Draw colored box
for x in range(20):
    for y in range(10):
        bext.goto(x, y)
        if x == 0 or x == 19 or y == 0 or y == 9:
            bext.fg('red')
            print('#', end='')
        else:
            bext.fg('blue')
            print(' ', end='')

# Animation loop
x, y = 1, 1
dx, dy = 1, 1

while True:
    bext.goto(x, y)
    print(' ', end='')  # Erase old position
    
    x += dx
    y += dy
    
    # Bounce off walls
    if x <= 1 or x >= 18:
        dx *= -1
    if y <= 1 or y >= 8:
        dy *= -1
    
    bext.goto(x, y)
    bext.fg('yellow')
    print('O', end='', flush=True)
    time.sleep(0.1)
```

**Projects Using This:** Bouncing DVD Logo, Digital Stream, Rainbow

---

## Animation Techniques

### Frame-Based Animation
```python
import time

frames = [
    '|',
    '/',
    '-',
    '\\'
]

for _ in range(20):
    for frame in frames:
        print(frame, end='\r', flush=True)  # \r returns to start of line
        time.sleep(0.1)
```

### Smooth Animation with Buffer
```python
import time
import sys

def animate_across_screen(char, width=40):
    for pos in range(width):
        # Build frame
        frame = ' ' * pos + char + ' ' * (width - pos - 1)
        
        # Display frame
        print(frame, end='\r', flush=True)
        time.sleep(0.05)
```

**Projects Using This:** Progress Bar, Bouncing DVD Logo

### Multi-Line Animation
```python
import time

def animate_falling(char, height=10):
    for row in range(height):
        # Clear screen
        print('\n' * 50)
        
        # Draw frame
        for i in range(height):
            if i == row:
                print(char)
            else:
                print()
        
        time.sleep(0.2)
```

### Double Buffering
```python
import time

# Build frame in memory first
def create_frame(data):
    frame = []
    for row in data:
        frame.append(''.join(row))
    return '\n'.join(frame)

# Display frame all at once
def display_frame(frame):
    print('\n' * 50)  # Clear
    print(frame)

# Main loop
while True:
    # Create frame
    frame_data = generate_frame_data()
    frame = create_frame(frame_data)
    
    # Display
    display_frame(frame)
    time.sleep(0.1)
```

**Projects Using This:** Conway's Game of Life, Langton's Ant

---

## Seven-Segment Displays

### Seven-Segment Digit Patterns
```python
DIGITS = {
    '0': [' _ ',
          '| |',
          '|_|'],
    '1': ['   ',
          '  |',
          '  |'],
    '2': [' _ ',
          ' _|',
          '|_ '],
    '3': [' _ ',
          ' _|',
          ' _|'],
    '4': ['   ',
          '|_|',
          '  |'],
    '5': [' _ ',
          '|_ ',
          ' _|'],
    '6': [' _ ',
          '|_ ',
          '|_|'],
    '7': [' _ ',
          '  |',
          '  |'],
    '8': [' _ ',
          '|_|',
          '|_|'],
    '9': [' _ ',
          '|_|',
          ' _|'],
}

def display_number(number):
    """Display number in seven-segment style."""
    num_str = str(number)
    
    # Print each row
    for row in range(3):
        for digit in num_str:
            print(DIGITS[digit][row], end=' ')
        print()
```

**Example Output:**
```
 _     _   _
| |  |  | |_|
|_|  |  |   |
```

**Projects Using This:** Digital Clock, Seven-Segment Display

### Advanced Seven-Segment
```python
def get_sevseg_str(number, min_width=0):
    """Get complete seven-segment string."""
    rows = ['', '', '']
    
    for digit in str(number).zfill(min_width):
        if digit in DIGITS:
            for i in range(3):
                rows[i] += DIGITS[digit][i] + ' '
    
    return '\n'.join(rows)

# Usage
print(get_sevseg_str(12345))
```

---

## Pattern Drawing

### Line Drawing
```python
def draw_horizontal_line(char, length):
    print(char * length)

def draw_vertical_line(char, height):
    for _ in range(height):
        print(char)

def draw_diagonal_line(char, size):
    for i in range(size):
        print(' ' * i + char)
```

### Pattern Generation
```python
def draw_diamond(size):
    """Draw diamond pattern."""
    # Top half
    for i in range(size):
        spaces = ' ' * (size - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    
    # Bottom half
    for i in range(size - 2, -1, -1):
        spaces = ' ' * (size - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

draw_diamond(5)
```

**Output:**
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

**Projects Using This:** Diamonds, Hex Grid, Shining Carpet

---

## Animation Helpers

### Flush Output
```python
import sys

# Force output to display immediately
print('Loading', end='', flush=True)
for _ in range(5):
    time.sleep(0.5)
    print('.', end='', flush=True)
print(' Done!')
```

### Frame Rate Control
```python
import time

FPS = 30
FRAME_TIME = 1.0 / FPS

while True:
    start_time = time.time()
    
    # Update and draw frame
    update_game()
    draw_frame()
    
    # Wait for next frame
    elapsed = time.time() - start_time
    if elapsed < FRAME_TIME:
        time.sleep(FRAME_TIME - elapsed)
```

### Spinner Animation
```python
import time
import sys

def spinner(duration=5):
    """Show spinning animation."""
    chars = '|/-\\'
    end_time = time.time() + duration
    
    i = 0
    while time.time() < end_time:
        sys.stdout.write('\r' + chars[i % len(chars)])
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    
    sys.stdout.write('\rDone!     \n')
```

---

## Tips and Best Practices

1. **Test Terminal Compatibility** - Not all terminals support all features
2. **Use `flush=True`** - For smooth animations
3. **Handle Ctrl+C** - Catch `KeyboardInterrupt` to clean up
4. **Reset Colors** - Always reset colors/styles when done
5. **Consider Terminal Size** - `os.get_terminal_size()` for responsive layouts
6. **Limit FPS** - Don't update faster than ~60 FPS
7. **Use Bext for Portability** - Works across platforms

---

## Complete Example: Animated Banner

```python
import time
import sys

def animated_banner(text, width=40):
    """Scroll text across screen."""
    # Pad text
    padded_text = ' ' * width + text + ' ' * width
    
    try:
        for offset in range(len(padded_text) - width):
            # Extract visible portion
            visible = padded_text[offset:offset + width]
            
            # Display
            sys.stdout.write('\r' + visible)
            sys.stdout.flush()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('\n\nStopped!')

animated_banner('*** HELLO WORLD ***')
```

---

## Related Projects

- **Animations:** Bouncing DVD, Digital Stream, Progress Bar, Rainbow
- **Art:** Diamonds, Hex Grid, Shining Carpet, Mondrian
- **Displays:** Digital Clock, Seven-Segment Display
- **Simulations:** Conway's Game of Life, Langton's Ant, Forest Fire
- **Visual Games:** Fish Tank, Ducklings, DNA Visualization

---

## Additional Resources

- **game_development_patterns.md** - Display patterns for games
- **PROJECTS_OVERVIEW.md** - All art and animation projects

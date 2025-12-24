# String Manipulation - Quick Reference

Common string operations and patterns used across Python projects.

## Table of Contents
- [Basic String Operations](#basic-string-operations)
- [String Methods](#string-methods)
- [String Formatting](#string-formatting)
- [Character Operations](#character-operations)
- [Text Generation](#text-generation)
- [Parsing and Validation](#parsing-and-validation)

---

## Basic String Operations

### Concatenation
```python
# Using +
greeting = 'Hello' + ' ' + 'World'

# Using join (more efficient for many strings)
words = ['Hello', 'World']
sentence = ' '.join(words)

# Repeat strings
dashes = '-' * 40  # '----------------------------------------'
```

### Slicing
```python
text = 'Hello World'

# Basic slicing
first_word = text[0:5]      # 'Hello'
second_word = text[6:11]    # 'World'

# Negative indices
last_char = text[-1]         # 'd'
last_word = text[-5:]        # 'World'

# Step slicing
every_other = text[::2]      # 'HloWrd'
reversed_text = text[::-1]   # 'dlroW olleH'
```

**Projects Using This:** ROT13, Pig Latin, Leetspeak

### String Length and Checking
```python
text = 'Hello'

# Length
length = len(text)  # 5

# Empty check
if text:
    print('Not empty')

# Contains substring
if 'ello' in text:
    print('Found')

# Starts with / ends with
if text.startswith('H'):
    print('Starts with H')
if text.endswith('o'):
    print('Ends with o')
```

---

## String Methods

### Case Conversion
```python
text = 'Hello World'

# Change case
lower = text.lower()        # 'hello world'
upper = text.upper()        # 'HELLO WORLD'
title = text.title()        # 'Hello World'
swapcase = text.swapcase()  # 'hELLO wORLD'
capitalize = text.capitalize()  # 'Hello world'
```

**Projects Using This:** Leetspeak, sPoNgEtExT, Caesar Cipher

### Whitespace Handling
```python
text = '  Hello World  '

# Remove whitespace
stripped = text.strip()      # 'Hello World'
left = text.lstrip()        # 'Hello World  '
right = text.rstrip()       # '  Hello World'

# Remove specific characters
text = '---Hello---'
trimmed = text.strip('-')   # 'Hello'
```

### Split and Join
```python
sentence = 'The quick brown fox'

# Split into words
words = sentence.split()     # ['The', 'quick', 'brown', 'fox']

# Split by specific delimiter
csv = 'apple,banana,cherry'
fruits = csv.split(',')      # ['apple', 'banana', 'cherry']

# Limit splits
parts = 'a:b:c:d'.split(':', 2)  # ['a', 'b', 'c:d']

# Join back together
rejoined = ' '.join(words)   # 'The quick brown fox'
csv_again = ','.join(fruits) # 'apple,banana,cherry'
```

**Projects Using This:** Clickbait Generator, Pig Latin

### Find and Replace
```python
text = 'Hello World, Hello Python'

# Find substring
index = text.find('World')   # 6
index = text.find('Java')    # -1 (not found)

# Count occurrences
count = text.count('Hello')  # 2

# Replace
new_text = text.replace('Hello', 'Hi')  # 'Hi World, Hi Python'

# Replace with limit
limited = text.replace('Hello', 'Hi', 1)  # 'Hi World, Hello Python'
```

**Projects Using This:** Caesar Cipher, Vigenère Cipher

---

## String Formatting

### F-Strings (Recommended)
```python
name = 'Alice'
age = 30
score = 95.5

# Basic formatting
message = f'Hello, {name}!'

# Expressions
info = f'{name} is {age} years old'
calc = f'5 + 3 = {5 + 3}'

# Format specifiers
formatted = f'Score: {score:.1f}%'  # 'Score: 95.5%'
padded = f'{age:05d}'               # '00030'
```

### Format Method
```python
# Positional
template = '{} scored {} points'
result = template.format('Alice', 100)

# Named
template = '{name} scored {points} points'
result = template.format(name='Alice', points=100)

# Number formatting
pi = 3.14159
rounded = '{:.2f}'.format(pi)  # '3.14'
```

### Old Style (% formatting)
```python
name = 'Bob'
age = 25

# Basic
message = 'Hello, %s!' % name

# Multiple values
info = '%s is %d years old' % (name, age)

# Formatting
number = 'Number: %05d' % 42  # 'Number: 00042'
```

---

## Character Operations

### Check Character Type
```python
char = 'A'

# Type checking
char.isalpha()      # True (letter)
char.isdigit()      # False
char.isalnum()      # True (letter or digit)
char.isupper()      # True
char.islower()      # False
char.isspace()      # False

# Check entire string
'abc'.isalpha()     # True
'abc123'.isalnum()  # True
'123'.isdecimal()   # True
```

**Projects Using This:** Caesar Cipher, Hangman, Bagels

### Character Code Conversion
```python
# Character to ASCII code
code = ord('A')     # 65
code = ord('a')     # 97

# ASCII code to character
char = chr(65)      # 'A'
char = chr(97)      # 'a'

# Unicode characters
heart = chr(9829)   # '♥'
```

**Example: Caesar Cipher Shift**
```python
def caesar_shift(char, shift):
    """Shift character by amount."""
    if char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    elif char.islower():
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        return char

shifted = caesar_shift('A', 3)  # 'D'
```

**Projects Using This:** Caesar Cipher, ROT13, Vigenère Cipher

### Iterate Over Characters
```python
word = 'Hello'

# Simple iteration
for char in word:
    print(char)

# With index
for i, char in enumerate(word):
    print(f'{i}: {char}')

# Build new string
uppercase_chars = [c.upper() for c in word]
uppercase_word = ''.join(uppercase_chars)
```

---

## Text Generation

### Random Text Templates
```python
import random

# Mad libs style
templates = [
    'The {adjective} {noun} {verb} {adverb}.',
    '{noun} is very {adjective}!',
]

words = {
    'adjective': ['big', 'small', 'happy'],
    'noun': ['cat', 'dog', 'bird'],
    'verb': ['runs', 'jumps', 'sleeps'],
    'adverb': ['quickly', 'slowly', 'loudly']
}

template = random.choice(templates)
sentence = template.format(
    adjective=random.choice(words['adjective']),
    noun=random.choice(words['noun']),
    verb=random.choice(words['verb']),
    adverb=random.choice(words['adverb'])
)
```

**Projects Using This:** Clickbait Generator, J'ACCUSE!

### Sentence Building
```python
def build_sentence(*parts):
    """Build sentence from parts."""
    return ' '.join(parts) + '.'

sentence = build_sentence('The', 'cat', 'meowed')
# 'The cat meowed.'
```

### Word Wrapping
```python
def wrap_text(text, width=40):
    """Wrap text to specified width."""
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + 1 > width:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word) + 1
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return '\n'.join(lines)
```

---

## Parsing and Validation

### Extract Numbers from String
```python
text = 'I have 5 apples and 3 oranges'

# Find all numbers
import re
numbers = re.findall(r'\d+', text)  # ['5', '3']
numbers = [int(n) for n in numbers]  # [5, 3]

# Simple parsing
digits = [char for char in text if char.isdigit()]
```

### Validate Input
```python
def is_valid_number(text):
    """Check if string is a valid number."""
    return text.isdecimal()

def is_valid_integer(text, min_val=None, max_val=None):
    """Check if string is valid integer in range."""
    if not text.lstrip('-').isdecimal():
        return False
    
    num = int(text)
    if min_val is not None and num < min_val:
        return False
    if max_val is not None and num > max_val:
        return False
    
    return True

# Usage
is_valid_number('123')    # True
is_valid_number('12.5')   # False
is_valid_integer('50', 1, 100)  # True
```

**Projects Using This:** Blackjack (bet validation), Hangman

### Clean User Input
```python
def clean_input(text):
    """Clean and normalize user input."""
    return text.strip().lower()

def get_yes_no(prompt):
    """Get yes/no response."""
    while True:
        response = input(prompt).strip().lower()
        if response.startswith('y'):
            return True
        elif response.startswith('n'):
            return False
        print('Please enter yes or no.')

# Usage
play_again = get_yes_no('Play again? (yes/no): ')
```

---

## Special String Manipulations

### Reverse String
```python
text = 'Hello'

# Using slicing (fastest)
reversed_text = text[::-1]  # 'olleH'

# Using reversed()
reversed_text = ''.join(reversed(text))

# Manual
reversed_text = ''
for char in text:
    reversed_text = char + reversed_text
```

### Remove Characters
```python
text = 'Hello, World!'

# Remove specific characters
no_punctuation = text.replace(',', '').replace('!', '')

# Remove all punctuation
import string
no_punct = text.translate(str.maketrans('', '', string.punctuation))
# 'Hello World'

# Remove vowels
vowels = 'aeiouAEIOU'
no_vowels = ''.join(c for c in text if c not in vowels)
```

### Pad Strings
```python
text = 'Hello'

# Left pad
padded = text.ljust(10)      # 'Hello     '
padded = text.rjust(10)      # '     Hello'
padded = text.center(10)     # '  Hello   '

# Pad with specific character
padded = text.ljust(10, '-') # 'Hello-----'
padded = text.rjust(10, '0') # '00000Hello'

# Zero-pad numbers
number = '42'
padded = number.zfill(5)     # '00042'
```

### Pig Latin Conversion
```python
def to_pig_latin(word):
    """Convert word to Pig Latin."""
    vowels = 'aeiouAEIOU'
    
    # Word starts with vowel
    if word[0] in vowels:
        return word + 'way'
    
    # Find first vowel
    for i, char in enumerate(word):
        if char in vowels:
            return word[i:] + word[:i] + 'ay'
    
    # No vowels
    return word + 'ay'

# Examples
to_pig_latin('hello')  # 'ellohay'
to_pig_latin('apple')  # 'appleway'
```

**Projects Using This:** Pig Latin

### Leetspeak Conversion
```python
def to_leetspeak(text):
    """Convert text to l33tsp34k."""
    leet_map = {
        'a': '4', 'A': '4',
        'e': '3', 'E': '3',
        'i': '1', 'I': '1',
        'o': '0', 'O': '0',
        't': '7', 'T': '7',
        's': '5', 'S': '5',
    }
    
    result = ''
    for char in text:
        result += leet_map.get(char, char)
    return result

# Example
to_leetspeak('Hello World')  # 'H3ll0 W0rld'
```

**Projects Using This:** Leetspeak

### Alternate Case (sPoNgEtExT)
```python
def to_spongetext(text):
    """Convert to mocking sponge text."""
    result = ''
    uppercase = True
    
    for char in text:
        if char.isalpha():
            result += char.upper() if uppercase else char.lower()
            uppercase = not uppercase
        else:
            result += char
    
    return result

# Example
to_spongetext('hello world')  # 'HeLlO WoRlD'
```

**Projects Using This:** sPoNgEtExT/Spongecase

---

## String Building Efficiently

### String Builder Pattern
```python
# SLOW - creates new string each time
result = ''
for i in range(1000):
    result += str(i)  # Creates 1000 intermediate strings!

# FAST - build list then join
parts = []
for i in range(1000):
    parts.append(str(i))
result = ''.join(parts)
```

### Multiple Line Building
```python
# Build multi-line strings
lines = []
lines.append('Line 1')
lines.append('Line 2')
lines.append('Line 3')

result = '\n'.join(lines)
```

---

## Regular Expressions (Bonus)

### Basic Regex Patterns
```python
import re

# Find email addresses
text = 'Contact: user@example.com or admin@site.org'
emails = re.findall(r'\w+@\w+\.\w+', text)

# Find phone numbers
text = 'Call 555-1234 or 555-5678'
phones = re.findall(r'\d{3}-\d{4}', text)

# Replace pattern
text = 'The price is $50'
new_text = re.sub(r'\$\d+', '$100', text)
# 'The price is $100'
```

---

## Complete Examples

### Word Game Helper
```python
def is_valid_word(word, available_letters):
    """Check if word can be made from available letters."""
    letters = list(available_letters.lower())
    
    for char in word.lower():
        if char not in letters:
            return False
        letters.remove(char)
    
    return True

# Usage
is_valid_word('cat', 'atcdog')  # True
is_valid_word('dog', 'atcdog')  # True
is_valid_word('bat', 'atcdog')  # False (no 'b')
```

### Text Statistics
```python
def text_stats(text):
    """Calculate text statistics."""
    words = text.split()
    
    return {
        'characters': len(text),
        'letters': sum(c.isalpha() for c in text),
        'digits': sum(c.isdigit() for c in text),
        'words': len(words),
        'sentences': text.count('.') + text.count('!') + text.count('?'),
        'uppercase': sum(c.isupper() for c in text),
        'lowercase': sum(c.islower() for c in text),
    }
```

### Hangman Word Display
```python
def display_word_with_blanks(word, guessed_letters):
    """Show word with guessed letters revealed."""
    display = ''
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

# Example
display_word_with_blanks('PYTHON', ['p', 'o', 'n'])
# 'P _ _ _ O N'
```

**Projects Using This:** Hangman

---

## Tips and Best Practices

1. **Use f-strings** - Modern and readable
2. **Join lists, don't concatenate** - Much faster for multiple strings
3. **Strip input** - Always strip whitespace from user input
4. **Check before accessing** - Check string length before indexing
5. **Use string methods** - Built-in methods are optimized
6. **Avoid repeated replacements** - Use `translate()` or regex for bulk replacements
7. **Case-insensitive comparisons** - Use `.lower()` or `.upper()`

---

## Related Projects

- **Text Manipulation:** Leetspeak, Pig Latin, sPoNgEtExT/Spongecase
- **Ciphers:** Caesar Cipher, ROT13, Vigenère Cipher
- **Word Games:** Hangman, Bagels, Guessthenumber
- **Text Generation:** Clickbait Generator, J'ACCUSE!
- **Input Validation:** All interactive games

---

## Additional Resources

- **game_development_patterns.md** - Input validation patterns
- **random_generation.md** - Random text generation
- **PROJECTS_OVERVIEW.md** - All text and cipher projects

# Scrabble-Python

A command-line implementation of the classic word game **Scrabble**. Play against friends or the computer in a text-based environment.

---

## Features

- **Single-player mode**: Play against a computer opponent.
- **Multiplayer mode**: Play with friends locally via the CLI.
- **Scoring system**: Follows official Scrabble scoring rules.
- **Interactive gameplay**: Input words, view the board, and track your scores in real-time.
- **Dictionary validation**: Ensure valid words using a built-in dictionary.

---

## Requirements

- Python 3.8 or higher
- Terminal or command-line interface

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Njijinoela/Scrabble-Python.git
   cd scrabble-cli
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the game:

   ```bash
   python main.py
   ```

2. Follow the on-screen instructions to:
   - Choose the mode (single-player or multiplayer).
   - Play against the computer or another player.
   - Place tiles, exchange tiles, or pass your turn.
   - View the current state of the board and scores.

---

## Game Rules

- Players take turns forming words on the board using tiles from their hand.
- Words must connect to existing words on the board.
- Points are awarded based on the letter values and placement on special tiles:
  - **Double Letter Score** (DL)
  - **Triple Letter Score** (TL)
  - **Double Word Score** (DW)
  - **Triple Word Score** (TW)
- The game ends when:
  - A player uses all their tiles and the bag is empty.
  - Both players pass consecutively.

For a full list of rules, visit [official Scrabble rules](https://scrabble.hasbro.com/en-us/rules).

---

## Controls

- **Place a word**: Type the word, starting position, and direction (e.g., `HELLO 7H V` to place "HELLO" starting at row 7, column H vertically).
- **Pass turn**: Enter `PASS` to skip your turn.

---

## Configuration

- **Board size**: Default is 15x15.
- **Tile distribution**: Follows official Scrabble letter frequencies and point values.

---

## Example Gameplay

```
Welcome to Scrabble CLI!

Player 1's turn.
Your tiles: E, A, R, T, L, I, N

Enter your move: EAR 8D H

Board:
  A B C D E F G H I J K L M N O
1
2
3
4
5
6
7
8        E A R
9
10
11
12
13
14
15

Player 1 scored 3 points.

Computer's turn.
Computer placed "TO" at 8G H.

Board:
  A B C D E F G H I J K L M N O
1
2
3
4
5
6
7
8        E A R T O
9
10
11
12
13
14
15

Computer scored 2 points.

Player 2's turn.
```

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature/bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- Inspired by the classic Scrabble board game.
- Special thanks to the Python community for libraries and tools.

---

Enjoy playing Scrabble in the CLI! Have fun and challenge your vocabulary!

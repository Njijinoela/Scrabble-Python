class Board:
    def _init_(self):
        self.size = 15
        self.board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.special_tiles = self._initialize_special_tiles()
        self._apply_special_tiles()

    def _initialize_special_tiles(self):
        """
        Returns a dictionary of special tiles, separating tile definitions 
        for readability and easier customization.
        """
        return {
            "TW": {(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)},
            "DW": {(1, 1), (1, 13), (2, 2), (2, 12), (3, 3), (3, 11), (4, 4), (4, 10), (7, 7),
                   (10, 4), (10, 10), (11, 3), (11, 11), (12, 2), (12, 12), (13, 1), (13, 13)},
            "TL": {(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)},
            "DL": {(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3),
                   (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11)}
        }

    def _apply_special_tiles(self):
        """
        Populates the board with special tiles based on their definitions.
        """
        for tile_type, positions in self.special_tiles.items():
            for row, col in positions:
                self.board[row][col] = tile_type
        self.board[self.size // 2][self.size // 2] = "*"  # Center tile

    def print_board(self):
        """
        Prints the board with formatted rows and columns.
        """
        header = "    " + "   ".join(f"{i:2}" for i in range(self.size))
        separator = "   " + "-" * (4 * self.size - 1)
        print(header)
        print(separator)
        for i, row in enumerate(self.board):
            row_content = " | ".join(f"{cell:2}" if len(cell) == 1 else cell for cell in row)
            print(f"{i:2} | {row_content} |")
            print(separator)

    def place_word(self, word, start_row, start_col, direction):
        """
        Places a word on the board in the specified direction.
        """
        if direction not in ("H", "V"):
            raise ValueError("Direction must be 'H' for horizontal or 'V' for vertical.")
        
        if not self._can_place_word(word, start_row, start_col, direction):
            raise ValueError("Invalid placement: Word overlaps or goes out of bounds.")
        
        for i, letter in enumerate(word):
            if direction == "H":
                self.board[start_row][start_col + i] = letter
            elif direction == "V":
                self.board[start_row + i][start_col] = letter

    def _can_place_word(self, word, start_row, start_col, direction):
        """
        Checks if a word can be placed at the specified location.
        """
        if direction == "H":
            if start_col + len(word) > self.size:
                print("debug word out of horizontal bounds")
                return False
            return all(self.board[start_row][start_col + i] in {" ", word[i]} for i in range(len(word)))
        elif direction == "V":
            if start_row + len(word) > self.size:
                print("debug word out of vertical bounds")
                return False
            return all(self.board[start_row + i][start_col] in {" ", word[i]} for i in range(len(word)))
        return False

    def is_valid_move(self, word, start_row, start_col, direction):
        """
        Validates the move logic (stub for extended functionality).
        """
        # Add more advanced move validation logic here as needed
        return self._can_place_word(word, start_row, start_col, direction)

if _name_ == "_main_":
    scrabble_board = Board()
    scrabble_board.print_board()
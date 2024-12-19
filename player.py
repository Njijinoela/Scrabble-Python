class Player:
    def __init__(self, name):
        self.name = name
        self.rack = []
        self.score = 0

    def play_word(self, board, word, start_row, start_col, direction, wordlist):
        """
        Attempts to play a word on the board. Updates score and rack if successful.
        Returns a tuple (success, message).
        """
        from board import place_word, is_valid_move
        from tiles import calculate_score

        word = word.upper()

        # Check if the word is valid
        if word not in wordlist:
            return False, f"'{word}' is not a valid word in the dictionary."

        # Check if the word can be formed from the player's rack
        if not self._can_form_word(word):
            return False, f"You cannot form the word '{word}' with your current rack."

        # Check if the move is valid on the board
        if not is_valid_move(board, word, start_row, start_col, direction):
            return False, f"Invalid move. The word '{word}' cannot be placed at ({start_row}, {start_col}) going {direction}."

        # Place the word and update rack and score
        place_word(board, word, start_row, start_col, direction)
        self.score += calculate_score(word)
        self._remove_letters_from_rack(word)

        return True, f"'{word}' successfully placed on the board."

    def _can_form_word(self, word):
        """
        Checks if the player's rack can form the given word.
        """
        rack_copy = self.rack[:]
        for letter in word:
            if letter in rack_copy:
                rack_copy.remove(letter)
            else:
                return False
        return True

    def _remove_letters_from_rack(self, word):
        """
        Removes the letters of the given word from the player's rack.
        """
import argparse
import time

class JumbleSolver():
    '''
    Class to solve a jumble problem using a given word list

    Initialise with word list and run solve on words as appropriate
    '''
    word_map: dict[str, list[str]] = {}
    words: list[str] = []

    def __init__(self, word_list: list[str]):
        for word in word_list:
            ordered_word = self.alphabetize_word(word)
            if ordered_word in self.word_map:
                self.word_map[ordered_word].append(word)
            else:
                self.word_map[ordered_word] = [word]

    @staticmethod
    def alphabetize_word(word: str) -> str:
        return ''.join(sorted(word))

    @staticmethod
    def remove_duplicates(word_list: list[str]):
        return [*set(word_list)]

    def solve(self, word: str) -> list[str]:
        '''
        Jumble solver in O(n!) time

        Finds the list of words at a set length in O(1) time but must perform n + 1 solves involving n!
        '''
        words = []
        word_len = len(word)
        
        ordered_word = self.alphabetize_word(word)
        # Get current complete word
        if ordered_word in self.word_map:
            words.extend(self.word_map[ordered_word])
        # Exit if at a leaf node
        if word_len == 1:
            return words
        # Get the one-less character words:
        for pos in range(word_len):
            new_word = ordered_word[:pos] + ordered_word[pos + 1:]
            words.extend(self.solve(new_word))
        return self.remove_duplicates(words)

if __name__ == '__main__':
    # Argument Parsing Setup
    parser = argparse.ArgumentParser()
    parser.add_argument('word_list_file', type=argparse.FileType('r'), help='File of word list to use.')
    parser.add_argument('word', type=str, help="Word to be \'jumble-solved\'.")
    parser.add_argument('--debug', action='store_true', help='Record and display runtime performance metrics')
    # Parse Arguments
    args = parser.parse_args()
    word_list = [line.strip() for line in args.word_list_file]
    # Run Jumble Solver
    solver = JumbleSolver(word_list)
    if args.debug:
        # Record start time
        time_start = time.time()
    words = solver.solve(args.word)
    if args.debug:
        print("JUMBLE SOLVED")
        # Record end time and print time elapsed
        time_end = time.time()
        print(f"Time Elapsed: {time_end - time_start} seconds")
    # Print result
    for word in words:
        print(word)
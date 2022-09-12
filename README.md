# jumble-solver
Jumble solver program to find anagrams and sub-anagrams of a collection of letters  
## Usage
Provide a file containing a word list to reference followed by the 'word' to be solved as positional arguments to the program.   
```usage: jumble_solver.py [-h] word_list_file word```   
## Complexity Analysis
Due to the pre-processing of the word list (ie. creating a hash table out of the alphabetized words), finding the anagrams of a set length is done in O(1) time. Finding the sub-anagrams, however, requires this solution to be carried out n times for the n-1 length 'words', 2n for the n-2 length 'words' and so on. This gives the algorithm O(n!) complexity. 
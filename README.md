# jumble-solver
Jumble solver program to find anagrams and sub-anagrams of a collection of letters  
## Usage
Provide a file containing a word list to reference followed by the 'word' to be solved as positional arguments to the program.   
```usage: jumble_solver.py [-h] word_list_file word```   
WARNING: This programs uses a naive algorithm so larger words will very quickly take unreasonable amounts of time
## Complexity Analysis
Due to the pre-processing of the word list (ie. creating a hash table out of the alphabetized words), finding the anagrams of a set length is done in O(1) time. Finding the sub-anagrams, however, requires this solution to be carried out n times for the n-1 length 'words', 2n for the n-2 length 'words' and so on. This gives the algorithm O(n!) complexity.  
The following outlines the average runtime at different character lengths; tests were performed by slowly adding the alphabet to a string and recording the average:  
| Character count  | Runtime           | No. Attempts |
| ---------------- | ----------------- | ------------ |
| 1 character      | 0.00012 seconds   | 10 attempts  |
| 2 characters     | 0.00067 seconds   | 10 attempts  |
| 3 characters     | 0.00062 seconds   | 10 attempts  |
| 4 characters     | 0.00141 seconds   | 10 attempts  |
| 5 characters     | 0.00166 seconds   | 10 attempts  |
| 6 characters     | 0.00185 seconds   | 10 attempts  |
| 7 characters     | 0.00685 seconds   | 5 attempts   |
| 8 characters     | 0.06371 seconds   | 5 attempts   |
| 9 characters     | 0.58086 seconds   | 5 attempts   |
| 10 characters    | 5.9064 seconds    | 3 attempts   |
| 11 characters    | 66.744 seconds    | 1 attempt    |  

Using this data, one can see the trend towards factorial time, particularly in longer words. 

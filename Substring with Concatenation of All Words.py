import collections
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

     
        word_len = len(words[0])
        num_words = len(words)
        total_concat_len = word_len * num_words

        word_counts = collections.Counter(words)

        result_indices = []

        for offset in range(word_len):
            left_ptr = offset
            
            current_window_word_counts = collections.Counter()
            words_found_in_window = 0

           
            for right_ptr in range(offset, len(s) - word_len + 1, word_len):
                current_word = s[right_ptr : right_ptr + word_len]

                if current_word not in word_counts:
                    current_window_word_counts.clear()
                    words_found_in_window = 0
                    left_ptr = right_ptr + word_len
                else:
                    current_window_word_counts[current_word] += 1
                    words_found_in_window += 1

                    
                    while current_window_word_counts[current_word] > word_counts[current_word]:
                        leftmost_word = s[left_ptr : left_ptr + word_len]
                        current_window_word_counts[leftmost_word] -= 1
                        words_found_in_window -= 1
                        left_ptr += word_len


                    if words_found_in_window == num_words:
            
                        result_indices.append(left_ptr)

                        
                        leftmost_word = s[left_ptr : left_ptr + word_len]
                        current_window_word_counts[leftmost_word] -= 1
                        words_found_in_window -= 1
                        left_ptr += word_len
                        
        return result_indices
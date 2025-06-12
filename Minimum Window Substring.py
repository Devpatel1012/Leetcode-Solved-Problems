from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t:
            return ""

        
        # Example: t = "ABC" -> target_char_counts = {'A': 1, 'B': 1, 'C': 1}
        target_char_counts = Counter(t)

        # Step 1: Determine the number of unique characters in t that we need to match.
        # This is used to check if our window is "valid" (contains all required types of chars).
        required_unique_chars = len(target_char_counts)

        # Step 1: Initialize pointers and counters for the sliding window
        left = 0  # The left pointer of our current window in string s
        
        # This counter tracks how many unique characters from 't'
        # have met their required frequency (or exceeded it) within the current window.
        formed_unique_chars = 0 
        
        # A dictionary to store the frequency of characters currently within our window.
        # defaultdict(int) automatically sets a default value of 0 for new keys.
        window_char_counts = defaultdict(int)

        # Step 1: Variables to store the result (smallest valid window found so far)
        min_len = float('inf')  # Initialize with a very large value
        min_window_start = 0    # Stores the starting index of the minimum window

        # Step 2: Expanding the Window (Move right pointer)
        # Iterate 'right' from 0 to the end of string 's'
        for right in range(len(s)):
            char_r = s[right]  # Get the character at the current right pointer

            # Add the character to our window's count
            window_char_counts[char_r] += 1

            # Check if this character is one of the required characters from 't'
            # AND if its count in the window now exactly matches the required count in 't'.
            # If both are true, it means we've successfully "formed" one more unique character requirement.
            if char_r in target_char_counts and window_char_counts[char_r] == target_char_counts[char_r]:
                formed_unique_chars += 1
            
            # --- Step 3: Shrink the Window (Move left pointer) ---
            # This 'while' loop runs as long as the current window is "valid"
            # (i.e., all required unique characters from 't' are "formed").
            while formed_unique_chars == required_unique_chars:
                # Update the minimum window found so far
                current_window_len = right - left + 1
                if current_window_len < min_len:
                    min_len = current_window_len
                    min_window_start = left  # Store the start index of this minimum window
                
                # Try to shrink the window from the left side
                char_l = s[left]  # Get the character at the current left pointer

                # Before removing char_l from the window, check its impact on formed_unique_chars.
                # If char_l is a required character from 't'
                # AND its count in the window was *exactly* what 't' needed *before* removal,
                # then removing it means we are no longer meeting that specific requirement.
                # So, we decrement 'formed_unique_chars'.
                if char_l in target_char_counts and window_char_counts[char_l] == target_char_counts[char_l]:
                    formed_unique_chars -= 1
                
                # Remove the character from the window's count
                window_char_counts[char_l] -= 1
                
                # Move the left pointer to truly shrink the window
                left += 1

        # Step 4: Return Result
        # After iterating through all of 's', if min_len is still infinity,
        # it means no valid window was ever found.
        if min_len == float('inf'):
            return ""
        else:
            # Return the minimum window substring using the stored start index and length.
            return s[min_window_start : min_window_start + min_len]
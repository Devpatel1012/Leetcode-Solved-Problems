class Solution(object):
    def decodeCiphertext(self, text, rows):
        if rows == 1:
            return text
        
        n = len(text)
        cols = n // rows
        st = []

        for start_col in range(cols):   
            for k in range(rows):      
                i = k
                j = start_col + k      
                
                if j >= cols:
                    break
                
                pos = i * cols + j
                st.append(text[pos])

        return "".join(st).rstrip()
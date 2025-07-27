class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                extraSpace = maxWidth - length
                spaces = extraSpace // max(1, len(line) - 1)
                remainder = extraSpace % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1

                res.append("".join(line))
                line, length = [], 0  # FIXED: length spelled correctly

            line.append(words[i])
            length += len(words[i])
            i += 1

        # Last line: left-justified
        last_line = " ".join(line)
        trailing_space = maxWidth - len(last_line)  # FIXED: spelling
        res.append(last_line + " " * trailing_space)

        return res

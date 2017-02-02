class Solution(object):
    def fullJustify(self, words, max_width):
        """
        :type words: List[str]
        :type max_width: int
        :rtype: List[str]
        """
        output = []
        curr_line = []
        curr_size = 0
        index = 0
        size = len(words)
        while index < size:
            curr_size += len(word)
            if curr_size <= max_width:
                curr_size += 1
                curr_line.append(word)
                index += 1
            else:
                output.append(self.justify(curr_line, max_width))
                curr_line = []
                curr_size = 0
        output.append(self.justify(curr_line, max_width))
        return output

    def justify(self, words, max_width):
        total_size = sum(map(lambda x: len(x), words))
        words_cnt = len(words)
        if words_cnt == 1:
            return " ".join(words).ljust(max_width)
        avg_space = (max_width-total_size) / (words_cnt-1)
        extra_space = (max_width - total_size) % (words_cnt-1)
        return (" "*(avg_space+1)).join(words[:extra_space] + [""]) + (" "*avg_space).join(words[extra_space:])

solution = Solution()

output =  solution.fullJustify(["This", "is", "an", "example", "of", "text", "justificaiton."], 16)
print map(len, output)
print output

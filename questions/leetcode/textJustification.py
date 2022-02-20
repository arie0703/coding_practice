def fullJustify(words, maxWidth):
    res = []
    row = []
    count = 0

    def makeRow(s, maxWidth, num_of_words):
        # 一行の長さがmaxWidthに等しくなるよう、均等にスペースを配置する
        i = 0
        needed_spaces = maxWidth - len(s)
        if num_of_words > 0:
            q = needed_spaces // num_of_words
            r = needed_spaces % num_of_words
            for _ in range(num_of_words):
                i = s.find(' ', i)
                s = s[:i] + (' ' * q) + s[i:]
                if r > 0:
                    s = s[:i] + (' ') + s[i:]
                    r -= 1
                    i += (q + 2)
                else:
                    i += (q + 1)
        else:
            s += (' ' * needed_spaces)

        return s

    for w in words:
        count += (len(w) + 1)
        if count > maxWidth + 1:
            s = makeRow(" ".join(row), maxWidth, len(row)-1)
            res.append(s)
            row = []
            count = len(w) + 1

        row.append(w)

    if row:
        spaces = ' ' * (maxWidth - len(" ".join(row)))
        res.append(" ".join(row) + spaces)


    for r in res:
        print(r, len(r))

    return res

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
print(fullJustify(words,maxWidth))
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(fullJustify(words,maxWidth))
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(fullJustify(words,maxWidth))





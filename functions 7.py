def longest_word(word_list):
    longest = ""
    for word in word_list:
        if len(word) > len(longest):
            longest = word
    return longest


words = []
word_ = ""
while word_ != "1":
    word_ = input("add word to list (or 1 to end): ")
    words.append(word_)

print(f"The longest in the list {words} is {longest_word(words)}")

def start_with_a(word_):
    if word_[0] == "A":
        return True

    else:
        return False


# Main routine
word = input("enter the word: ").title()
print(start_with_a(word))

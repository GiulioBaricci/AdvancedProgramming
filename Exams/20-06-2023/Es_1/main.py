from wordle import read_words, wordle

def print_wordlet(wordlet):
    for w in wordlet:
        print(w)
    print('\
          ')
    
if __name__ == "__main__":
    wl = read_words("dictionary.txt")
    print_wordlet(wordle("model", "melon", wl))
    print_wordlet(wordle("slice", "mount", wl))
    print_wordlet(wordle("crane", "vowel", wl))
    print_wordlet(wordle("drive", "sooty", wl))
    print_wordlet(wordle("yacht", "sassy", wl))
    print_wordlet(wordle("happy", "roots", wl))
    print_wordlet(wordle("lines", "hatch", wl))
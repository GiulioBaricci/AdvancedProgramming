def read_words(fileName):
    wordlist = []
    with(open(fileName, 'r') as file):
        wordlist = [word for word in file.read().split('\n') if len(word) == 5]
    return wordlist


def wordle(startWord, wordle, dictionary):
    guesses = []                                # Lista di tentativi
    correctCorrect = {}                         # Dictionary delle lettere corrette e alla posizione corretta
    correctWrong = {}                           # Dictionary delle lettere corrette ma alla posizione sbagliata
    wrong = []                                  # Dictionary delle lettere sbagliate
    wordleList = [c for c in wordle]            # Lista delle lettere del wordle
    def guess(currentWord):
        if currentWord == wordle:               # Se la parola è corretta
            guesses.append("\u001b[32;1m" + currentWord + "\u001b[0m")      # Colora la parola di verde
            return guesses                      # Ritorna i tentativi
        else:
            currentList = [c for c in currentWord]      # Lista delle lettere della parola corrente
            for ind in range(len(currentList)):         # Scorre per ogni carattere della parola
                if currentList[ind] == wordleList[ind]:                         # Se il carattere è corretto
                    if ind not in correctCorrect:                               # Se il carattere non è nel dictionary delle lettere corrette e alla posizione corretta
                        correctCorrect[ind] = currentList[ind]                  # Lo aggiunge con l'indice come chiave 
                    currentList[ind] = "\u001b[32;1m" + currentList[ind]
                elif wordleList.__contains__(currentList[ind]):
                    if ind not in correctCorrect:
                        correctWrong[ind] = currentList[ind]
                    currentList[ind] = "\u001b[33;1m" + currentList[ind]
                else:
                    if not wrong.__contains__(currentList[ind]):
                        wrong.append(currentList[ind])
                    currentList[ind] = "\u001b[37;1m" + currentList[ind]
                currentList[ind] = currentList[ind] + "\u001b[0m"

            dictionary.remove(currentWord)

            currentWord = [word for word in dictionary if (not any(x in [c for c in word] for x in wrong)) and \
                           (all([c for c in word][ind] == char for ind, char in correctCorrect.items())) and \
                            (all([c for c in word].__contains__(char) and [c for c in word][ind] != char for ind, char in correctWrong.items()))][0]
            
            guesses.append("".join(currentList))
            return guess(currentWord)
    return guess(startWord)

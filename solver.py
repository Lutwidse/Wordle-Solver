def get_words():
    with open("words_alpha.txt", "r") as f:
        words = f.read().splitlines()
        return words

def get_result():
    result = input("(M/W/C) > ")
    if result == "CCCCC":
        print("(Wordle) > End")
        exit(1)
    return result

def get_guess():
    guess = input("(Wordle) > ")
    return guess

def update_words(words, guess, result):
    m,w,c = [],[],[]
    for i in range(5):
        if result[i] == "M":
            m.append(f"{i}:{guess[i]}")
        elif result[i] == "W":
            w.append(guess[i])
        elif result[i] == "C":
            c.append(f"{i}:{guess[i]}")

    if guess in words:
        words.remove(guess)
    updated_words = []
    for i in words:
        # Miss
        for j in m:
            idx, char = j.split(":")
            if i[int(idx)] == char:
                break
        else:
            # Correct
            for k in c:
                idx, char = k.split(":")
                if i[int(idx)] != char:
                    break
            else:
                # WrongSpot
                for l in w:
                    if l not in i:
                        break
                else:
                    updated_words.append(i)

    if not updated_words:
        print("(Wordle) > Words are empty")
        exit(1)
    return updated_words
            

def solve():
    words = get_words()
    while True:
        guess = get_guess()
        result = get_result()
        words = update_words(words, guess, result)
        print(words)

if __name__ == "__main__":
    solve()
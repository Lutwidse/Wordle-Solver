from itertools import product

def get_words():
    with open("wordle-answers-alphabetical.txt", "r") as f:
        words = f.read().splitlines()
        return words

def get_result():
    result = input("(M/W/C) > ")
    if result == "CCCCC":
        print("(Wordle) > End")
        exit(0)
    return result

def get_guess():
    guess = input("(Wordle) > ")
    return guess

def update_words(words, guess, result):
    miss, wrong_spot, correct = [], {}, {}
    for i in range(5):
        if result[i] == "M":
            miss.append(guess[i])
        elif result[i] == "W":
            wrong_spot.update({i:guess[i]})
        elif result[i] == "C":
            correct.update({i:guess[i]})
            
    if guess in words:
        words.remove(guess)

    # Miss
    updated_words = words
    for i in words[:]:
        for m in miss:
            if m in i and m not in correct.values():
                updated_words.remove(i)
                break
    
    # WrongSpot
    for i in words[:]:
        for ws_k, ws_v in wrong_spot.items():
            if i[ws_k] == ws_v:
                updated_words.remove(i)
                break
    # Correct
    for i in words[:]:
        for c_k, c_v in correct.items():
            if i[c_k] != c_v:
                updated_words.remove(i)
                break


    if not updated_words:
        print("(Wordle) > Words are empty")
        exit(0)
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
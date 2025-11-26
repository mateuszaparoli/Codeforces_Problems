n = int(input())

while(n > 0):
    word = (input())
    if len(word) <= 10 :
        print(word)
    else:
        word1 = word[0]
        wordX = word[-1]
        print(f"{word1}{len(word)-2}{wordX}")
    n = n - 1

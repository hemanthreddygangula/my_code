import random
import hangman_words as words
import hangman_asciiart as pics

print(pics.logo)
word = random.choice(words.a).lower()
choosen_word = []
for i in word:
    choosen_word.append(i)
blanks = ["_"]*len(choosen_word)
blanks[len(choosen_word)//2] = choosen_word[len(choosen_word)//2]

#print(word)
print("Word: ", *blanks)
lives = 6
print(pics.hangman[0])

while lives>0:
    guess = input("Guess a letter: ").lower()
    if guess in choosen_word:
        co = choosen_word.count(guess)
        while co>0:
            blanks[choosen_word.index(guess)] = guess
            choosen_word[choosen_word.index(guess)] = '_'
            co-=1
        print(*blanks)
        if '_' not in blanks:
            print("You won the Game")
            break
    else:
        lives-=1
        print(pics.hangman[6-lives])
        print(f"You lost a life. You have remaining {lives} lives")
        if lives == 0:
            print("You are hanged.")
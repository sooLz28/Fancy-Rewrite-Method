import random
import string
words = [
    "apple", "baby", "ball", "bear", "bird", "book", "bread", "chair", "cheese", "child",
    "cloud", "dance", "dream", "earth", "family", "fish", "flower", "friend", "fruit", "game",
    "ghost", "glass", "grass", "happy", "heart", "horse", "house", "light", "magic", "money",
    "moon", "music", "ocean", "panda", "piano", "pizza", "plant", "queen", "river", "robot",
    "school", "sheep", "shirt", "shoe", "smile", "snake", "space", "spoon", "spring", "stars",
    "stone", "story", "sunny", "table", "tiger", "train", "tree", "uncle", "water", "window",
    "world", "zebra", "angel", "arrow", "beach", "block", "bread", "brick", "brush", "carpet",
    "candy", "clock", "crown", "dance", "eagle", "fairy", "flame", "forest", "glove", "honey",
    "island", "jewel", "ladder", "lemon", "magic", "melon", "pencil", "rainy", "rocket", "smile",
    "soccer", "summer", "ticket", "tomato", "turtle", "vacuum", "village", "winter", "yogurt"
]

hangmann = {
    0: (
        "     -----",
        "     |   |",
        "         |",
        "         |",
        "         |",
        "         |",
        "    ========="
    ),
    1: (
        "     -----",
        "     |   |",
        "     O   |",
        "         |",
        "         |",
        "         |",
        "    ========="
    ),
    2: (
        "     -----",
        "     |   |",
        "     O   |",
        "     |   |",
        "         |",
        "         |",
        "    ========="
    ),
    3: (
        "     -----",
        "     |   |",
        "     O   |",
        "    /|   |",
        "         |",
        "         |",
        "    ========="
    ),
    4: (
        "     -----",
        "     |   |",
        "     O   |",
        "    /|\\  |",
        "         |",
        "         |",
        "    ========="
    ),
    5: (
        "     -----",
        "     |   |",
        "     O   |",
        "    /|\  |",
        "    /    |",
        "         |",
        "    ========="
    ),
    6: (
        "     -----",
        "     |   |",
        "     O   |",
        "    /|\  |",
        "    / \  |",
        "         |",
        "    ========="
    )
}


def hangman(wrong):
           for line in hangmann[wrong]:
            print(line)
    













def hintt(hint):
    print(' '.join(hint))




















def answershow(answer):
    print('the answer is')
    print(f'********{answer}*********')
    
    




























def main():    
    answer=random.choice(words)
    guesses=set()
    wrong=0
    hint=['_']* len(answer)
    run=True
    while run:
        hangman(wrong)
        hintt(hint)
        guess=input('Guess a letter ! ').lower()
        
        if len(guess) != 1:  
            print('only one letter should be guessed !')
            continue
        elif not guess.isalpha():
            print('YOU SHOULD PUT A LETTER!')
            continue
        elif guess in guesses:
            print(f'{guess} is already guessed!')
            continue
        guesses.add(guess)    
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i]=guess
        else:
            wrong+=1
        if wrong == 6:
            print('YOU LOST!')
            hangman(wrong)
            answershow(answer)
            run=False
        if "_" not in hint:
               print('YOU WON!')
               answershow(answer)
               print(f'you made {wrong} mistakes')    
               run=False
    ask=input('wanna play again? (Y/N): ').upper()
    if ask =="Y":
       main()    
        
    else:
         
                             
      
      print('Thanks for playing!')       
                       


                    
        
        
        
            

























































main()
import random


class colorcodes:
    GREEN = '\u001b[42;1m'
    YELLOW = '\u001b[43;1m'
    ENDC = '\033[0m'

def init_file(numletters):
    name = numletters + '.txt'
    f = open(name, 'r')
    content = f.read()
    word_list = content.splitlines()
    f.close()
    return word_list

def charsplit(word):
    return [char for char in word]

def main():
    num = input('Word length: four or five letters? Type \'four\' or \'five\' to select. ')
    while num != 'four' and num != 'five':
        num = input('Error! Invalid response\n')
    word_list = init_file(num)
    answer = random.choice(word_list)
    playing = True
    counter = 0
    while playing:
        guess = input('Guess a word!\n')
        while len(guess) != len(answer):
            print('Error! Please make sure your input is the right length')
            guess = input('Guess a word!\n')
        while guess not in word_list:
            print('Error! Please make sure your guess is a valid word')
            guess = input('Guess a word!\n')
        guesslist = charsplit(guess)
        answerlist = charsplit(answer)
        if guesslist == answerlist:
            playing = False
            print(colorcodes.GREEN + answer + colorcodes.ENDC)
            print('You win! This attempt took you ' + str(counter) + ' tries')
        else:
            for x in range(0, len(guesslist)):
                if guesslist[x] == answerlist[x]:
                    print(colorcodes.GREEN + guesslist[x] + ' ' + colorcodes.ENDC)
                    answerlist[x] = 0
                elif guesslist[x] in answerlist:
                    print(colorcodes.YELLOW + guesslist[x] + ' ' + colorcodes.ENDC)
                    index = answerlist.index(guesslist[x])
                    answerlist[index] = 0
                else:
                    print(guesslist[x] + ' ')
            counter += 1

main()


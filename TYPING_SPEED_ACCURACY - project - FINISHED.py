# TYPING TEST, MEASURING TIME AND ACCURACY
# FINISHED !!!

# import pandas for reading the file and modifying it
import pandas as pd
# import time for the measurement
import time
# import random for the sentences to be randomly picked
import random

# import numpy just for rounding
import numpy as np

# and from itertools import zip_longest 'cause in some case we wanna zip through the longest iterator
from itertools import zip_longest


start_stop = ('''
TEST FOR START AND STOP AND TOTAL TIME

start = time.time()
a = input('napis: ')
stop = time.time()

total = stop - start
print('total time', total)

Hello Matus.
Hellos Matus.  dadawdwd

''')

# we have created a new file with english sentences only --> 'sentences_enf.txt'
# --> data = pd.read_csv('eng_sentences.tsv', delimiter='\t', index_col='Number', names=['Number', 'Lang', 'Sentences'])
# --> data.drop(columns=['Lang'], inplace=True)
# --> sentences = data['Sentences']
# --> sentences.to_csv('sentences_eng.txt', index=False)

# so we are reading the file called 'sentences_eng.txt'
df = pd.read_csv('sentences_eng.txt')
# with this we only grab the sentences column and it's values
sentences_df = df['Sentences']

# we wanna apply the len() function for the sentences_df pandas frame
length_sentences = sentences_df.apply(len)

# we are creating the mask where the sentences have more than 100 characters
mask = length_sentences >= 100
# and then we wanna delete those sentences using .drop()
# .drop() works only to delete rows and with a given index so --> .index means that it will just convert the answer to a index where it is
df.drop(index=df[mask].index, inplace=True)

sentences_df = df['Sentences']


# now we create a new list of sentences
sentences = []
# and for each sentence in our pandas sentences_df we wanna append each sentence into the sentences list
for sentence in sentences_df:
    sentences.append(sentence)


def typing_test():
    # run = True for the while infinite loop
    run = True

    def infinite_loop():
        # so while True --> infinite loop
        while run:
            print('')
            # ask the player if he wants to start
            begin = input('Would you like to start the typing test? Yes/No: ').upper()

            # a random sentences is picked up in the sentences list
            random_select = random.choice(sentences)

            # if player wants to begin
            if begin == 'YES':

                def test():
                    print('')
                    # he has to just click enter for the sentence to be generated
                    _ = input('CLICK Enter when you are ready to start')
                    print('')

                    # right after he clicked enter, the random sentence is being printed out
                    print('         ' + random_select)

                    # start the timer using --> time.time()
                    start_time = time.time()

                    # ask the player to rewrite the sentence as fast and as accurate as possible
                    rewritten = input('REWRITE: ')

                    # we take the 1/4 of the random picked up sentence
                    one_fourth = len(list(random_select)) / 4

                    # and now let's see if the player has rewritten at least the 1/4 of the random generated sentence
                    # so if he did
                    if len(list(rewritten)) > one_fourth:

                        # stop the timer right after he clicked enter, after he typed the rewritten text
                        stop_time = time.time()
                        # than we calculate the total_time using the stop_time - start_time
                        total_time = stop_time - start_time


                        # we create 3 list of that rewritten sentence, 'cause we are going to check for 3 conditions
                        # 1st and 3th will take each element and create a list
                        # 2nd will take each word and create a list
                        lst_rewritten = list(rewritten)
                        lst2_rewritten = rewritten.split(' ')
                        lst3_rewritten = list(rewritten)

                        # we also make a list of words for the random picked up sentence
                        split_rd = random_select.split(' ')


                        # this is 1% amount characters in the random generated sentence
                        one_percent_letter = 1 / len(list(random_select))
                        # and with this one we are going to add up our percentage accuracy
                        percentage_letter = 0

                        # so we are enumerating through the zip of 2 lists --> for index, (a, b) in enumerate(zip(a_list, b_list))
                        for ind, (char_rd, char_rewritten) in enumerate(zip(list(random_select), lst_rewritten)):

                            # if that character is equal to the character in the rewritten text than add the percentage
                            if char_rd == char_rewritten:
                                percentage_letter += one_percent_letter


                            # if not, and the rewritten sentence has more characters than the random generated sentence
                            # just in that rewritten list delete that character using -->
                            # .pop() --> it takes the exact position/index so that's why we are using enumerate
                            elif char_rd != char_rewritten and len(list(random_select)) <= len(lst_rewritten):
                                lst_rewritten.pop(ind)


                            # if not, and the rewritten sentence has less characters than the random generated sentence
                            elif char_rd != char_rewritten and len(list(random_select)) > len(lst_rewritten):
                                # just in that rewritten sentence add/append a space ' ' into that location where there are not equal
                                # --> using .insert() --> takes the position/index and than what you wanna append there ' '
                                lst_rewritten.insert(ind, ' ')



                        # this is 1% amount words in the random generated sentence
                        one_percent_word = 1 / len(split_rd)
                        # and with this one we are going to add up our percentage accuracy
                        percentage_word = 0

                        # so we are enumerating through the zip of 2 lists --> for index, (a, b) in enumerate(zip(a_list, b_list))
                        for ind, (word_rd, word_rewritten) in enumerate(zip(split_rd, lst2_rewritten)):

                            # if that word is equal to the word in the rewritten text than add the percentage
                            if word_rd == word_rewritten:
                                percentage_word += one_percent_word


                            # if not, but the length is still the same of those word in those 2 lists
                            elif word_rd != word_rewritten and len(split_rd) == len(lst2_rewritten):
                                # iterate through those 2 words and take each letter in those words
                                for letter_rd, letter_rewritten in zip(word_rd, word_rewritten):
                                    # this is 1% amount letters in the word in the random generated sentence
                                    letter_percent = one_percent_word / len(word_rd)

                                    # and if that letter is equal to the letter in rewritten word, add the percentage
                                    if letter_rd == letter_rewritten:
                                        percentage_word += letter_percent


                            # if not, but in rewritten sentence are more words than in that random generated one
                            # just in that rewritten list delete that word using -->
                            # .pop() --> it takes the exact position/index so that's why we are using enumerate
                            elif word_rd != word_rewritten and len(split_rd) <= len(lst2_rewritten):
                                lst2_rewritten.pop(ind)


                            # if not, but in rewritten sentence are less words than in that random generated one
                            elif word_rd != word_rewritten and len(split_rd) > len(lst2_rewritten):
                                # just in that rewritten sentence add/append a space ' ' into that location where there are not equal
                                # --> using .insert() --> takes the position/index and than what you wanna append there ' '
                                lst2_rewritten.insert(ind, ' ')



                        # this is 1% amount characters in the random generated sentence
                        one_percent_length = 1 / len(list(random_select))
                        # and with this one we are going to add up our percentage accuracy
                        percentage_length = 0

                        # so we are enumerating through the longest zip of 2 lists --> for index, (a, b) in enumerate(zip_longest(a_list, b_list))
                        for ind, (char_rd, char_rewritten) in enumerate(zip_longest(list(random_select), lst3_rewritten)):

                            # if that character is equal to the character in the rewritten text than add the percentage
                            if char_rd == char_rewritten:
                                percentage_length += one_percent_length


                            # if not, and the rewritten sentence has more characters than the random generated sentence
                            # just in that rewritten list delete that character using -->
                            # .pop() --> it takes the exact position/index so that's why we are using enumerate
                            elif char_rd != char_rewritten and len(list(random_select)) <= len(lst3_rewritten):
                                lst3_rewritten.pop(ind)
                                # and also you subtract that percentage by the half of that 1%
                                percentage_length -= one_percent_length / 2


                            # if not, and the rewritten sentence has less characters than the random generated sentence
                            elif char_rd != char_rewritten and len(list(random_select)) > len(lst3_rewritten):
                                # just in that rewritten sentence add/append a space ' ' into that location where there are not equal
                                # --> using .insert() --> takes the position/index and than what you wanna append there ' '
                                lst3_rewritten.insert(ind, ' ')
                                # and also you subtract that percentage by the half of that 1%
                                percentage_length -= one_percent_length / 2


                            # if that percentage is less or equal to 0, it cannot get any fewer, than just keep it in 0%
                            if percentage_length <= 0:
                                percentage_length = 0


                        # we calculate the mean percentage of those 3 percentage by adding  them up, and than divide them by 3
                        # and also we are using np.round() to round that value into 2 decimals --> .round(number, how_many_decimals)
                        mean_percentage = np.round((percentage_letter + percentage_word + percentage_length) / 3, 2)

                        # let's also check if that mean percentage was f.e. 100.1%, there cannot be more than 100%,
                        # so everything more or equal to 100 is just 1 (percentage is * 100)
                        if mean_percentage * 100 >= 100:
                            mean_percentage = 1


                        print('')
                        # print out the score, you will multiply the percentage by 100, 'cause we want it to be in % units
                        # and also you will round the total time into 2 decimal points
                        print('Your total percentage:', str(mean_percentage * 100) + '%')
                        print('Your time was:', str(np.round(total_time, 2)) + 's')


                    # if the player has typed less than the 1/4 of that random generated sentence,
                    # notice him to try again
                    elif len(list(rewritten)) <= one_fourth:
                        print('You have rewritten less than one fourth of the whole text, we want you to try again !!!')
                        test()

                    # if the test has turned out well, if he completed it, ask him to try again with the same sentence
                    def try_again():
                        print('')
                        again_same = input('Wanna try the same sentence again or to try the new one? again/new: ').upper()

                        # if he want's to try again with the same sentence call the test() function
                        if again_same == 'AGAIN':
                            test()

                        # if new just pass, 'cause we are running the infinite loop, so when everything has been passed, it will start all over again
                        elif again_same == 'NEW':
                            pass

                        # if he typed yes/no wrong, encourage him to type that again
                        else:
                            print('')
                            print('You have printed again/new wrong, try again !!!')
                            try_again()

                    try_again()


                test()


            # if the player doesn't want to begin the test, then just exit the program
            elif begin == 'NO':
                print('You have decided to leave.')
                exit()

            # if he typed something other than yes/no, encourage him to try that again
            else:
                print('You have typed Yes/No wrong, try again !!!')
                infinite_loop()


    infinite_loop()

typing_test()

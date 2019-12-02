""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
def lines_from_file(path):
    file = open(path)
    assert readable(file), "The file is not readable."
    line = readlines(file)
    wo_blank = []
    for i in line:
        wo_blank += [strip(i)]
    return wo_blank

def new_sample(path, i):
    return lines_from_file(path)[i]

def analyze(sample_paragraph, typed_string, start_time, end_time):
    def words_per_minute(string, seconds):
        word_length = len(string)/5
        return word_length/(seconds/60)

    def accuracy_percentage(correct_string, typed_string):
        if strip(typed_string) == "":
            return 0.0
        correct_words = split(correct_string)
        typed_words = split(typed_string)
        length = min(len(correct_words), len(typed_words))
        right_count = 0
        for i in range(length):
            if correct_words[i] == typed_words[i]:
                right_count += 1
        return right_count / length * 100

    return [words_per_minute(typed_string, end_time-start_time), accuracy_percentage(sample_paragraph, typed_string)]

def pig_latin(word):
    vowels = ["a", "e", "i", "o", "u"]
    def find_vowel(string):
        for letter in string:
            if letter in vowels:
                return string.index(letter)
        return len(string)+1
    vowel_place = find_vowel(word)
    if vowel_place == 0:
        return word + "way"
    else :
        consanants = word[:vowel_place]
        others = word[vowel_place:]
        return others + consanants + "ay"

def autocorrect(user_input,words_list,score_function):
    def key_of_min_value(d):
        return min(d, key=lambda x: d[x])

    if user_input in words_list:
        return user_input
    else:
        d = {}
        for word in words_list:
            d[word] = score_function(user_input, word)
        return key_of_min_value(d)

def swap_score(str1, str2):
    def helper(w1, w2, score):
        if w1 == w2:
            return score
        elif w1 == "" or w2 == "":
            return score
        else:
            if w1[0] == w2[0]:
               return helper(w1[1:], w2[1:], score)
            else:
                return helper(w1[1:], w2[1:], score=score+1)

    return helper(str1, str2, score=0)
# END Q1-5

# Question 6
def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if word1 == "": # Fill in the condition
        # BEGIN Q6
        return len(word2)
        # END Q6

    elif word2 == "": # Feel free to remove or add additional cases
        # BEGIN Q6
        return len(word1)
        # END Q6

    elif word1[0] == word2[0]:
        return score_function(word1[1:], word2[1:])

    else:
        add_char = score_function(word1, word2[1:])  # Fill in these lines
        remove_char = score_function(word1[1:], word2) 
        substitute_char = score_function(word1[1:], word2[1:]) 
        # BEGIN Q6
        return 1 + min(add_char, remove_char, substitute_char)
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
def score_function_accurate(word1, word2):

    if word1 == "": 
        return len(word2)
        
    elif word2 == "": 
        return len(word1)
        
    elif word1[0] == word2[0]:
        return score_function_accurate(word1[1:], word2[1:])

    else:
        distance = KEY_DISTANCES[word1[0], word2[0]]
        add_char = score_function_accurate(word1, word2[1:])  
        remove_char = score_function_accurate(word1[1:], word2) 
        substitute_char = score_function_accurate(word1[1:], word2[1:])
        return min(add_char + 1, remove_char + 1, substitute_char + distance)

word_dict = {}

def score_function_final(word1, word2):
    if word1 == "": 
        return len(word2)
        
    elif word2 == "": 
        return len(word1)
        
    elif word1[0] == word2[0]:
        return score_function_final(word1[1:], word2[1:])

    else:
        if (word1, word2) not in word_dict:
            distance = KEY_DISTANCES[word1[0], word2[0]]
            add_char = score_function_final(word1, word2[1:])  
            remove_char = score_function_final(word1[1:], word2) 
            substitute_char = score_function_final(word1[1:], word2[1:])
            score = min(add_char + 1, remove_char + 1, substitute_char + distance)
            word_dict[(word1, word2)] = score            
        return word_dict[(word1, word2)]
# END Q7-8

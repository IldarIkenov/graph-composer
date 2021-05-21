import string
from graph import Graph, Vertex
import random
import re
import os

def get_words_from_text(text_path):
    with open(text_path, 'r') as f: 
        text = f.read()

        # remove [text in here]
        text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split()) # turn whitespace into just spaces
        text = text.lower() # make everything lowercase to compare stuff
        # for example: Hello! it's me --> hello its me 
        text = text.translate(str.maketrans('', '', string.punctuation))
    
    words = text.split() # split on spaces again
    return words

def make_graph(words):
    g = Graph()

    previous_word = None

    # for each  word
    for word in words:
        word_vertex = g.get_vertex(word) # check that is in tle graph, and if not then add it

        if previous_word:
            previous_word.increment_edge(word_vertex) 

        previous_word = word_vertex # set our word to the previous and iterate

    g.generate_probability_mappings()

    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words)) # pick a random word to start
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    
    return composition

def main(artist):
    # get words from text
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    #for song lyrics
    words = []
    for song_file in os.listdir(f'songs/{artist}'):
        if song_file == '.DS_Store':
            continue
        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extend(song_words)

    # make a graph using those words
    g = make_graph(words)

    # get the next word for x number of words (defined by used)
    # show the user
    composition = compose(g, words, 100)
    return ' '.join(composition) # return a string, where all the words are separated by a space

if __name__ == '__main__':
    print(main('taylor_swift')) # enter any artist in the list
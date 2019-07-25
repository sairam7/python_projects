from collections import Counter
import matplotlib.pyplot as plt

def get_word_count(filename):
    word_counter=0
    open_file = open(filename,'r')
    get_contents = open_file.read()
    open_file.close()
    get_unique_word_list = set(get_contents.split())
    counter_loop = Counter(get_contents.split())
    #print(list(counter_loop.values()))
    plt.xticks(range(len(counter_loop)),list(counter_loop.values()))
    plt.show()

    for unique_word in get_unique_word_list:
        word_counter+=1
    print (word_counter)

get_word_count('sample_text.txt')
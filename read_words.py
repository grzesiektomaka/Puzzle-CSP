
def read_words(words_file_name):
    words_list = []
    file = open(words_file_name, "r")

    for row in file:
        for word in row.split():
            words_list.append(word)

    return words_list

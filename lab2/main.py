import re
import string
from pathlib import Path
from common import common


def get_text_from_file(filename):
    return Path(f'./documents/{filename}').read_text()


def split_to_words(sentence):
    return list(set((filter(lambda w: len(w) > 0, [re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w) for w in sentence.lower().split()]))))


def create_index(filenames, index, file_titles):
    if index is None:
        index = {}
    if file_titles is None:
        file_titles = {}
    for file in filenames:
        filetext = get_text_from_file(file)
        headline = filetext.split("\n")[0]
        file_titles[file] = headline
        words = split_to_words(filetext)
        for word in words:
            if word not in index:
                index[word] = []
            index[word].append(file)


def search(index, query):
    results = None
    query_words = split_to_words(query)
    for query_word in query_words:
        if query_word in index:
            current_list = index[query_word]
        else:
            current_list = []
        if current_list is None:
            continue
        if results is None:
            results = current_list
            continue
        results = common(results, current_list)
    return results


def get_summary_from_results(filenames, file_titles):
    result = []
    for filename in filenames:
        result.append({'filename': filename, 'content': file_titles[filename]})
    return result


def run():
    index = {}
    file_titles = {}
    list_of_filenames = ["file1.txt", "file2.txt", "file3.txt"]
    create_index(list_of_filenames, index, file_titles)
    while True:
        user_input = input("Enter search query, please\n")
        if len(user_input) < 1:
            break
        found_filenames = search(index, user_input)
        print(get_summary_from_results(found_filenames, file_titles))


run()
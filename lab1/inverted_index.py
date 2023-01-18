import json


def inverted_index_data(data):
    indexes = {}
    for item in data:
        words = get_keywords_from_doc(data)
        for word in words:
            if word not in indexes:
                indexes[word] = []
            indexes[word].append(get_item_id(item))
    return indexes


def get_item_id(item):
    return item['id']


def get_item_keywords(item):
    return item['keywords']


def search_in_inverted_index(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return []


def main():
    f = open('./data.json')
    data = json.load(f)
    
    inverted_index = inverted_index_data(documents)
    results = search_in_inverted_index(built_inverted_index, 'family')

    print(inverted_index)
    print(results)


main()
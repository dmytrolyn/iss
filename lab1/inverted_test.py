from inverted_index import inverted_index_data, search_in_inverted_index
import json


file = open("./data.json")
data = json.load(file)
inverted_index = inverted_index_data(data)


def test_index():
    assert inverted_index == {'opinions': [1],
                            "world": [1],
                            "frankness": [1],
                            "active": [1],
                            "extent": [1],
                            "excellence": [1],
                            "settle": [1],
                            "fifteen": [2],
                            "mistake": [2],
                            "end": [2],
                            "fat": [2],
                            "assistance": [2],
                            "neat": [2],
                            "raptures": [2],
                            "result": [3],
                            "valley": [3],
                            "family": [3],
                            "knowledge": [3],
                            "house": [3],
                            "expenses": [3],
                            "rank": [3],
                            "passage": [3],
                            "addition": [4], 
                            "newspaper": [4],
                            "size": [4],
                            "relation": [4],
                            "stuff": [4],
                            "help": [4],
    }

def test_search():
    assert search_in_inverted_index(inverted_index, 'extent') == [1]
    assert search_in_inverted_index(inverted_index, 'knowledge') == [3]
    assert search_in_inverted_index(inverted_index, 'test') == []

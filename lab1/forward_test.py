from forward_index import forward_index_data, search_in_forward_index
import json

file = open('./data.json')
documents = json.load(file)
forward_index = forward_index_data(documents)
      
def test_index():
    assert forward_index == [
        {'id': 1, 'words': ['world', 'frankness', 'active', 'extent', 'excellence', 'settle']},
        {'id': 2, 'words': ['fifteen', 'mistake', 'end', 'fat', 'assistance', 'neat', 'raptures']},
        {'id': 3, 'words': ['result', 'valley', 'family', 'knowledge', 'house', 'expenses', 'rank', 'passage']},
        {'id': 4, 'words': ['addition', 'newspaper', 'size', 'relation', 'stuff', 'help']}]

def test_search():
 assert search_in_forward_index(forward_index, 'world') == [1]
 assert search_in_forward_index(forward_index, 'relation') == [4]
 assert search_in_forward_index(forward_index, 'end') == [2]
 assert search_in_forward_index(forward_index, 'rank') == [3]

    
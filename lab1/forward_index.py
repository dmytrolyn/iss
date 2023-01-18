import json


def forward_index_data(data):
 indexes = []
 for item in data:
  index = {'id': get_item_id(item), 'words': get_item_keywords(item)}
  indexes.append(index)
 return indexes


def get_item_id(item):
 return item['id']


def get_item_keywords(item):
 return item['keywords']


def search_in_forward_index(index, keyword):
 result_indexes = []
 for row in index:
     if keyword in row['words']:
         result_indexes.append(row['id'])
 return result_indexes


def main():
 file = open('./data.json')
 data = json.load(file)

 forward_index = forward_index_data(data)
 results = search_in_forward_index(forward_index, 'relation')

 print(forward_index)
 print(results)


main()
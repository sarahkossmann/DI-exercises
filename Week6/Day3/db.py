import json

def create_db(dst_file='my_file.json'):
    data = [
        {
            'id' : 0,
            'name' : 'Red wine',
            'price' : 25,
            'instock': 3,
            'image':"x"
        },
        {
            'id': 1,
            'name': 'Penne Pasta',
            'price': 3,
            'instock': 3,
            'image': "x"
        },
        {
            'id': 2,
            'name': 'Parmesan Cheese',
            'price': 4,
            'instock': 3,
            'image': "x"
        },
    ]

    with open(dst_file, 'w') as f:
        json.dump(data, f, indent=4)

def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data
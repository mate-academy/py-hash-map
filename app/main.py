from app.hashtable import Hashtable


class Dictionary:
    list_nodes = []

    def __init__(self, *args, **kwargs):
        Dictionary.list_nodes += [kwargs]

    def __setitem__(self, key, value):
        Dictionary.list_nodes.append((key, value))
        hash_table = Hashtable(Dictionary.list_nodes)

    def __getitem__(self, key):
        return self.key

    def __len__(self):
        return len(Dictionary.list_nodes)


# name_data = Dictionary()

# name_data[4] = 10

# print(name_data[4])


def the_same(something):
    print(something)

the_same([(123123, "awdawd"), (1231, "fweww")])

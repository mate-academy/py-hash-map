import copy
import random

hash_table = [[] for i in range(8)]  # [key #value #hash]
capacity = len(hash_table)
resize_breakpoint = 2 / 3
current_load_factor = (capacity - hash_table.count([])) / capacity


def new_elem(key, value, self=None):
    print(key, value)
    # self key value -> key, value, and hash
    new_element = [key, value, hash(key)]
    elem_index = new_element[2] % capacity

    if len(hash_table[elem_index]) > 0:
        hash_table[hash_table.index([])] = new_element
    else:
        hash_table[elem_index] = new_element

    print(f"CHECK {current_load_factor} and {resize_breakpoint}")
    if current_load_factor > resize_breakpoint:
        print("RESIZE")
        hash_table += [[] for i in range(capacity)]
        capacity *= 2

    print(f"hash: {hash_table}\ncapacity: {capacity}\n"
          f"current_load_factor: {current_load_factor}")
    print("______")


new_elem("key", "value")
new_elem("key", "value")
new_elem("key", "value")
new_elem("key", "value")


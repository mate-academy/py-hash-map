class Dictionary:
    def __init__(self):
        self.current_capacity = 8
        self.elements = [None for _ in range(self.current_capacity)]
        self.length = 0

    def __setitem__(self, key, value):
        self.check_and_resize()
        self.add_element(key, value)

    def add_element(self, key, value):
        hash_code = hash(key)
        input_index = hash_code % self.current_capacity
        while True:
            if self.elements[input_index] is None:
                self.elements[input_index] = [key, value, hash_code]
                self.length += 1
                break
            if self.elements[input_index][0] == key \
                    and self.elements[input_index][2] == hash_code:
                self.elements[input_index][1] = value
                break
            input_index = (input_index + 1) % self.current_capacity

    def check_and_resize(self):
        if self.length == int(self.current_capacity * 2 / 3):
            self.current_capacity *= 2
            temp_elements = [element for element in self.elements
                             if element is not None]
            self.elements = [None for _ in range(self.current_capacity)]
            self.length = 0
            for item in temp_elements:
                self.add_element(item[0], item[1])

    def __getitem__(self, key):
        hash_code = hash(key)
        output_index = hash_code % self.current_capacity
        while self.elements[output_index] is not None:
            if self.elements[output_index][0] == key \
                    and self.elements[output_index][2] == hash_code:
                return self.elements[output_index][1]
            output_index = (output_index + 1) % self.current_capacity
        raise KeyError("Element is not present in dict.")

    def __len__(self):
        return self.length

    def clear(self):
        self.length = 0
        self.current_capacity = 8
        self.elements = [None for _ in range(self.current_capacity)]

    def __delitem__(self, key):
        hash_code = hash(key)
        output_index = hash_code % self.current_capacity
        while self.elements[output_index] is not None:
            if self.elements[output_index][0] == key \
                    and self.elements[output_index][2] == hash_code:
                self.elements[output_index] = None
                break
            output_index = (output_index + 1) % self.current_capacity
        raise KeyError("Element is not present in dict.")

    def get(self, key, *args):
        hash_code = hash(key)
        output_index = hash_code % self.current_capacity
        while self.elements[output_index] is not None:
            if self.elements[output_index][0] == key \
                    and self.elements[output_index][2] == hash_code:
                return self.elements[output_index][1]
            output_index = (output_index + 1) % self.current_capacity
        return None if len(args) == 0 else args[0]

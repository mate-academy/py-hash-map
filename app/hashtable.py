import pprint


class Hashtable:
    def __init__(self, elements):
        table_size = 8
        table_resize = table_size * 2/3
        while len(elements) > table_resize:
            table_size *= 2
        self.bucket_size = table_size
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)

    def _assign_buckets(self, elements):
        self.buckets = [None] * self.bucket_size

        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size

            while self.buckets[index] is not None:
                print(f"The key {key} collided with {self.buckets[index]}")
                index = (index + 1) % self.bucket_size

            self.buckets[index] = (key, value,)

    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == input_key:
                return value
            index = (index + 1) % self.bucket_size

    def __str__(self):
        return pprint.pformat(self.buckets)

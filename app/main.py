import pprint


class Dictionary:
    def __init__(self, elements):
        self.len_bucket = len(elements)
        self.bucket_size = 8
        self.bucket_resize = self.bucket_size * 2/3
        while self.len_bucket > self.bucket_resize:
            self.bucket_size *= 2
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)
        self.len_bucket = len([full_bucket for full_bucket in self.buckets if full_bucket is not None])

    def _assign_buckets(self, elements):
        self.buckets = [None] * self.bucket_size

        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size

            while self.buckets[index] is not None:
                print(f"The key {key} collided with {self.buckets[index]}")
                index = (index + 1) % self.bucket_size

            self.buckets[index] = (key, value,)

    def __setitem__(self, key, value):
        while self.len_bucket > self.bucket_resize:
            self.bucket_size *= 2
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets((key, value))

    def __getitem__(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == input_key:
                return value
            index = (index + 1) % self.bucket_size

    def __str__(self):
        return pprint.pformat(self.buckets)

    def __len__(self):
        return self.len_bucket

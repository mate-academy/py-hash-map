class Dictionary:
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [None for _ in range(self.bucket_size)]
        self.assign_buckets(elements)

    def assign_buckets(self, elements):
        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size
            self.buckets[index].append((key, value))

    def __getitem__(self, key):
        hashed_value = hash(key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for bucket_key, bucket_value in bucket:
            if bucket_key == key:
                return bucket_value
        return None

    def __len__(self):
        return len(self.buckets)




class Hashtable:
    def __init__(self, elements):
        self.bucket_size = len(elements) * 2
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

            self.buckets[index] = ((key, value))
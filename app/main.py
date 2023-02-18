import pprint


class Dictionary:
    def __init__(self, elements):
        self.bucket_size = 8
        self.bucket_resize = self.bucket_size * 2/3
        while len(elements) > self.bucket_resize:
            self.bucket_size *= 2
        self.buckets = [[] for i in range(self.bucket_size)]
        self.len_bucket = 0
        self._assign_buckets(elements)

    def _assign_buckets(self, elements):
        print(self.len_bucket)
        if not self.len_bucket:
            self.buckets = [None] * self.bucket_size

        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size

            while self.buckets[index] is not None:
                index = (index + 1) % self.bucket_size

            self.buckets[index] = (key, value,)

    def get_buckets_full(self):
        return [full_bucket for full_bucket in self.buckets if full_bucket is not None]

    def resize(self):
        while self.len_bucket > self.bucket_resize:
            self.bucket_size *= 2
        self.buckets = [[] for i in range(self.bucket_size)]

    def __setitem__(self, key, value):
        self.len_bucket = len(self.get_buckets_full())
        current_buckets = []
        if self.len_bucket > self.bucket_resize:
            current_buckets = self.get_buckets_full()
            current_buckets += [(key, value)]
            self.resize()
            self._assign_buckets(current_buckets)
        else:
            self._assign_buckets([(key, value)])

    def __getitem__(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == input_key:
                return value
            index = (index + 1) % self.bucket_size

    def __str__(self):
        return pprint.pformat(self.buckets)#pprint.pformat(self.get_buckets_full())

    def __len__(self):
        return len(self.get_buckets_full())


some_dict = Dictionary([("some", 1), (4, "1241"), ("the same", 3)])

print(some_dict)

some_dict[5] = "good idea"

some_dict[6] = "cool idea"

some_dict[7] = "bad idea"
# some_dict[8] = "great idea"
print(f"""
    
    {some_dict}
    
    {len(some_dict)}
    
    {some_dict["some"]}
    
    {some_dict}
""")

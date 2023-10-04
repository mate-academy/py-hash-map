from app.point import Point
class Dictionary:
    def __init__(self, size=8):
        self.data = size
        self.buckets = [[] for _ in range(self.data)]
        self.load_factor = 2/3

    def hash_data(self, key):
        return hash(key) % self.data

    def __setitem__(self, key, value):
        key_hash = self.hash_data(key)
        for i, (k, v) in enumerate(self.buckets[key_hash]):
            if k == key:
                self.buckets[key_hash][i] = (key, value)
                return
        self.buckets[key_hash].append((key, value))
        self.__check_load_factor__()


    def __getitem__(self, key):
        key_hash = self.hash_data(key)
        for k, v in self.buckets[key_hash]:
            if k == key:
                return v
        raise KeyError(f'Key not found: {key}')


    def __len__(self):
        total_count = 0
        for bucket in self.buckets:
            total_count += len(bucket)
        return total_count


    def __check_load_factor__(self):
        total_count = 0
        for bucket in self.buckets:
            total_count += len(bucket)
            if total_count > self.load_factor * self.data:
                self.__resize__()

    def __resize__(self):
        new_size = 2 * self.data
        new_bucket = [[] for _ in range(new_size)]

        for bucket in self.buckets:
            for key, value in bucket:
                new_key_hash = self.hash_data(key)
                new_bucket[new_key_hash].append((key, value))

        self.data = new_size
        self.buckets = new_bucket


my_dict = Dictionary()
my_dict.__setitem__(key=3, value="staho")
print(my_dict.__getitem__(key=3))
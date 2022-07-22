class Dictionary:

    def __init__(self):
        self.class_dict = {}

    def __setitem__(self, key, value):
        self.class_dict[key] = value

    def __getitem__(self, key):
        return self.class_dict[key]

    def clear(self):
        self.class_dict.clear()

    def __delitem__(self, key):
        del self.class_dict[key]

    def pop(self, *args, **kwargs):
        return self.class_dict.pop(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.class_dict.update(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.class_dict.get(*args, **kwargs)

    def __len__(self):
        return len(self.class_dict)

    def __iter__(self):
        return iter(self.class_dict)

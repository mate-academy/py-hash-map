class Dictionary:
    def __init__(self):
        self._hash_table_size = 8
        self._cells = [None] * self._hash_table_size

    @property
    def table(self):
        table = []
        for cell in self._cells:
            if cell is not None:
                key, _, value = cell
                table.append((key, value))

        return table

    def __setitem__(self, key, value):
        if self._is_necessary_hash_table_resizing():
            self._perform_hash_table_resize()

        self._fill_hash_table_cell(self._cells, key, value)

    def __getitem__(self, item):
        hashed_index = self._get_hashed_index(item)

        while self._cells[hashed_index] is not None:
            cell_key, cell_hash, cell_value = self._cells[hashed_index]
            if cell_key == item and cell_hash == hash(item):
                return cell_value
            hashed_index = (hashed_index + 1) % self._hash_table_size
        else:
            raise KeyError

    def __len__(self):
        return sum((cell is not None for cell in self._cells))

    def _get_hashed_index(self, key):
        hashed_key = hash(key)
        index = hashed_key % self._hash_table_size
        return index

    def _is_necessary_hash_table_resizing(self):
        threshold = int(2 / 3 * self._hash_table_size)

        if self.__len__() >= threshold:
            self._hash_table_size *= 2
            return True

        return False

    def _perform_hash_table_resize(self):
        new_cells = [None] * self._hash_table_size
        for cell in self._cells:
            if cell is not None:
                key, _, value = cell
                self._fill_hash_table_cell(new_cells, key, value)

        self._cells = new_cells

    def _fill_hash_table_cell(self, cell, key, value):
        hashed_index = self._get_hashed_index(key)

        while cell[hashed_index] is not None:
            cell_key, cell_hash, cell_value = cell[hashed_index]
            if cell_key == key:
                cell[hashed_index] = cell_key, cell_hash, value
                break
            else:
                hashed_index = (hashed_index + 1) % self._hash_table_size
        cell[hashed_index] = (key, hash(key), value)

    def clear(self):
        del self._cells
        self.__init__()

    def __delitem__(self, key):
        hashed_index = self._get_hashed_index(key)

        while self._cells[hashed_index] is not None:
            cell_key, cell_hash, cell_value = self._cells[hashed_index]
            if cell_key == key:
                self._cells[hashed_index] = None
                break
            else:
                hashed_index = (hashed_index + 1) % self._hash_table_size
        else:
            raise KeyError

    def __iter__(self):
        return iter(self.table)

    def get(self, key):
        return self.__getitem__(key)

    def pop(self, key):
        value = self.__getitem__(key)
        self.__delitem__(key)
        return value

    def update(self, key, value):
        self.__setitem__(key, value)

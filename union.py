class UnionGroup:
    class Union:
        def __init__(self, element):
            self.parent = self
            self.size = 1
            self.element = element

        def __repr__(self):
            return 'Union({!r}, size = {})'.format(self.element, self.size)

    def __init__(self, iterable=None):
        self.unions = {}
        if iterable is not None:
            self.make_sets(iterable)

    def make_set(self, element):
        self.unions[element] = self.Union(element)

    # def _find_union(self, element):
    #     for u in self.unions:
    #         if u.element == element:
    #             return u
    #     else:
    #         raise ValueError('{} not in this union group'.format(element))

    def find(self, element):
        set_ = self.unions[element]
        root = set_
        while root.parent != root:
            root = root.parent
        while set_.parent != root:
            set_.parent, set_ = root, set_.parent
        return root

    def union2(self, element1, element2):
        s1, s2 = self.find(element1), self.find(element2)
        if s1.size >= s2.size:
            s2.parent = s1
            s1.size += s2.size
        else:
            s1.parent = s2
            s2.size += s1.size

    def union(self, iterable):
        # sets = (self.find(x) for x in iterable)
        largest = max(iterable, key=lambda x: self.find(x).size)
        for x in iterable:
            if x != largest:
                self.union2(x, largest)

    def make_sets(self, iterable):
        for x in iterable:
            self.make_set(x)

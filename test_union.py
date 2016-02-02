import unittest
import union


class TestUnion(unittest.TestCase):
    def test_init(self):
        u = union.UnionGroup.Union('a')
        self.assertEqual(u.parent, u)
        self.assertEqual(u.size, 1)
        self.assertEqual(u.element, 'a')


class TestUnionGroup(unittest.TestCase):
    def test_find(self):
        ug = union.UnionGroup()
        ug.make_set('a')
        self.assertEqual(ug.find('a').element, 'a')

    def test_union2(self):
        ug = union.UnionGroup()
        ug.make_set('a')
        ug.make_set('b')
        ug.union2('a', 'b')
        self.assertEqual(ug.find('a'), ug.find('b'))
        self.assertEqual(ug.find('a').size, 2)

    def test_make_sets(self):
        ug = union.UnionGroup()
        ug.make_sets('abc')
        self.assertEqual(len(ug.unions), 3)

    def test_union_by_root(self):
        ug = union.UnionGroup()
        ug.make_sets('abcd')
        ug.union2('a', 'b')
        ug.union2('b', 'c')
        ug.union2('c', 'd')
        for x in 'abcd':
            self.assertEqual(ug.unions[x].parent, ug.unions['a'])

    def test_path_compression(self):
        ug = union.UnionGroup()
        ug.make_sets('abcd')
        ug.union2('a', 'b')
        ug.union2('c', 'd')
        ug.union2('a', 'c')
        self.assertNotEqual(ug.unions['d'].parent, ug.unions['a'])
        ug.find('d')
        self.assertEqual(ug.unions['d'].parent, ug.unions['a'])

    def test_union(self):
        ug = union.UnionGroup('abcdef')
        ug.union2('a', 'b')
        ug.union2('c', 'd')
        ug.union2('c', 'e')
        ug.union(['a', 'c', 'f'])
        for x in 'bcdef':
            self.assertEqual(ug.find(x), ug.find('a'))


if __name__ == '__main__':
    unittest.main()

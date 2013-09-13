"""
unit tests for sorting algorithms
"""

import unittest
import sorting.interfaces
import sorting.algorithms
import zope.interface

class _Prepare(unittest.TestCase):

    seq1 = None
    seq2 = None
    s = None

    def setUp(self):
        self.s = None
        self.seq1 = [MyItem(3), MyItem(33), MyItem(4), MyItem(98), MyItem(77),
                    MyItem(35), MyItem(9), MyItem(70), MyItem(34), MyItem(6),
                    MyItem(50), MyItem(36), MyItem(12), MyItem(1), MyItem(81),
                    MyItem(-50), MyItem(38), MyItem(212), MyItem(13), MyItem(-81),
                    MyItem(87), MyItem(32), MyItem(-12), MyItem(99), MyItem(181),
                    MyItem(52), MyItem(6), MyItem(12), MyItem(-1), MyItem(81),
                    MyItem(24), MyItem(33), MyItem(97), MyItem(11), MyItem(8)]
        self.seq2 = []
        for i in self.seq1:
            self.seq2.append(i)

    def tearDown(self):
        self.seq1 = None
        self.seq2 = None
        self.s = None

    def _testSortAsc(self):
        self.assertEquals(self.s.sortAsc(self.seq1), sorted(self.seq2))

    def _testSortDesc(self):
        self.assertEquals(self.s.sortDesc(self.seq1), list(reversed(sorted(self.seq2))))

class TestInsertSort(_Prepare):

    def setUp(self):
        _Prepare.setUp(self)
        self.s = sorting.algorithms.InsertSort(MyItemComparator())

    def test_sortAsc(self):
        self._testSortAsc()

    def test_sortDesc(self):
        self._testSortDesc()

class TestSelectionSort(_Prepare):

    def setUp(self):
        _Prepare.setUp(self)
        self.s = sorting.algorithms.SelectionSort(MyItemComparator())

    def test_sortAsc(self):
        self._testSortAsc()

    def test_sortDesc(self):
        self._testSortDesc()

class TestBubbleSort(_Prepare):

    def setUp(self):
        _Prepare.setUp(self)
        self.s = sorting.algorithms.BubbleSort(MyItemComparator())

    def test_sortAsc(self):
        self._testSortAsc()

    def test_sortDesc(self):
        self._testSortDesc()

class TestQuickSort(_Prepare):

    def setUp(self):
        _Prepare.setUp(self)
        self.s = sorting.algorithms.QuickSort(MyItemComparator())

    def test_sortAsc(self):
        self._testSortAsc()

    def test_sortDesc(self):
        self._testSortDesc()

class TestHeapSort(_Prepare):

    def setUp(self):
        _Prepare.setUp(self)
        self.s = sorting.algorithms.HeapSort(MyItemComparator())

    def test_sortAsc(self):
        self._testSortAsc()

    def test_sortDesc(self):
        self._testSortDesc()

class TestMergeSort(_Prepare):

    def setUp(self):
        _Prepare.setUp(self)
        self.s = sorting.algorithms.MergeSort(MyItemComparator())

    def test_sortAsc(self):
        self._testSortAsc()

    def test_sortDesc(self):
        self._testSortDesc()

class MyItem(object):

    value = None

    def __init__(self, v):
        self.value = v

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def __cmp__(self, other):
        return self.value.__cmp__(other.value)

class MyItemComparator(object):

    zope.interface.implements(sorting.interfaces.Comparator)

    def compare(self, o1, o2):
        return o1.value.__cmp__(o2.value)

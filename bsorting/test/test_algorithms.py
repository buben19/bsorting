"""
unit tests for sorting algorithms
"""

import unittest
import random
import bsorting.interfaces
import bsorting.algorithms
import zope.interface

class _Prepare(unittest.TestCase):

    # cardinality of sorted sequences
    SEQ_CARDINALITY = 100

    # boudary valuest of sorted sequences
    SEQ_MIN_VALUE = -100
    SEQ_MAX_VALUE = 100

    seq1 = None
    seq2 = None
    s = None

    def setUp(self):
        self.s = None

        # create sequnce 1
        self.seq1 = []
        for i in xrange(self.SEQ_CARDINALITY):
            self.seq1.append(MyItem(random.randint(self.SEQ_MIN_VALUE, self.SEQ_MAX_VALUE)))

        # create sequence 2
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
        self.s = bsorting.algorithms.InsertSort(MyItemComparator())

    def test_sortAsc(self):
        self._testSortAsc()

    def test_sortDesc(self):
        self._testSortDesc()

class TestSelectionSort(_Prepare):

    def setUp(self):
        _Prepare.setUp(self)
        self.s = bsorting.algorithms.SelectionSort(MyItemComparator())

    def test_sortAsc(self):
        self._testSortAsc()

    def test_sortDesc(self):
        self._testSortDesc()

class TestBubbleSort(_Prepare):

    def setUp(self):
        _Prepare.setUp(self)
        self.s = bsorting.algorithms.BubbleSort(MyItemComparator())

    def test_sortAsc(self):
        self._testSortAsc()

    def test_sortDesc(self):
        self._testSortDesc()

class TestQuickSort(_Prepare):

    def setUp(self):
        _Prepare.setUp(self)
        self.s = bsorting.algorithms.QuickSort(MyItemComparator())

    def test_sortAsc(self):
        self._testSortAsc()

    def test_sortDesc(self):
        self._testSortDesc()

class TestHeapSort(_Prepare):

    def setUp(self):
        _Prepare.setUp(self)
        self.s = bsorting.algorithms.HeapSort(MyItemComparator())

    def test_sortAsc(self):
        self._testSortAsc()

    def test_sortDesc(self):
        self._testSortDesc()

class TestMergeSort(_Prepare):

    def setUp(self):
        _Prepare.setUp(self)
        self.s = bsorting.algorithms.MergeSort(MyItemComparator())

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

    zope.interface.implements(bsorting.interfaces.IComparator)

    def compare(self, o1, o2):
        return o1.value.__cmp__(o2.value)

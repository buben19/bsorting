"""
implemantation of sorting algorithms
"""

import bsorting.interfaces
import zope.interface


class Sort(object):
    """
    abstract base class for sorting algorithms
    """

    zope.interface.implements(bsorting.interfaces.ISorting)

    comparator = None

    def __init__(self, comparator):
        if self.__class__ is Sort:
            raise NotImplementedError, self.__class__.__name__ + "is abstract"
        else:
            self.comparator = comparator

class InsertSort(Sort):
    """
    implementation of insert sort algorithm
    """

    def sortAsc(self, seq):
        return self.__insertSort(seq, -1)

    def sortDesc(self, seq):
        return self.__insertSort(seq, 1)

    def __insertSort(self, seq, order):
        for i in xrange(len(seq) - 1):
            j = i + 1
            tmp = seq[j]
            while j > 0 and (self.comparator.compare(tmp, seq[j - 1]) == order):
                seq[j] = seq[j - 1]
                j -= 1
            seq[j] = tmp
        return seq

class SelectionSort(Sort):

    def sortAsc(self, seq):
        return self.__selectionSort(seq, -1)

    def sortDesc(self, seq):
        return self.__selectionSort(seq, 1)

    def __selectionSort(self, seq, order):
        for i in xrange(len(seq) - 1):
            minIndex = i
            for j in xrange(i + 1, len(seq)):
                if self.comparator.compare(seq[j], seq[minIndex]) == order:
                    minIndex = j
            (seq[i], seq[minIndex]) = (seq[minIndex], seq[i])
        return seq

class BubbleSort(Sort):

    def sortAsc(self, seq):
        return self.__bubbleSort(seq, 1)

    def sortDesc(self, seq):
        return self.__bubbleSort(seq, -1)

    def __bubbleSort(self, seq, order):
        for i in xrange(len(seq) - 1):
            for j in xrange(len(seq) - i - 1):
                if self.comparator.compare(seq[j], seq[j + 1]) == order:
                    (seq[j], seq[j + 1]) = (seq[j + 1], seq[j])
        return seq

class QuickSort(Sort):

    def sortAsc(self, seq):
        return self.__quickSort(seq, 0, len(seq), -1)

    def sortDesc(self, seq):
        return self.__quickSort(seq, 0, len(seq), 1)

    def __quickSort(self, seq, left, right, order):
        if left < right:
            boundary = left
            for i in xrange(left + 1, right):
                if self.comparator.compare(seq[i], seq[left]) == order:
                    boundary += 1
                    (seq[i], seq[boundary]) = (seq[boundary], seq[i])
            (seq[left], seq[boundary]) = (seq[boundary], seq[left])
            self.__quickSort(seq, left, boundary, order)
            self.__quickSort(seq, boundary + 1, right, order)
            return seq

class HeapSort(Sort):

    def sortAsc(self, seq):
        return self.__heapSort(seq, -1)

    def sortDesc(self, seq):
        return self.__heapSort(seq, 1)

    def __heapSort(self, seq, order):
        for i in xrange(len(seq) / 2 - 1, -1, -1):
            self.__repairTop(seq, len(seq) - 1, i, order)
        for i in xrange(len(seq) - 1, 0, -1):
            (seq[0], seq[i]) = (seq[i], seq[0])
            self.__repairTop(seq, i - 1, 0, order)
        return seq

    def __repairTop(self, seq, bottom, topIndex, order):
        """
        repair heap
        """
        tmp = seq[topIndex]
        success = topIndex * 2 + 1
        if success < bottom and self.comparator.compare(seq[success], seq[success + 1]) == order:
            success += 1
        while success <= bottom and self.comparator.compare(tmp, seq[success]) == order:
            seq[topIndex] = seq[success]
            topIndex = success
            success = success * 2 + 1
            if success < bottom and self.comparator.compare(seq[success], seq[success + 1]) == order:
                success += 1
        seq[topIndex] = tmp

class MergeSort(Sort):

    def sortAsc(self, seq):
        return self.__mergeSort(seq, [None] * len(seq), 0, len(seq) - 1, -1)

    def sortDesc(self, seq):
        return self.__mergeSort(seq, [None] * len(seq), 0, len(seq) - 1, 1)

    def __mergeSort(self, seq, aux, left, right, order):
        if left == right:
            return
        else:
            middleIndex = (left + right) / 2
            self.__mergeSort(seq, aux, left, middleIndex, order)
            self.__mergeSort(seq, aux, middleIndex + 1, right, order)
            self.__merge(seq, aux, left, right, order)
            for i in xrange(left, right + 1):
                seq[i] = aux[i]
            return seq

    def __merge(self, seq, aux, left, right, order):
        middleIndex = (left + right) / 2
        leftIndex = left
        rightIndex = middleIndex + 1
        auxIndex = left
        while (leftIndex <= middleIndex) and (rightIndex <= right):
            if self.comparator.compare(seq[leftIndex], seq[rightIndex]) == order:
                aux[auxIndex] = seq[leftIndex]
                leftIndex += 1
            else:
                aux[auxIndex] = seq[rightIndex]
                rightIndex += 1
            auxIndex += 1
        while leftIndex <= middleIndex:
            aux[auxIndex] = seq[leftIndex]
            leftIndex += 1
            auxIndex += 1
        while rightIndex <= right:
            aux[auxIndex] = seq[rightIndex]
            rightIndex += 1
            auxIndex += 1
        return seq

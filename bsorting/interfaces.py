"""
interface definition for sorting library
"""

import zope.interface

class ISorting(zope.interface.Interface):

    def sortAsc(seq):
        """
        sort sequence in ascending order
        """

    def sortDesc(seq):
        """
        sort sequence in descending order
        """

class IComparator(zope.interface.Interface):

    def compare(o1, o2):
        """
        compare two elements
        returns:
            0   - o1 == o2
            1   - o1 > o2
            -1  - o1 < o2
        """

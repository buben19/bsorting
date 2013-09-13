# bsorting - Python library of sorting algoritms

bsorting is library providing couple of sorting algorithms with easy to use
API. All what you need is create comparator class for your objects, give its
instace to sorting algoritms a start sorting.

```pycon
import random
from bsorting.algorithms import *

class Car(object):
    def __init__(self, doors):
        self.doors = doors

    def __unicode__(self):
        return "doors: %d" % self.doors

    def __str__(self):
        return unicode(self).encode("utf-8")

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, str(self))

class CarComparator(object):
    def compare(self, car1, car2):
        return cmp(car1.doors, car2.doors)

# generate some cars
cars = [Car(int(random.random() * 5)) for i in xrange(10)]

# create Bubble sort for sorting cars
carSorter = BubbleSort(CarComparator())

# sort them
for car in carSorter.sortAsc(cars):
    print repr(car)
```

### Implemented algoritms

bsorting.algorithms provides follwing list of sorting algorithms:

    BubbleSort
    HeapSort
    InsertSort
    MergeSort
    QuickSort
    SelectionSort


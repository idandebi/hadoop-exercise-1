#!/usr/bin/env python
"""reducer.py"""

from itertools import groupby
from operator import itemgetter
import sys


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    data = sorted(data, key=itemgetter(0))

    word_counts = []

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            word_counts.append((current_word, total_count))
        except ValueError:
            pass

    word_counts.sort(key=lambda x: x[1], reverse=True)

    top_n = 3
    for word, total in word_counts[:top_n]:
        print("%s%s%d" % (word, separator, total))


if __name__ == "__main__":
    main()

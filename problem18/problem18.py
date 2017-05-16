#!/usr/bin/python


def problem18():
    with open("tree.txt") as f:
        tree = f.readlines()

    prev_row = None
    for row in reversed(tree):
        row = [int(x) for x in row.split(' ')]
        if prev_row:
          for x in range(0, len(row)):
              row[x] = row[x] + max(prev_row[x], prev_row[x + 1])
        prev_row = row
    print "solution = %s" % prev_row[0]


if __name__ == "__main__":
    problem18()

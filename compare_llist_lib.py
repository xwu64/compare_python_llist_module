from llist import sllist
from pyllist import sllist as pyllist
from cllist import sllist as csllist

from time import time_ns
from numpy import random
import matplotlib.pyplot as plt

random.seed(0)

print('llist pyllist csllist')

print('Append left')

sizes = []
time_sllist = []
time_pyllist = []
time_csllist = []

for i in range(2, 7):
    ROUND = 10 ** i
    sizes.append(ROUND)
    print("size=", ROUND)
    tick = time_ns()
    l = sllist()
    for i in range(ROUND):
        l.appendleft(i)
    tock = time_ns()
    time_sllist.append(tock - tick)
    print(tock - tick)

    tick = time_ns()
    l = pyllist()
    for i in range(ROUND):
        l.appendleft(i)
    tock = time_ns()
    time_pyllist.append(tock - tick)
    print(tock - tick)

    tick = time_ns()
    l = csllist()
    for i in range(ROUND):
        l.appendleft(i)
    tock = time_ns()
    time_csllist.append(tock - tick)
    print(tock - tick)
    print('='*10)

plt.plot(sizes, time_sllist, marker='x')
plt.plot(sizes, time_pyllist, marker='x')
plt.plot(sizes, time_csllist, marker='x')
plt.legend(['llist', 'pyllist', 'cllist'])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of appended node')
plt.ylabel('Execution time (ns)')
plt.title('Comparison of appendleft function')
plt.show()

print('Append right')

sizes = []
time_sllist = []
time_pyllist = []
time_csllist = []

for i in range(2, 7):
    ROUND = 10 ** i
    sizes.append(ROUND)
    print("size=", ROUND)
    tick = time_ns()
    l = sllist()
    for i in range(ROUND):
        l.appendright(i)
    tock = time_ns()
    time_sllist.append(tock - tick)
    print(tock - tick)

    tick = time_ns()
    l = pyllist()
    for i in range(ROUND):
        l.appendright(i)
    tock = time_ns()
    time_pyllist.append(tock - tick)
    print(tock - tick)

    tick = time_ns()
    l = csllist()
    for i in range(ROUND):
        l.appendright(i)
    tock = time_ns()
    time_csllist.append(tock - tick)
    print(tock - tick)
    print('='*10)

plt.plot(sizes, time_sllist, marker='x')
plt.plot(sizes, time_pyllist, marker='x')
plt.plot(sizes, time_csllist, marker='x')
plt.legend(['llist', 'pyllist', 'cllist'])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of appended node')
plt.ylabel('Execution time (ns)')
plt.title('Comparison of appendright function')
plt.show()


print('pop left')

sizes = []
time_sllist = []
time_pyllist = []
time_csllist = []

for i in range(2, 7):
    ROUND = 10 ** i
    sizes.append(ROUND)
    print("size=", ROUND)
    l = sllist()
    for i in range(ROUND):
        l.appendright(i)
    tick = time_ns()
    while l.size > 0:
        l.popleft()
    tock = time_ns()
    time_sllist.append(tock - tick)
    print(tock - tick)

    l = pyllist()
    for i in range(ROUND):
        l.appendright(i)
    tick = time_ns()
    while l.size > 0:
        l.popleft()
    tock = time_ns()
    time_pyllist.append(tock - tick)
    print(tock - tick)

    l = csllist()
    for i in range(ROUND):
        l.appendright(i)
    tick = time_ns()
    while l.size > 0:
        l.popleft()
    tock = time_ns()
    time_csllist.append(tock - tick)
    print(tock - tick)
    print('='*10)

plt.plot(sizes, time_sllist, marker='x')
plt.plot(sizes, time_pyllist, marker='x')
plt.plot(sizes, time_csllist, marker='x')
plt.legend(['llist', 'pyllist', 'cllist'])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of appended node')
plt.ylabel('Execution time (ns)')
plt.title('Comparison of popleft function')
plt.show()

print('pop right')

sizes = []
time_sllist = []
time_pyllist = []
time_csllist = []

for i in range(2, 7):
    ROUND = 10 ** i
    sizes.append(ROUND)
    print("size=", ROUND)
    l = sllist()
    for i in range(ROUND):
        l.appendright(i)
    tick = time_ns()
    while l.size > 0:
        l.popright()
    tock = time_ns()
    time_sllist.append(tock - tick)
    print(tock - tick)

    l = pyllist()
    for i in range(ROUND):
        l.appendright(i)
    tick = time_ns()
    while l.size > 0:
        l.popright()
    tock = time_ns()
    time_pyllist.append(tock - tick)
    print(tock - tick)

    l = csllist()
    for i in range(ROUND):
        l.appendright(i)
    tick = time_ns()
    while l.size > 0:
        l.popright()
    tock = time_ns()
    time_csllist.append(tock - tick)
    print(tock - tick)
    print('='*10)

plt.plot(sizes, time_sllist, marker='x')
plt.plot(sizes, time_pyllist, marker='x')
plt.plot(sizes, time_csllist, marker='x')
plt.legend(['llist', 'pyllist', 'cllist'])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of pop node')
plt.ylabel('Execution time (ns)')
plt.title('Comparison of popright function')
plt.show()


print('remove')

sizes = []
time_sllist = []
time_pyllist = []
time_csllist = []

for i in range(2, 7):
    ROUND = 10 ** i
    sizes.append(ROUND)
    print("size=", ROUND)
    l = sllist()
    nodes = []
    for i in range(ROUND):
        l.appendright(i)
        nodes.append(l.last)
    random.shuffle(nodes)
    tick = time_ns()
    for node in nodes:
        l.remove(node)
    tock = time_ns()
    time_sllist.append(tock - tick)
    print(tock - tick)

    l = pyllist()
    nodes = []
    for i in range(ROUND):
        l.appendright(i)
        nodes.append(l.last)
    random.shuffle(nodes)
    tick = time_ns()
    for node in nodes:
        l.remove(node)
    tock = time_ns()
    time_pyllist.append(tock - tick)
    print(tock - tick)

    l = csllist()
    nodes = []
    for i in range(ROUND):
        l.appendright(i)
        nodes.append(l.last)
    random.shuffle(nodes)
    tick = time_ns()
    for node in nodes:
        l.remove(node)
    tock = time_ns()
    time_csllist.append(tock - tick)
    print(tock - tick)

    print('='*10)

plt.plot(sizes, time_sllist, marker='x')
plt.plot(sizes, time_pyllist, marker='x')
plt.plot(sizes, time_csllist, marker='x')
plt.legend(['llist', 'pyllist', 'cllist'])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of removed node')
plt.ylabel('Execution time (ns)')
plt.title('Comparison of remove function')
plt.show()

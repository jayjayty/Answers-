print("Hello World")
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
result1 = dict(sorted(d.items(), key=operator.itemgetter(1)))
result2 = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(result1)
print(result2)
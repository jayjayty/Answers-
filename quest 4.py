print("Hello world")
dict_a = {1: 20, 3: 10}
dict_b = {2: 40, 4: 50}
result = {}
for c in (dict_a, dict_b):
    result.update(c)
    print(c)


from collections import Counter, defaultdict

tests = [
    (111, 1023, 2420),
    (132, 2352, 6456),
    (342, 1234, 3453),
    (111, 3453, 1123),
    (243, 1251, 3453),
    (342, 1512, 3453),
    (111, 5532, 1453)
]
counter = Counter([test[0] for test in tests])
selected_tests = defaultdict(list)
for test in tests:
    if counter[test[0]] > 1 and len(selected_tests[test[0]]) < 2:
        selected_tests[test[0]].append(test)

print(selected_tests.values())

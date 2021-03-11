def check_leaves():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    pairs = []

    for i in range(len(digits)):
        for j in range(i + 1, len(digits), 1):
            pairs.append(str(digits[i]) + '-' + str(digits[j]))

    test_pairs = [
        [[[8], [9]], [[2], [7]], [[2], [3]], [[5], [9]], [[4], [6]], [[3], [5]], [[7], [9]], [[2], [9]], [[5], [8]],
         [[5], [6]], [[3], [9]], [[2], [5]], [[0], [9]], [[4], [9]], [[0], [5]], [[3], [7]], [[0], [2]], [[4], [8]],
         [[0], [1]], [[0], [8]], [[1], [6]], [[2], [8]], [[0], [7]], [[6], [8]], [[2], [4]], [[0], [6]], [[2], [6]],
         [[1], [9]], [[7], [8]], [[5], [7]], [[3], [8]], [[1], [2]], [[0], [3]], [[1], [4]], [[1], [5]], [[1], [8]],
         [[1], [7]], [[4], [7]], [[6], [9]], [[1], [3]], [[3], [4]], [[0], [4]], [[6], [7]], [[4], [5]], [[3], [6]]],
        [[[0], [6]], [[4], [9]], [[5], [9]], [[2], [7]], [[0], [9]], [[2], [5]], [[7], [9]], [[2], [4]], [[2], [3]],
         [[3], [9]], [[3], [7]], [[2], [9]], [[0], [5]], [[3], [5]], [[8], [9]], [[7], [8]], [[5], [6]], [[4], [6]],
         [[3], [8]], [[2], [8]], [[6], [8]], [[0], [2]], [[0], [8]], [[5], [8]], [[3], [4]], [[1], [6]], [[5], [7]],
         [[1], [2]], [[0], [7]], [[4], [8]], [[6], [9]], [[4], [5]], [[0], [3]], [[1], [9]], [[1], [5]], [[0], [4]],
         [[2], [6]], [[1], [4]], [[1], [8]], [[1], [7]], [[0], [1]], [[6], [7]], [[1], [3]], [[3], [6]], [[4], [7]]],
        [[[5], [9]], [[2], [8]], [[1], [6]], [[2], [7]], [[0], [7]], [[5], [8]], [[7], [9]], [[3], [9]], [[0], [2]],
         [[3], [5]], [[2], [9]], [[2], [3]], [[3], [7]], [[8], [9]], [[4], [9]], [[2], [5]], [[0], [9]], [[2], [4]],
         [[4], [8]], [[4], [7]], [[4], [6]], [[3], [8]], [[5], [6]], [[0], [5]], [[7], [8]], [[5], [7]], [[0], [8]],
         [[1], [8]], [[2], [6]], [[3], [4]], [[0], [4]], [[6], [9]], [[6], [8]], [[1], [5]], [[0], [1]], [[1], [4]],
         [[1], [9]], [[1], [2]], [[1], [7]], [[1], [3]], [[0], [6]], [[4], [5]], [[3], [6]], [[6], [7]], [[0], [3]]],
        [[[2], [7]], [[5], [9]], [[8], [9]], [[2], [5]], [[3], [9]], [[7], [9]], [[2], [9]], [[2], [6]], [[0], [5]],
         [[0], [2]], [[1], [6]], [[0], [6]], [[0], [9]], [[4], [9]], [[3], [7]], [[2], [3]], [[1], [9]], [[2], [8]],
         [[3], [5]], [[5], [8]], [[6], [8]], [[5], [6]], [[3], [8]], [[4], [8]], [[1], [2]], [[5], [7]], [[2], [4]],
         [[4], [6]], [[7], [8]], [[1], [5]], [[0], [8]], [[1], [4]], [[0], [4]], [[6], [9]], [[0], [7]], [[4], [5]],
         [[1], [8]], [[1], [3]], [[0], [3]], [[1], [7]], [[6], [7]], [[3], [4]], [[3], [6]], [[0], [1]], [[4], [7]]],
        [[[2], [5]], [[2], [3]], [[5], [8]], [[4], [9]], [[3], [7]], [[2], [7]], [[8], [9]], [[2], [9]], [[5], [9]],
         [[7], [9]], [[0], [5]], [[6], [8]], [[3], [9]], [[0], [2]], [[2], [4]], [[0], [9]], [[5], [6]], [[0], [6]],
         [[5], [7]], [[3], [5]], [[0], [8]], [[1], [6]], [[2], [8]], [[3], [8]], [[4], [8]], [[4], [5]], [[4], [6]],
         [[2], [6]], [[1], [2]], [[1], [5]], [[6], [7]], [[1], [4]], [[1], [9]], [[1], [7]], [[0], [4]], [[7], [8]],
         [[0], [1]], [[6], [9]], [[4], [7]], [[1], [8]], [[1], [3]], [[3], [4]], [[0], [7]], [[0], [3]], [[3], [6]]],
        [[[2], [3]], [[4], [9]], [[2], [9]], [[7], [9]], [[2], [7]], [[3], [7]], [[3], [5]], [[3], [9]], [[5], [9]],
         [[0], [6]], [[5], [8]], [[0], [9]], [[8], [9]], [[5], [6]], [[6], [8]], [[2], [6]], [[5], [7]], [[2], [5]],
         [[0], [5]], [[2], [8]], [[7], [8]], [[4], [8]], [[0], [2]], [[2], [4]], [[0], [8]], [[1], [7]], [[4], [6]],
         [[1], [6]], [[3], [8]], [[1], [5]], [[1], [8]], [[1], [4]], [[6], [9]], [[1], [2]], [[0], [1]], [[1], [9]],
         [[3], [4]], [[0], [7]], [[6], [7]], [[4], [5]], [[0], [3]], [[1], [3]], [[0], [4]], [[4], [7]], [[3], [6]]],
        [[[3], [9]], [[7], [9]], [[2], [5]], [[2], [3]], [[2], [7]], [[3], [5]], [[0], [6]], [[8], [9]], [[5], [8]],
         [[5], [9]], [[4], [7]], [[2], [9]], [[4], [9]], [[5], [6]], [[4], [8]], [[0], [9]], [[2], [6]], [[0], [2]],
         [[1], [6]], [[6], [8]], [[4], [5]], [[2], [8]], [[3], [8]], [[3], [7]], [[7], [8]], [[0], [8]], [[2], [4]],
         [[1], [2]], [[5], [7]], [[1], [9]], [[0], [7]], [[1], [8]], [[4], [6]], [[0], [4]], [[1], [5]], [[1], [4]],
         [[6], [9]], [[0], [1]], [[1], [3]], [[3], [4]], [[3], [6]], [[1], [7]], [[0], [5]], [[0], [3]], [[6], [7]]],
        [[[7], [9]], [[2], [9]], [[0], [5]], [[6], [8]], [[3], [9]], [[5], [9]], [[0], [8]], [[2], [7]], [[8], [9]],
         [[4], [9]], [[4], [8]], [[1], [7]], [[1], [5]], [[5], [8]], [[2], [3]], [[0], [2]], [[0], [9]], [[1], [6]],
         [[2], [8]], [[2], [5]], [[3], [7]], [[3], [5]], [[0], [7]], [[2], [4]], [[6], [9]], [[5], [7]], [[5], [6]],
         [[0], [1]], [[4], [6]], [[1], [2]], [[0], [6]], [[1], [9]], [[4], [5]], [[1], [4]], [[3], [8]], [[2], [6]],
         [[3], [4]], [[7], [8]], [[1], [8]], [[3], [6]], [[1], [3]], [[0], [3]], [[4], [7]], [[0], [4]], [[6], [7]]],
        [[[5], [9]], [[1], [6]], [[2], [3]], [[2], [9]], [[5], [8]], [[2], [7]], [[7], [9]], [[2], [5]], [[2], [8]],
         [[3], [5]], [[0], [6]], [[3], [7]], [[3], [9]], [[8], [9]], [[0], [7]], [[4], [6]], [[0], [9]], [[5], [7]],
         [[4], [8]], [[4], [9]], [[1], [8]], [[2], [6]], [[0], [2]], [[0], [8]], [[6], [8]], [[6], [9]], [[5], [6]],
         [[3], [8]], [[7], [8]], [[1], [7]], [[0], [5]], [[1], [4]], [[4], [5]], [[1], [9]], [[1], [2]], [[0], [3]],
         [[2], [4]], [[0], [4]], [[3], [6]], [[1], [5]], [[4], [7]], [[0], [1]], [[1], [3]], [[6], [7]], [[3], [4]]],
        [[[2], [3]], [[6], [8]], [[5], [8]], [[4], [9]], [[2], [8]], [[8], [9]], [[2], [7]], [[5], [9]], [[7], [9]],
         [[4], [8]], [[0], [2]], [[3], [9]], [[2], [9]], [[2], [5]], [[0], [9]], [[1], [7]], [[0], [8]], [[3], [5]],
         [[1], [9]], [[1], [6]], [[7], [8]], [[2], [4]], [[0], [4]], [[5], [6]], [[1], [2]], [[3], [8]], [[3], [7]],
         [[1], [4]], [[5], [7]], [[4], [6]], [[1], [5]], [[0], [6]], [[3], [4]], [[4], [7]], [[0], [5]], [[0], [7]],
         [[1], [8]], [[6], [9]], [[2], [6]], [[0], [1]], [[1], [3]], [[3], [6]], [[4], [5]], [[6], [7]], [[0], [3]]],
        [[[7], [9]], [[2], [3]], [[5], [6]], [[5], [8]], [[4], [9]], [[2], [7]], [[1], [6]], [[2], [9]], [[3], [9]],
         [[5], [9]], [[3], [8]], [[0], [6]], [[3], [5]], [[8], [9]], [[2], [8]], [[4], [6]], [[0], [2]], [[2], [5]],
         [[0], [9]], [[5], [7]], [[6], [8]], [[1], [9]], [[0], [7]], [[2], [4]], [[2], [6]], [[3], [7]], [[0], [8]],
         [[4], [8]], [[7], [8]], [[1], [2]], [[0], [1]], [[1], [4]], [[0], [5]], [[4], [5]], [[6], [9]], [[0], [4]],
         [[1], [5]], [[1], [8]], [[1], [7]], [[1], [3]], [[0], [3]], [[3], [4]], [[4], [7]], [[3], [6]], [[6], [7]]],
        [[[2], [7]], [[7], [8]], [[2], [5]], [[4], [9]], [[5], [9]], [[3], [9]], [[2], [9]], [[8], [9]], [[2], [3]],
         [[3], [5]], [[0], [9]], [[1], [7]], [[5], [8]], [[3], [7]], [[6], [8]], [[7], [9]], [[0], [2]], [[0], [6]],
         [[2], [8]], [[5], [6]], [[1], [6]], [[2], [6]], [[5], [7]], [[4], [6]], [[0], [5]], [[1], [9]], [[0], [8]],
         [[2], [4]], [[1], [2]], [[6], [7]], [[0], [7]], [[1], [5]], [[3], [8]], [[4], [7]], [[1], [8]], [[1], [4]],
         [[6], [9]], [[0], [1]], [[0], [3]], [[4], [8]], [[1], [3]], [[0], [4]], [[3], [6]], [[3], [4]], [[4], [5]]]
    ]
    train_pairs = [
        [[[8], [9]], [[2], [3]], [[2], [7]], [[5], [9]], [[7], [9]], [[3], [5]], [[5], [8]], [[4], [6]], [[2], [9]],
         [[3], [9]], [[1], [9]], [[2], [8]], [[0], [5]], [[4], [9]], [[2], [5]], [[0], [8]], [[1], [6]], [[0], [9]],
         [[5], [6]], [[0], [2]], [[0], [1]], [[6], [8]], [[1], [2]], [[3], [7]], [[0], [3]], [[4], [8]], [[3], [8]],
         [[2], [4]], [[0], [6]], [[0], [4]], [[1], [5]], [[1], [4]], [[7], [8]], [[1], [3]], [[4], [7]], [[5], [7]],
         [[1], [7]], [[4], [5]], [[1], [8]], [[0], [7]], [[3], [4]], [[2], [6]], [[6], [9]], [[3], [6]], [[6], [7]]],
        [[[0], [6]], [[4], [9]], [[7], [9]], [[2], [3]], [[5], [8]], [[2], [4]], [[5], [9]], [[2], [5]], [[2], [7]],
         [[3], [9]], [[0], [5]], [[2], [8]], [[0], [9]], [[2], [9]], [[3], [8]], [[3], [7]], [[8], [9]], [[3], [5]],
         [[1], [6]], [[6], [8]], [[7], [8]], [[0], [4]], [[5], [6]], [[1], [2]], [[0], [8]], [[1], [4]], [[0], [2]],
         [[3], [4]], [[1], [9]], [[4], [5]], [[4], [6]], [[0], [1]], [[1], [3]], [[4], [8]], [[0], [3]], [[0], [7]],
         [[5], [7]], [[1], [5]], [[1], [8]], [[4], [7]], [[2], [6]], [[1], [7]], [[6], [9]], [[3], [6]], [[6], [7]]],
        [[[5], [8]], [[2], [8]], [[7], [9]], [[5], [9]], [[1], [6]], [[3], [9]], [[0], [2]], [[3], [5]], [[2], [3]],
         [[0], [7]], [[2], [7]], [[4], [9]], [[8], [9]], [[2], [9]], [[2], [5]], [[1], [8]], [[3], [7]], [[2], [4]],
         [[0], [4]], [[3], [8]], [[0], [8]], [[4], [7]], [[1], [2]], [[4], [8]], [[6], [8]], [[0], [9]], [[1], [4]],
         [[3], [4]], [[7], [8]], [[1], [9]], [[5], [6]], [[0], [5]], [[5], [7]], [[2], [6]], [[4], [6]], [[1], [5]],
         [[0], [1]], [[1], [3]], [[1], [7]], [[4], [5]], [[6], [9]], [[0], [6]], [[3], [6]], [[0], [3]], [[6], [7]]],
        [[[1], [6]], [[7], [9]], [[2], [5]], [[5], [9]], [[3], [9]], [[8], [9]], [[5], [8]], [[2], [3]], [[2], [7]],
         [[4], [9]], [[3], [5]], [[0], [6]], [[2], [8]], [[3], [8]], [[0], [2]], [[1], [9]], [[2], [9]], [[4], [8]],
         [[1], [2]], [[0], [9]], [[0], [5]], [[2], [6]], [[0], [8]], [[1], [4]], [[6], [8]], [[3], [7]], [[2], [4]],
         [[4], [5]], [[0], [4]], [[5], [7]], [[5], [6]], [[7], [8]], [[1], [5]], [[1], [8]], [[1], [3]], [[1], [7]],
         [[4], [6]], [[0], [3]], [[0], [7]], [[3], [4]], [[6], [9]], [[0], [1]], [[4], [7]], [[3], [6]], [[6], [7]]],
        [[[2], [5]], [[2], [3]], [[5], [8]], [[4], [9]], [[7], [9]], [[3], [7]], [[8], [9]], [[2], [9]], [[3], [9]],
         [[0], [5]], [[2], [7]], [[5], [9]], [[6], [8]], [[0], [2]], [[2], [8]], [[2], [4]], [[3], [5]], [[1], [2]],
         [[1], [4]], [[3], [8]], [[1], [6]], [[0], [8]], [[5], [6]], [[4], [8]], [[0], [4]], [[0], [9]], [[4], [5]],
         [[5], [7]], [[1], [9]], [[2], [6]], [[0], [6]], [[4], [6]], [[1], [5]], [[0], [1]], [[4], [7]], [[1], [8]],
         [[7], [8]], [[0], [3]], [[1], [3]], [[1], [7]], [[0], [7]], [[3], [4]], [[6], [7]], [[3], [6]], [[6], [9]]],
        [[[2], [3]], [[7], [9]], [[4], [9]], [[2], [9]], [[5], [8]], [[3], [9]], [[3], [5]], [[2], [8]], [[3], [7]],
         [[5], [9]], [[6], [8]], [[0], [5]], [[2], [6]], [[1], [2]], [[4], [8]], [[8], [9]], [[7], [8]], [[2], [7]],
         [[1], [4]], [[0], [8]], [[2], [4]], [[0], [6]], [[3], [8]], [[1], [6]], [[0], [9]], [[2], [5]], [[5], [7]],
         [[0], [2]], [[1], [8]], [[5], [6]], [[4], [6]], [[1], [5]], [[1], [9]], [[0], [4]], [[4], [5]], [[1], [7]],
         [[0], [1]], [[0], [7]], [[1], [3]], [[4], [7]], [[3], [4]], [[0], [3]], [[6], [9]], [[3], [6]], [[6], [7]]],
        [[[3], [9]], [[7], [9]], [[2], [3]], [[5], [8]], [[2], [5]], [[8], [9]], [[2], [7]], [[4], [8]], [[3], [5]],
         [[0], [6]], [[2], [9]], [[4], [9]], [[2], [6]], [[4], [5]], [[2], [8]], [[5], [9]], [[3], [8]], [[5], [6]],
         [[4], [7]], [[0], [2]], [[1], [2]], [[0], [8]], [[6], [8]], [[1], [4]], [[0], [9]], [[1], [6]], [[2], [4]],
         [[1], [5]], [[3], [7]], [[0], [4]], [[1], [9]], [[3], [4]], [[0], [5]], [[7], [8]], [[4], [6]], [[1], [7]],
         [[1], [8]], [[5], [7]], [[1], [3]], [[0], [1]], [[0], [7]], [[0], [3]], [[3], [6]], [[6], [9]], [[6], [7]]],
        [[[7], [9]], [[2], [9]], [[0], [5]], [[5], [8]], [[0], [8]], [[8], [9]], [[3], [9]], [[6], [8]], [[4], [9]],
         [[2], [8]], [[5], [9]], [[4], [8]], [[2], [7]], [[0], [2]], [[2], [5]], [[2], [3]], [[1], [7]], [[3], [5]],
         [[1], [2]], [[2], [4]], [[1], [4]], [[1], [5]], [[1], [6]], [[3], [8]], [[3], [7]], [[1], [9]], [[0], [6]],
         [[5], [6]], [[0], [4]], [[0], [9]], [[5], [7]], [[4], [5]], [[0], [1]], [[4], [6]], [[0], [7]], [[6], [9]],
         [[1], [8]], [[1], [3]], [[3], [4]], [[4], [7]], [[2], [6]], [[7], [8]], [[0], [3]], [[3], [6]], [[6], [7]]],
        [[[5], [9]], [[1], [6]], [[7], [9]], [[5], [8]], [[2], [3]], [[8], [9]], [[2], [8]], [[2], [9]], [[2], [5]],
         [[3], [9]], [[1], [8]], [[1], [2]], [[4], [9]], [[2], [7]], [[0], [7]], [[3], [8]], [[1], [4]], [[2], [4]],
         [[3], [5]], [[3], [7]], [[6], [8]], [[4], [6]], [[0], [2]], [[4], [8]], [[0], [8]], [[0], [6]], [[5], [6]],
         [[0], [3]], [[0], [4]], [[2], [6]], [[1], [9]], [[1], [3]], [[5], [7]], [[4], [5]], [[1], [5]], [[0], [9]],
         [[0], [5]], [[0], [1]], [[6], [9]], [[7], [8]], [[1], [7]], [[4], [7]], [[3], [4]], [[3], [6]], [[6], [7]]],
        [[[2], [3]], [[6], [8]], [[5], [8]], [[4], [9]], [[1], [2]], [[2], [8]], [[8], [9]], [[7], [9]], [[3], [9]],
         [[4], [8]], [[0], [2]], [[1], [6]], [[5], [9]], [[2], [5]], [[3], [5]], [[2], [7]], [[1], [4]], [[0], [8]],
         [[2], [9]], [[0], [4]], [[1], [7]], [[1], [9]], [[3], [8]], [[0], [9]], [[2], [4]], [[0], [5]], [[1], [5]],
         [[3], [7]], [[5], [6]], [[7], [8]], [[4], [6]], [[4], [7]], [[3], [4]], [[1], [3]], [[4], [5]], [[0], [1]],
         [[1], [8]], [[0], [6]], [[0], [7]], [[5], [7]], [[2], [6]], [[6], [9]], [[0], [3]], [[3], [6]], [[6], [7]]],
        [[[7], [9]], [[5], [8]], [[2], [3]], [[4], [9]], [[5], [6]], [[3], [9]], [[2], [8]], [[1], [6]], [[3], [8]],
         [[2], [9]], [[2], [7]], [[5], [9]], [[2], [5]], [[2], [4]], [[8], [9]], [[6], [8]], [[1], [9]], [[1], [2]],
         [[3], [5]], [[0], [2]], [[1], [4]], [[0], [6]], [[3], [7]], [[0], [8]], [[0], [4]], [[4], [8]], [[1], [5]],
         [[2], [6]], [[4], [6]], [[0], [5]], [[4], [5]], [[7], [8]], [[5], [7]], [[0], [9]], [[1], [8]], [[1], [3]],
         [[4], [7]], [[0], [1]], [[0], [7]], [[0], [3]], [[6], [9]], [[3], [4]], [[1], [7]], [[3], [6]], [[6], [7]]],
        [[[2], [3]], [[2], [5]], [[7], [8]], [[2], [7]], [[8], [9]], [[5], [8]], [[3], [9]], [[7], [9]], [[4], [9]],
         [[5], [9]], [[2], [8]], [[1], [6]], [[3], [5]], [[2], [9]], [[6], [8]], [[0], [8]], [[1], [2]], [[0], [9]],
         [[3], [7]], [[1], [4]], [[3], [8]], [[1], [7]], [[1], [9]], [[0], [2]], [[5], [6]], [[0], [1]], [[2], [4]],
         [[0], [5]], [[2], [6]], [[0], [6]], [[4], [6]], [[1], [5]], [[0], [4]], [[4], [8]], [[1], [8]], [[1], [3]],
         [[5], [7]], [[4], [7]], [[4], [5]], [[0], [3]], [[3], [4]], [[0], [7]], [[6], [9]], [[3], [6]], [[6], [7]]]
    ]

    test = {}
    train = {}

    for p in pairs:
        test[p] = 0
        train[p] = 0

    for i in range(len(test_pairs)):
        for (j, p) in enumerate(test_pairs[i]):
            pair = str(p[0][0]) + '-' + str(p[1][0])
            test[pair] += j + 1

    for i in range(len(train_pairs)):
        for (j, p) in enumerate(train_pairs[i]):
            pair = str(p[0][0]) + '-' + str(p[1][0])
            train[pair] += j + 1

    differences = []

    for p in test:
        print(f'Pair: {p}')
        print(f'Mean for test: {test[p] / len(test_pairs)}')
        print(f'Mean for train: {train[p] / len(train_pairs)}\n')
        differences.append(abs(test[p] / len(test_pairs) - train[p] / len(train_pairs)))

    test = {}
    train = {}

    for p in pairs:
        test[p] = []
        train[p] = []

    for i in range(len(test_pairs)):
        for (j, p) in enumerate(test_pairs[i]):
            pair = str(p[0][0]) + '-' + str(p[1][0])
            test[pair].append(j)

    for i in range(len(train_pairs)):
        for (j, p) in enumerate(train_pairs[i]):
            pair = str(p[0][0]) + '-' + str(p[1][0])
            train[pair].append(j)

    for p in test:
        print(f'Pair: {p}')
        print(f'Values for test: {test[p]}')
        print(f'Values for train: {train[p]}\n')

    print(differences)
    print(max(differences))

    total = 0

    for d in differences:
        total += d

    print(total/len(differences))


if __name__ == '__main__':
    check_leaves()

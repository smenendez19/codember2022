# Tests solutions

from solution import solution

tests = [
    (['red', 'blue', 'red', 'blue', 'green'], (4, "blue")), # 4, blue
    (['green', 'red', 'blue', 'gray'], (2, "gray")), # 2, gray
    (['blue', 'blue', 'blue', 'blue'], (1, "blue")), # 1, blue
    (['red', 'green', 'red', 'green', 'red', 'green'], (6, "green")), # 6, green
    (['blue', 'red', 'blue', 'red', 'gray'], (4, "red")), # 4, red
    (['red', 'red', 'blue', 'red', 'red', 'red', 'green'], (3, "red")), # 3, red
    (['red', 'blue', 'red', 'green', 'red', 'green', 'red', 'green'], (6, "green")) # 6, green
]

if __name__ == "__main__":
    for test in tests:
        zebra = test[0]
        max_count, max_last_color = solution(zebra)
        assert max_count == test[1][0]
        assert max_last_color == test[1][1]
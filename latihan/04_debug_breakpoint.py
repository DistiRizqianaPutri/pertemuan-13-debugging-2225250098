
def rata_rata(data):
    total = sum(data)

    if len(data) == 0:
        return 0

    return total / len(data)


print(rata_rata([80, 90, 70]))

def merge(colletion, start=0, end=None):
    if end is None:
        end = len(colletion)
    if (end - start) > 1:
        middle = (start + end) // 2
        merge(colletion, start, middle)
        merge(colletion, middle, end)
        sort(colletion, start, middle, end)


def sort(colletion, start, middle, end):
    right = colletion[start:middle]
    left = colletion[middle:end]
    top_l = top_r = 0
    for count in range(start, end):
        if top_l >= len(left):
            colletion[count] = right[top_r]
            top_r += 1
        elif top_r >= len(right):
            colletion[count] = left[top_l]
            top_l += 1
        elif left[top_l] <= right[top_r]:
            colletion[count] = left[top_l]
            top_l += 1
        else:
            colletion[count] = right[top_r]
            top_r += 1


if __name__ == '__main__':
    lista_desordenada = [2, 1, 54, 34, 21, 65, 76, 22, 35]
    print(merge(lista_desordenada))

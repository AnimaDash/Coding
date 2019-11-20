def range_sum(range):
    sum = 0
    i = 1
    while i <= range:
        sum += i
        i += 1
    return sum

def num_square(num):
    return num * num

def num_square_range_sum(range):
    sum = 0
    i = 1
    while i <= range:
        sum += num_square(i)
        i += 1
    return sum

if __name__ == "__main__":
    input_num = int(input("input number:"))

    i = 1
    val1 = num_square(range_sum(input_num))
    val2 = num_square_range_sum(input_num)

    print(val1 - val2)

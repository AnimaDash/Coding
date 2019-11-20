def generate_palindrome(max_num):
    i = 1
    num = 0
    while i <= max_num:
        num = num * 10 + i
        i += 1
    
    i -= 2
    while i > 0:
        num = num * 10 + i
        i -= 1
    return num

if __name__ == "__main__":
    input_num = int(input("input number:"))
    i = 1
    while i <= input_num:
        print(generate_palindrome(i))
        i += 1

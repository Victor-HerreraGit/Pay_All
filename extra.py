def last2(str):
    if len(str) < 2:
        return 0
    last_2 = str[len(str) - 2:]

    count = 0
    for i in range(len(str) - 2):
        sub = str[i:i + 2]

        if sub == last_2:
            print(f"This matches last two {sub}")
            count += 1
    print(count)


# last2("12")


def array_front9(nums):
    if not nums:
        return False
    for num in nums[:4]:

        if num == 9:
            return True
    return False


arr = [1, 2, 9, 3, 4]


# print(array_front9(arr))


def array_123(nums):
    ope = []
    if len(nums) < 3:
        return False
    for i in range(len(nums)):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2]:
            return True
    return False


array = [1, 1, 2, 3, 1]
print(array_123(array))


def hello_name(name):
    return "Hello "+name+ "!"


print(hello_name('Bob'))

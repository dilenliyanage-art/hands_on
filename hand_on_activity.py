Numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers2, Numbers1)
print("addition of two lists")
print(list(result))

nums = [1, 2, 3, 4, 5, 6]
def sq(n):
    return n*n
squre = list(map (sq, nums))
print("square numbers in list: ")
print(squre)
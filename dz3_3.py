# задание №3
def my_func(a, b, c):
    return sorted([a, b, c])
a = int(input())
b = int(input())
c = int(input())
print(my_func(a, b, c)[1] + my_func(a, b ,c)[2])
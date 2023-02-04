# This program determines the optimal/minimum moves required for a Tower of Henoi of n size

def toh_movecount(n):
    sum = 0
    if n == 1:
        return 1
    else:
        for i in range(n, 1, -1):
            sum += toh_movecount(i - 1)
        return n + sum


# n = int(input("Enter no. of disks: "))
# result = toh_movecount(n)
# print(f"Minimum no. of moves for {n} disks are", result)












# if you want to understand how this function works, comment out the above program and run the program below
# it will make it easier to understand, although the explanation bugs out from 4 disks onwards you should
# be able to understand it by the first three disks


# def toh_movecount(n):
#     global i  # This line is added cuz the PEP said that "local variable 'i' might be assigned before reference", although that will probably not be a problem if you comment out the above program before running this one
#     sum = 0
#     if n == 1:
#         return 1
#     else:
#         for i in range(n, 1, -1):
#             print(f"i switches to {i}")
#             print("sum is currently", sum)
#             sum += toh_movecount(i - 1)
#             print(f"after function sum is  {sum}")
#             print(f"i is {i} right now in the new function")
#         print("sum is", sum, "and will be now be added to ", n,
#               "thus terminating the current recursed function where i is ", i)
#         return n + sum
#
#
# n = int(input("Enter no. of disks: "))
# result = toh_movecount(n)
# print("Final sum is", result)

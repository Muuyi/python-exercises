# def is_multiple(n,m):
#     p = n%m
#     if p==0:
#         print("True")
#     else:
#         print("false")
# is_multiple(8,4)
# ##CHECKING FOR EVEN AND ODD
# def is_even(k):
#     if k & 1:
#         return 'True'
#     else:
#         return 'False'
# is_even(5)
# is_even(6)
#
# ##MIN AND MAX VALUES IN A LIST WITHOUT USING FUNCTIONS MIN AND MAX
# def minmax(data):
#     biggest = data[0]
#     smallest = data[0]
#     for j in range(len(data)):
#         if data[j] >= biggest:
#             biggest = data[j]
#         elif data[j] <= smallest:
#             smallest = data[j]
#
#     print(biggest,smallest)
# minmax([4,3,1,32,3,4,5])
##TAKES A VALUE N AND RETURNS ALL THE SQUEARES
def nsquare(n):
    total = 0;
    for a in range(n):
        mult =  a * a
        total = total + mult
    return total
print(nsquare(5))
 ##SIGNLE COMMAND
def sqrsum(n):
    total = sum(k*k for k in range(n))
    print(total)
sqrsum(10)
##SQUEARE OF POSITIVE ODD NUMBERS
def sqrodd(n):
    total = sum(k*k for k in range(1,n,2))
    print(total)
sqrodd(5)

def is_multiple(n,m):
    p = n%m
    if p==0:
        print("True");
    else:
        print("false");
is_multiple(8,4)
##CHECKING FOR EVEN AND ODD
def is_even(k):
    if k & 1:
        return 'True'
    else:
        return 'False'
is_even(5)
is_even(6)
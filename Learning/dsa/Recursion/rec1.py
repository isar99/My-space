def rec1_printx_ntimes(x,n):
    if n == 0:
        return
    print(x)
    rec1_printx_ntimes(x,n-1)

def rec2_print_1_to_n_rev(n):
    if n == 0:
        return
    print(n)
    rec2_print_1_to_n_rev(n-1)

def rec3_print_1_to_n_4ward(n):
    if n == 0:
        return
    rec3_print_1_to_n_4ward(n - 1)
    print(n)

def rec4_sum_of_n_nums(sum,i,n):
    if i > n:
        print(sum)
        return
    # sum += i
    # i+=1
    rec4_sum_of_n_nums(sum+i,i+1,n)

def rec5_sum_of_n_nums_meth2(n):
    if n==1:
        return 1
    return n + rec5_sum_of_n_nums_meth2(n-1)

def rec6_factorial(n):
    if n==0 or n==1:
        return 1
    return n*rec6_factorial(n-1)

def rec7_rev_an_array(arr_rev, i, arr):
    if i == len(arr):
        return
    rec7_rev_an_array(arr_rev, i+1, arr)
    arr_rev.append(arr[i])

def rec7_rev_an_array_meth2(lp,arr,rp):

    if lp >= rp:
        return
    arr[lp], arr[rp] = arr[rp], arr[lp]
    rec7_rev_an_array_meth2(lp+1,arr,rp-1)

def rec8_is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return rec8_is_palindrome(text[1:-1])

def rec9_is_palindrom_meth2(text, left, right):
    if text[left].lower() != text[right].lower():
        print("Text is not palindrome")
        return False
    if left > right:
        print("Text is palindrom")
        return True
    rec9_is_palindrom_meth2(text, left+1, right-1)

def rec10_fibonacci(n):
    if n==0 or n==1:
        return n
    return rec10_fibonacci(n-1) + rec10_fibonacci(n-2)



if __name__ == "__main__":
    # You need to print x n times
    x = "abc"
    n = 6
    sum = 0
    i = 0
    arr = [5,6,3,9,2,7]
    arr_rev = []

    lp = 0  # Left pointer
    rp = len(arr)-1  # Right pointer

    # rec1_printx_ntimes(x, n)
    # rec2_print_1_to_n_rev(n)
    # rec3_print_1_to_n_4ward(n)
    # rec4_sum_of_n_nums(sum,i,n)
    # print(rec5_sum_of_n_nums_meth2(n))
    # print(rec6_factorial(n))
    # rec7_rev_an_array(arr_rev,i,arr)
    # print(arr_rev)
    # rec7_rev_an_array_meth2(lp, arr, rp)
    # print(rec8_is_palindrome("abcbad"))
    # text = "aNittina"
    # rec9_is_palindrom_meth2(text,0,len(text)-1)
    n=12
    print(rec10_fibonacci(n))
    # print(arr)

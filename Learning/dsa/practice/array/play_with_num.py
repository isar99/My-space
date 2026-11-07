from math import sqrt

def print_digits(num):
    while num>0:
        digit = num%10
        print(digit)
        num = num//10

def count_digits(num):
    count = 0
    while num>0:
        count += 1
            num = num//10
    print(count)

def digit_palindrome(num):
    n = num
    new_n = 0
    while n>0:
        last = n%10
        n = n//10
        new_n = last+(new_n*10)
    if new_n==num:
        print(f"Digit {num} is Palindrome")
        return True
    else:
        print(f"Digit {num} is not a Palindrome")
        return False

def armstrong_num(num):
    """Armstrong number is addition of digits raised to the power number
    of digits is same as number
    153 -> 1^3+5^3+3^3 = 153 is an armstrong number
    1634 -> 1^4+6^4+3^3+4^4 = 1634 is an armstrong number
    :param num:
    :return:
    """
    n = num
    digit_count = len(str(n))
    summ = 0
    while n>0:
        last = n%10
        last_num_powered = last**digit_count
        summ = summ + last_num_powered
        n = n//10
    return summ == num
    # if summ == num:
    #     print(f"{num} is Armstrong number")
    # else:
    #     print(f"{num} is not an Armstrong number")

def count_armstrong_num_upto(num):
    count = 0
    numm = num
    for n in range(1,numm+1):
        is_armstrong = armstrong_num(n)
        if is_armstrong:
            print(f"{n} is armstrong")
            count=count+1

    print(count)

def get_factors_count(num):
    factors_list = []
    numm = num
    for i in range(1,numm+1):
        remainder = numm%i
        if remainder == 0:
            factors_list.append(i)
    print(factors_list)

def get_factors_count_meth2(num):
    factors_list = []
    numm = num
    sqrt_num = int(sqrt(numm))
    for n in range(1,sqrt_num+1):
        if numm%n == 0:
            factors_list.append(n)
            quotient = numm//n
            if quotient != n:
                factors_list.append(quotient)
    print(factors_list)

def store_freq_dict_meth1(num_ls):
    freq_dict = {}
    for i in num_ls:
        if i in freq_dict.keys():
            count = freq_dict[i]
            count_new = count + 1
            freq_dict[i] = count_new
        else:
            freq_dict[i] = 1
    print(freq_dict)

def store_freq_dict_meth2(num_ls):
    nums = num_ls
    hash_map = {}
    n = len(nums)
    for i in range(0,n):
       hash_map[nums[i]] = hash_map.get(nums[i],0)+1
    return hash_map



if __name__ == "__main__":
    num = 30
    num_ls = [3,4,7,2,3,8,11,8,3,2,2]
    #print_digits(n)
    #count_digits(n)
    #digit_palindrome(num)
    #print(armstrong_num(num))
    #count_armstrong_num_upto(num)
    #get_factors_count(num)
    #get_factors_count_meth2(num)
    #store_freq_dict_meth1(num_ls)
    print(store_freq_dict_meth2(num_ls))



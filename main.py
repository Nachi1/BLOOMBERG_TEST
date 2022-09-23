# given a number n, for each integer i in the range of 1 to n inclusive
# print one value per line as follows
# if 'i' is a multiple of both 3 & 5, print 'fizzbuzz'
# if 'i' is a multiple of 3 but not 5, print fizz
# if 'i' is a multiple of 5 but not 3, print buzz
# if 'i' is not a multiple of 3 or 5, print value of i

def fizzBuzz(n):
    mod1 = [i for i in range(1, n)]
    for a in mod1:
        if a % 5 == 0 and a % 3 == 0:
            print('fizzbuzz')
        elif a % 5 == 0 and a % 3 != 0:
            print('fizz')
        elif a % 5 != 0 and a % 3 == 0:
            print('buzz')
        elif a % 5 != 0 and a % 3 != 0:
            print(a)


fizzBuzz(int(input('enter a number 1 - 40 \n').strip()))

for num in range(100,100000):
    def is_perfect(num):
        for i in range(1,num):
            if i*i == num:
                return True
                break
    def is_prime(num):
        for i in range(2,num):
            if num % i == 0:
                return False
                break
        else:
            return True
    if is_perfect(num) == True:
        print "Bar", num
    elif is_prime(num) == True:
        print "Foo", num
    else:
        print "FooBar", num
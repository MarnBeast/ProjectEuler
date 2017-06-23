#!/usr/bin/python



# Returns the number of digits in the base 10 decimal representation
# of the passed in val.
def digits(val):
    str_val = str(val)
    str_len = len(str_val)
    return str_len

# How many n-digit positive integers exist which are also an nth power?
# 10^n will always be n+1 digits long. So 10 is our upper bound.

def main():
    count = 0
    print("How many n-digit positive integers exist which are also an nth power?")
    
    for x in range(1,10):     # 10 and up are guaranteed to long
        n = 1
        old_diff = 0
        keep_going = True
    
        print("Testing x = %d" % x)
    
        # keep incrementing our exponent n and checking if our pow matches our digits
        while keep_going:
            #does our exponent n match our digits d?
            p = pow(x,n)
            d = digits(p)
            if d == n:       
                count += 1  #yes it does!
    
            # When do we stop?
            # When it's clear that we are running away from converging on n = d
            diff = abs(d-n)
    
            if (diff > old_diff
            and old_diff != 0):
                keep_going = False;
    
            print ("{0}^{1}={2} which is {3} digits long. diff:{4} old diff:{5} count:{6}"
            .format(x, n, p, d, diff, old_diff, count))
    
            n += 1
            old_diff = diff
    
    print ("%d integers" % count)

if __name__ == "__main__":
    main()

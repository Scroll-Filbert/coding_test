#print 1 ... 100
#print "Fizz" if divisible by 3
#print "Buzz" if divisible by 5
#print "Bazz" if divisible by 7
#print "FizzBuzz" if divisible by 3 and 5

def main():
    i = 1
    text = ""

    while i<100 :
        #if (i % 3 == 0) and (i % 5 == 0):
        #    print("FizzBuzz")
        #elif (i % 3 == 0):
        #   print("Fizz")
        #elif (i % 5 == 0):
        #    print("Buzz")
        #else:
        #    print(i)

        match True:
            case _ if i % 3 == 0 and i % 5 == 0:
                text += "FizzBuzz"
            case _ if i % 3 == 0:
                text += "Fizz"
            case _ if i % 5 == 0:
                text += "Buzz"
            case _ if i% 7 == 0:
                text += "Bazz"
            case _ :
                text = str(i)
        print(text)
        text = ""        
        i += 1

if __name__ == "__main__":
    main()
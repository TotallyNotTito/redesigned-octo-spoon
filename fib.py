
#code for input
print("This calculator givens the Nth fibonaci term in a sequence. Inputting the iteration outputs the number in that sequence")
print('input a fibonacci number')
n = float(input())

# code for first 2 outputs of fibonacci sequence
if (n == 1 or n == 2) :
    print(1, 'is fibonacci output')
# main code for fibonacci output
else :
    prev = 1 # output when fib is 2
    prevPrev = 1 # output for when fib is 1
    counter = 0 # initialize while loop
    fib = 1 # first fib output in fib sequence
    while (counter < n - 2) : # counter is at - 2 since first 2 outputs are in first conditional
        prevPrev = prev # want to move the last position up along the output ladder
        prev = fib # want the previous value to equal the fib output 
        fib = prev + prevPrev # want to add the last 2 outputs to equal current output
        counter = counter + 1 # want to terminate loop
    print(fib, '\nis fibonacci output')

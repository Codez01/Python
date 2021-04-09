import matplotlib.pyplot as plt
import numpy as np


#




# *********** Function to find the root for is : x^3 - 5*x - 9 **********

# Function ; x^3 - 5*x - 9
# Replacing given x to the specified function
def f(x):
    answer = lambda x: x ** 3 - 8 * x - 11
    answer = answer(x)

    return answer


# Derivative of the above function
# which is 3*x^2 - 5
# Replacing given x to the specified function
def g(x):
    answer = lambda x: 3 * x ** 2 - 8
    answer = answer(x)

    return answer

#*************Newton Raphson Method **************

def newtonRaphson(x, epsilon, delta, max_iter):# finding root using newton raphson method 
    
    if abs(f(x)) < delta : return x
    
    xn_prev = x# for storing previous value of x
    xn = 0
    i = 0 # for the iterations value
    found = False

    while (1):

        if g(x) == 0.0:
            print('Divide by zero error!')
            print("No Solution Was Found")
            break

        xn = xn_prev - (f(xn_prev) / g(xn_prev))

        if (max_iter < i):#checking first statement
            print("exceeded max iterations")
            break

        if (abs(xn - xn_prev) < epsilon):#checking second statement
            found = True
            break

        if (abs(f(xn)) < delta):#checking third statement
            found = True
            break

        xn_prev = xn# updating xn_prev to have the prev value of xn in the begginning of each loop

        i += 1 #incrementing the number of the current iteration number by 1
        
    if (found):# it means that the root of the specified equation is found 
        print("The answer Using Newton's Method Is : {} After : {} iterations ".format(xn, i))
    else :
        print("No Solution Was Found")

#************** Secant Method ***************

def secant(a, b, epsilon, delta, max_iter):# finding root using secant method
    j = 0# for storing each iteration number
    xn = 0
    found = False

    if abs(f(a)) < delta: return a
    if abs(f(b)) < delta: return b

    while 1:
        try:# making sure that there are no divisions error

            xn = b - (f(b) * ((b - a) / (f(b) - f(a))))

        except:
            print('Divide by zero error!')


            break

        if max_iter < j:# checking the first statement
            print("exceeded max iterations")
            break

        if abs(xn - b) < epsilon:# checking the second statement
            found = True
            break

        if abs(f(xn)) < delta:# checking the third statement 
            found = True
            break

        a = b
        b = xn
        j += 1 #incrementing the number of the current iteration number by 1

    if (found):# if the root was found 
        print("The answer Using Secant's Method Is : {} After : {} iterations ".format(xn, j))
    else :
        print("No Solution Was Found")


epsilon = 0.0000001
delta = epsilon

newton = newtonRaphson(0, epsilon, delta, 10000)
secant = secant(2,3,epsilon,delta,10000)

try:
    # 100 linearly spaced numbers
    x = np.linspace(-5, 5, 100)

    # the function, which is y = x ** 3 - 8 * x - 11
    y = x ** 3 - 8 * x - 11

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x, y, 'g')

    # show the plot
    plt.grid()
    plt.show()

except:

    print("Cannot Be Shown On A Graph")

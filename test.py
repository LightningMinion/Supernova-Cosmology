import scipy
import scipy.integrate
def integrand(x):
    return x

answer, error = scipy.integrate.quad(integrand, 0, 1)
print(answer)

myarray = [1,2,3,4,5]
print(len(myarray))
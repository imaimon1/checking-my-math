import sympy
import random 
import matplotlib.pyplot as plt


def gcd(a,b,k=0):

	if a==b:
		return a*(2**k)
	
	if a==0 or b==0:
		return (a+b)*(2**k)
	
	if a%2==0 and b%2==0:
		k+=1
		return gcd(a/2,b/2,k)
	
	elif a%2==0:
		return gcd(a/2,b,k)
	
	elif b%2==0:
		return gcd(a,b/2,k)
		
	elif a < b:
		return gcd((b-a)/2,a,k)
			
	elif b < a:	
		return gcd((a-b)/2,b,k)

def gcd_average_lower(a):
	i=0
	out=1
	primes = list(sympy.sieve.primerange(1,a))
	while primes[i] <= int(a/3)**.5:
		out *= (1+1.0/float(primes[i])-1.0/float(primes[i]**2))
		i += 1
	
	n=0
	while n < i:
		out *= (1+1.0/float(primes[i+n])-1.0/float(primes[i+n]**2))
		n += 1
		
	while primes[n+i]< int(a/3):
		out *= (1+1.0/float(a/3)-1.0/float((a/3)**2))
		n += 1
	return out	
		
def gcd_average_upper(a):
	i=0
	out=1
	primes = list(sympy.sieve.primerange(1,a))
	
	while primes[i] <= int(a/3)**.5:
		out *= (1+1.0/float(primes[i]))
		i += 1
	
	n=0
	while n < i:
		out *= (1+1.0/float(primes[i+n]))
		n += 1
		
	while primes[n+i]< int(a/3):
		out *= (1+1.0/float(a/3))
		n += 1
	return out	
	
def monte_carlo_gcd(a,number):
	i=0
	total=0
	while i < number:
		first = random.randint(1,a)
		second = random.randint(1,a)
		gcd_mc = gcd(first,second)
		total += gcd_mc
		i += 1
	return float(total)/float(number)
i=0
input= []
while i < 40: 
	input.append(random.randint(500*i,500*(i+1)))
	i+=1

gcd_real = []
gcd_upper = [] 
gcd_lower = []
for i in input:
	gcd_real.append(monte_carlo_gcd(i,100000))
	gcd_lower.append(gcd_average_lower(i))
	gcd_upper.append(gcd_average_upper(i))
	
plt.plot(input,gcd_real,'b--',input,gcd_lower,'g^',input,gcd_upper, 'r^')
plt.show()















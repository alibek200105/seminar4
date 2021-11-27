m=int(input("Введите значение а="))
l=int(input("Введите значение n="))
def myfunc(a,n):
	i=1
	p=1
	while i<=n:
		p=p*((a+i)**2)
		i+=1
	print("Значение р=",p)
myfunc(m,l)

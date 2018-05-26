#zgadywanie na odwrot	 DZIALA xD 
import random
random.seed()


if __name__=="__main__":
	print "No siema, sprobuje zgadnac te liczbe, ok?"
	print "ale plox, niech ta liczba bedzie w przedziale 0,100"
	a = int(0)
	b = int(100)
	zgadniete = False
	licznik = int(0)
	while zgadniete is False:
		liczba = random.randint(a,b)
		print "Czy ta liczba to... %s" %liczba
		warunek = input ( "1.Tak 2.Nie " )
		if warunek is int(2):
			gdzie = input ( "1.wieksze od mojej? 2. mniejsze od mojej? ")
			if gdzie == int(1):
				a = liczba +1
				print 'a= %s' %a
				print "b= %s " %b
				licznik +=1
			else:
				b = liczba -1
				print 'a= %s' %a
				print "b= %s " %b
				licznik +=1
		else:
			licznik +=1
			print "yay, zgadlem." 
			print "Potrzebowalem %s prob. " %licznik 
			zgadniete = True
			

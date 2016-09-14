#Cisco Static Route Generator
#Author Kishan Bhugul
#Version 1.0

file = open('ipRoutes.txt', 'r')

for line in file:
        count=0
        for word in line.split():
            if(count==0):
               x = "ip route "+word+" 255.255.255.255 "
               count=count+1
            else:
                x=x+word

                print x

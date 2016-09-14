# Cisco-Route-Generator
Python script to generate static routes

It is a Python script to quickly generate static routes for Cisco routers.

The IP Addresses (Source IP + Gateway) can be added in a spreadsheet and saved as a text file.

A sample of the text file format is given (ipRoutes.txt).

The input Format:

172.17.168.249 192.168.103.1

The output Format:

ip route 172.17.168.249 255.255.255.255 192.168.103.1

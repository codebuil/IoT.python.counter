#!/usr/bin/python
import os
def head():
	print("<html><head><title>");	
	print("counter");
	print("</title><head><body bgcolor='#008800'><br>");
def body():
	i=0
	ss=""
	s=""
	try:
		f= open("0", "r+")
	except:
		f= open("0", "w+")
		f.write('0')
		f.close
		f= open("0", "r+")
	s=f.read()
	f.close
	i=1+int(s)
	print(i)
	f= open("0", "w+")
	f.write(str(i))
	f.close

def enddoc():
	print("<br></body></html>");	

print("Content-type:plain-text\r\n\r\n");
head()
body()
enddoc()
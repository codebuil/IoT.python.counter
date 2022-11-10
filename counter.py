#!/usr/bin/python
import os
def head():
	print("Content-type:plain-text\r\n\r\n");
	print("<html><head><title>");	
	print("counter");
	print("</title><head><body bgcolor='#008800'>");
def body():
	i=0
	ss=""
	s=""
	sss=""
	ss=os.getenv('QUERY_STRING')	
	sss="zzz"+ss
	ss=""
	try:
		f= open(sss, "r+")
	except:
		f= open(sss, "w+")
		f.write('0')
		f.close
		f= open(sss, "r+")
	s=f.read()
	f.close
	i=1+int(s)
	print(i)
	f= open(sss, "w+")
	f.write(str(i))
	f.close

def enddoc():
	print("</body></html>");	

head()
body()
enddoc()
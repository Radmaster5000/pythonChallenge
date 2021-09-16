
# OpenerDirector.open(url, data=None[, timeout])
# Open the given url (which can be a request object or a string), 
# optionally passing the given data. Arguments, return values and exceptions 
# raised are the same as those of urlopen() (which simply calls the open() 
# 	method on the currently installed global OpenerDirector). The optional 
# timeout parameter specifies a timeout in seconds for blocking operations like 
# the connection attempt (if not specified, the global default timeout setting 
# 	will be used). The timeout feature actually works only for HTTP, HTTPS and 
# FTP connections).

from urllib.request import urlopen

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

page = urlopen(url)

##### https://realpython.com/python-web-scraping-practical-introduction/ #####

#urllib.request.urlopen(http://www.philipradford.com)


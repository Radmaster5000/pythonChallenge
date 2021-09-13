string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

url = "http://www.pythonchallenge.com/pc/def/map.html"

#for i in string:
#	if i.isalpha():
#		print(chr(ord(i)+2), end='')
#	else:
#		print(i, end='')

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = url.maketrans(intab, outtab)

print(url.translate(trantab))
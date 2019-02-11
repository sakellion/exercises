import string
import re

x=raw_input("Tell me the file")
with open("%s.txt" %x,'r') as f :
    file = f.read().replace('/n','')
    strings = file.replace(" ","")

finalstring = re.sub(r'[^/w/s]'),'',strings
maxstring = max(finalstring, key = strings.count)
minstring = min(finalstring, kay = strings.count)
print "The most showed letter is",maxstring
print "The letter showed the least is", minstring

for a in range(("%s"%minstring,"%s" %maxstring.upper()),("%s"%minstring.upper())):
        file = file.replace(*a)
print file

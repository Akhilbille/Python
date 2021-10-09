import re,urllib
import urllib.request
u=urllib.request.urlopen("http://alits.ac.in/contact-us.html")
text=u.read()

numbers=re.findall("\w[a-zA-Z0-9_.]*@(gmail|yahoo|alts)[.](com|org|in|ac.in)",str(text),re.I)
for n in numbers:
   print(n)

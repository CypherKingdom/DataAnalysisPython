import re
#the library will not get installed
#here we dont have a patter, we are just looking if where the string is inside s
s = "AbbbbAbbbbAbbb:A computer science portal for aaaaa"
#what does r mean, it means it is raw, raw means that \ will not be interpreted
#it will not escape it will take it as is
#if we put re it will compile it and take the \
match = re.search(r'portal',s)
print('Start Index:', match.start())
print('End Index',match.end())

#re.findall() finds and returns all matching occurence in a list
#re.compile() regular expression are transformed into a pattern objects
#re.cplit() we can split the expression by a pttern or a character
#re.sub() we replace all occurence of a pattern to a string
#re.escape() it escapes a certain character
#re.search() it find the first occurence of a character or a pattern

#it will return non overlapping strings, meaning that they dont have an intersection
string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""
regex = '\d+'
#\ escape
#\d digit
#\d+ sequence of digits
#d\* ma32oul tkoun 0 digits
match = re.findall(regex, string)
print(match)

p = re.compile('[a-e]')
#it is all the characters between a and e
print(p.findall("Aye, said Mr. Gibeeeenson Startk"))
#it starts from left to right, and it returns the list accordingly

import re
p = re.compile('\d')
#find all one singular digit
print(p.findall("I went to him at 11 A.M. on 4th july 1886"))
p = re.compile('\d+')
#find all sequence of digits
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))


############
#by default it takes raw
p = re.compile('\w')
#single character (things that can be used in a variable)

print(p.findall("He said * in some_lang.")) 
p = re.compile('\w+')
#successive character
print(p.findall('I went to him at 11 A.M., he \
                said *** in some_language'))
p = re.compile('\W')
#everything that cannot be used in a variable name
print(p.findall("he said *** in some_language."))

p = re.compile('ab*')
print(p.findall("ababbaabbb"))
#it should be obvious


#split function details 
#maxsplit is the number of times we want the code to split the string
#flags are used to ignore some stuff (optional it is an extra condition, lower case upper case, not case sensitive (insensitive) re.IGNORECASE mesh fer2a ma3o eza upper case or lower case)
#re.split(pattern, string, maxsplit=0, flags=0)
#maxsplit is optional if it is not specified then it would work in a way such that it always split the string according to the occurance\=
#WHICH IS LOGIC
#VERY UZAFUL

print(re.split('\W+','Words, words , Words'))
#it will split according to W+ which means successive special characters, so it will split according to (, ) and then ( , )
print(re.split('\W+',"Words's words Words"))
#same idea but now (') is also a special character
print(re.split('\W+','On 12th Jan 2016, at 11:02 AM'))
#\W+ | \d+ (this is how we do or) (honeh it will split 7asab el digit too) when it was W+ it took it because a digit is not considered as a special character
print(re.split('\d+','On 12th Jan 2016, at 11:02 AM'))
#it will cut relative to the sequence of digits

#try to see what happens when we remove the +, the idea is that we split many times and we get empty string

print(re.split('\d+','On 12th Jan 2016, at 11:02 AM',1))
#it will split only one time
print(re.split('[a-f]+','Aey, Bou oh boy, come here',flags=re.IGNORECASE))
#equivalent to (a+b+c+d+e+f)+ it will also ignore the the case so it is taking into consideration also the characters that are uppercase
print(re.split('[a-f]+','Aey, Boy oh boy, come here'))

#re.sub(pattern, repl, string, count=0, flags=0)
#we search for a pattern in a string and it is replaces by repl


#it will replace ub with ~* inside the string (with relation to the condition)
print(re.sub('ub','~*', 'Subject has Uber booked already',flags=re.IGNORECASE))
#IGNORECASE will take into consideration 2^n combinations ub Ub uB UB (4 possiblities because n = 2)
print(re.sub('ub','~*', 'Subject has Uber booked already'))
#only ub
print(re.sub('ub','~*', 'Subject has Uber booked already',count=1,flags=re.IGNORECASE))
#it will only do it once
print(re.sub('ub','~*', 'Subject has Uber booked already uBik',count=3,flags=re.IGNORECASE))
#it will do it 3 times
print(re.sub(r'\sAND\s','&',"Baked Beans And Spam",flags=re.IGNORECASE))
#r means that it is raw, meaning that it will take symbols like \s hiyeh space, so we are searching for ( AND )
print(re.sub(r'\'AND\'','&',"Baked Beans 'And' Spam",flags=re.IGNORECASE))


#re.subn(pattern, repl, string, count=0, flags=0)
#it just like sub but it returns it in the first part of the tuple, and the count in the second part of the tuple
print(re.subn('ub','~*', 'Subject has Uber booked already',flags=re.IGNORECASE))
t = re.sub('ub','~*', 'Subject has Uber booked already',flags=re.IGNORECASE)
print(t)
print(len(t))
print(t[0])

#non alphanumerical not digit and not alphabet
#re.escape(string) 
print(re.sub('\W+',r'\ ', 'This is Awesome even 1 AM'))
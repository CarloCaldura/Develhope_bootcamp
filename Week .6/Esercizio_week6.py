'''
s.endswith(suffix)     # Check if string ends with suffix
s.find(t)              # First occurrence of t in s
s.index(t)             # First occurrence of t in s
s.isalpha()            # Check if characters are alphabetic
s.isdigit()            # Check if characters are numeric
s.islower()            # Check if characters are lower-case
s.isupper()            # Check if characters are upper-case
s.join(slist)          # Join a list of strings using s as delimiter
s.lower()              # Convert to lower case
s.replace(old,new)     # Replace text
s.rfind(t)             # Search for t from end of string
s.rindex(t)            # Search for t from end of string
s.split([delim])       # Split string into list of substrings
s.startswith(prefix)   # Check if string starts with prefix
s.strip()              # Strip leading/trailing space
s.upper()              # Convert to upper case
s1 = "REDDITO_LAVORO_DIPENDENTE_2021"
s1.split("_")
['REDDITO', 'LAVORO', 'DIPENDENTE', '2021']
s1.lower().split("_")
['reddito', 'lavoro', 'dipendente', '2021']
s1.split("_")[-1]
'2021'
TODO Trovare l'anno all'interno della stringa s2 in modo indipendente dalla posizione dell'anno all'interno della stringa
s2 = "REDDITO_LAVORO_2021_DIPENDENTE"
s2.split("_")[-1]
'DIPENDENTE'
'''
s2 = "REDDITO_LAVORO_2021_DIPENDENTE"
print(s2.join([anno for anno in s2.split("_") if anno.isdigit()]))


for i in s2.split("_"):
    if i.isdigit() :
        print(i)







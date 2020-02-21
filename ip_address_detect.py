import re   # importing python regexp module. how do I know how it works? where is its doc?

# opening a file (read mode) and getting its handle
with open('testfile.txt', 'r') as f:
    lines = f.readlines() # reading all lines in the file. I get back a list of strings
# why don't I close the file handle here? what does the "with" keyword do?

# compiling a regular expression for performance reasons
# what does this thing do?
pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

ip_addresses = [] # what does this mean?

for line in lines:
    matches = pattern.findall(line) # and this?
    ip_addresses.extend(matches) # and this?

print(ip_addresses)
# result:
# ['1.1.1.1', '123.234.12.0', '2.123.2.3', '123.231.78.4', '800.900.700.1']

# TODO:
# 1. Is '800.900.700.1' a valid ip address? what can I do to improve my regexp?
# 2. What should I do with the result? write it to a file? how do i do that?
# 3. I'm reading all the file in memory and then i'm iterating line by line. Can I do better?

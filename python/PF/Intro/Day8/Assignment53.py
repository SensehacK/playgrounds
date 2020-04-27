#PF-Assgn-53
#This verification is based on string match.
import re
poem='''
If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.
'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.

#Write your logic here for question 1

print()
print(re.sub(r'\n',r' ',poem))

print()
print(re.sub(r'c(h|o)',r'C\1',poem))


print(re.sub(r"(a|h)i...",r" \1i*\*",poem))
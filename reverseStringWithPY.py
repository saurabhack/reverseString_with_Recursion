
def reverse(s):
    if len(s)==0:
        return s
    return reverse(s[1:] )+s[0]
s="saurabh"
i=-1
j=len(s)-1
print(reverse(s))

def substr(s,x,y):
    list1=s[x:y+1:]
    print(f"这是切割后：{list1}")
substr("abcdefghjkl",1,4)
def strreverse(s):
    s=s[::-1]
    print(f"这是翻转后的：{s}")
strreverse("abcdefghijk")
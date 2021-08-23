f = open("upkey.txt")
content_f = f.readlines()
access = content_f[0].strip()
secret = content_f[1].strip()

print(access)
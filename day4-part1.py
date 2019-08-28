from hashlib import md5
test = md5(b"bgvyzdsv").hexdigest()
i = 0

while test[:6] != "000000":
    print(test)
    test = md5(b"bgvyzdsv" + str(i).encode("utf8")).hexdigest()
    i += 1

print(test)
print(i-1)
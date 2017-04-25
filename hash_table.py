import hashlib


def check_password(p):
    md5_digest = 'a4757d7419ff3b48e92e90596f0e7548'  # god
    md5 = hashlib.md5(p)
    return md5.hexdigest() == md5_digest

p = raw_input("Enter password: ")
print check_password(p)

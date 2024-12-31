import crypt

password = "yourpassword"
salt = "$6$6QFbdp2H$"  # Salt from the hash

# Hash the password using the same salt
hashed_password = crypt.crypt(password, salt)

print(hashed_password)
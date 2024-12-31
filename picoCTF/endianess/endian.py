def to_little_endian(string):
    # Convert the string to bytes
    byte_data = string.encode("utf-8")  # UTF-8 or ASCII encoding
    # Reverse the byte order for little-endian
    little_endian = byte_data[::-1]
    # Convert each byte to a 2-character hex string and join them
    return "".join(f"{byte:02X}" for byte in little_endian)

def to_big_endian(string):
    # Convert the string to bytes
    byte_data = string.encode("utf-8")  # UTF-8 or ASCII encoding
    # Convert each byte to a 2-character hex string and join them
    return "".join(f"{byte:02X}" for byte in byte_data)

# Test example
word = "zhfvt"
little_endian_hex = to_little_endian(word)
big_endian_hex = to_big_endian(word)

print(f"Original string: {word}")
print(f"Little-endian hex: {little_endian_hex}")
print(f"Big-endian hex: {big_endian_hex}")

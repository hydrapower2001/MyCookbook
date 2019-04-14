# Bytes kann nicht verändert werden
empty_bytes = bytes(10)

print(empty_bytes)

bytes_with_content = bytes(b'\x01\x02\xff')

print(bytes_with_content)

# Bytesarray kann verändert werden

bytearray = bytearray(10)

print(bytearray)

bytearray[0] = 254
bytearray.append(255)

print(bytearray)

# Bytesarray in Bytes umwandeln
immutable = bytes(bytearray)
print(immutable)

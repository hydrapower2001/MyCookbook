# Bytes kann nicht verändert werden
empty_bytes = bytes(10)

print(empty_bytes)

bytes_with_content = bytes(b'\x01\x02\xff')

print(bytes_with_content)

# Bytesarray kann verändert werden

empty_bytearray = bytearray(10)

print(empty_bytearray)

empty_bytearray[0] = 254

print (empty_bytearray)

word = b'r\xc3\xa9sum\xc3\xa9'
decode_word = word.decode('utf-8')
print(decode_word)

latin_byte = decode_word.encode("Latin1")
print(latin_byte)

new_word = latin_byte.decode("Latin1")
print(new_word)


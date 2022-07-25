global _start:

section .data
        text db "This is a simple assembly code!!", 10
        len equ $ -text
section .text
_start: 
        mov eax, 4 ; eax is a general purpose register and this performs a sys_wite system call           ; which is a call to system to execute a task
        mov ebx, 1 ; stdout file descriptor
        mov ecx, text
        mov edx, len
        int 0x80

        mov eax, 1 ; sys_exit system call
        mov ebx, 0 ; exit status code is 0 (ended succesfully)
        int 0x80           
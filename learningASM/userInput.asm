section .data
        text1 db "What is your name, bro? "
        text2 db "Hi, nice to meet you, "

section .bss
        name resb 50 ; this label stores the address of the name variable

section .text
        global _start

_start:
        call _printtext1
        call _getname
        call _printtext2
        call _printname

        mov rax, 60
        mov rdi, 0
        syscall

_printtext1:
        mov rax, 1
        mov rdi, 1
        mov rsi, text1
        mov rdx, 24
        syscall
        ret

_printtext2:
        mov rax, 1
        mov rdi, 1
        mov rsi, text2
        mov rdx, 22
        syscall
        ret

_getname:
        mov rax, 0
        mov rdi, 0
        mov rsi, name
        mov rdx, 20
        syscall
        ret

_printname:
        mov rax, 1
        mov rdi, 1
        mov rsi, name
        mov rdx, 20
        syscall
        ret 

    
section .data
        digit db 0,10
section .text
        global _start
_start:
        mov rax, 6
        mov rbx, 3
        div rbx
        call _printDigit
_printDigit:
        add rax, 48
        mov [digit], al
        mov rax, 1
        mov rdi, 1
        mov rsi, digit
        mov rdx, 2
        syscall
        ret
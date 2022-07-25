section .data
        digit db 0,10
section .text
        global _start
_start:
        push 9
        push 6
        push 5
        push 4
        pop rax
        call _printDigit
        pop rax
        call _printDigit
        pop rax
        call _printDigit
        pop rax
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
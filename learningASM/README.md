# ASM
This is a collection of assembly files.
The __NASM__ assmebler converts the assembly code into machine language (here an ELF64 object file).
which is then linked by the __GNU Linker(ld)__ to create an executable from the .o machine code.

The Registers are parts/components of the processor that executes operations on the data, the
variables are loaded into special or general purpose register and then operations are executed 
and then thses values can be stores in permanent registers. The x86_64 has 64 registers like
__rax__, __rsi__, __rdi__, __eax__, __ebx__, __ecx__, and there are system calls . The `int` stands for interrupt that 
the processor transfers control to an interruot handler that is associated with a value, in  cases
like __0x80__ stands for __system calls__. The specific system call is determined byt the __eax__ register.
like `mov eax, 1` stands for __sysexit__ and  `mov ebx, 42` stands for a __status code__ of 42.

It's __TOUGH__!!

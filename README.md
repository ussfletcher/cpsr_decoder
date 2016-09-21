# cpsr_decoder
Basically a python conversion of https://gist.github.com/jroelofs/126d2563f9c32f7e7353

This is made to decode an ARM CPSR register value into a visually useful table

Consists of one function, decode_cpsr that takes in a CPSR integer value and an optional number of leading tabs. This function outputs a string with linebreaks and leading tabs as necessary, that can then be printed out.

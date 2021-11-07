logfile log/test.txt
stepsize 50
h vdd! 
l vss! 
l cin0 
vector A a3 a2 a1 a0 
vector B b3 b2 b1 b0 
vector op s1 s0 
vector C_out cout 
vector out aluout3 aluout2 aluout1 aluout0 
vector in s1 s0 a3 a2 a1 a0 b3 b2 b1 b0 
w in out C_out a b op 
analyzer A B op C_out out in 
setvector in 1101111010
s
setvector in 0111101111
s
setvector in 0101011010
s
setvector in 1000111100
s
setvector in 1000101010
s
setvector in 1110101101
s
setvector in 0001101111
s
setvector in 0001101100
s
setvector in 0110010001
s
setvector in 0111000011
s
logfile
exit
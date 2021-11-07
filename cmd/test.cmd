logfile log/test.txt
stepsize 50
h vdd! 
l vss! 
l cin 
vector A a3 a2 a1 a0 
vector B b3 b2 b1 b0 
vector op s1 s0 
vector C_out cout 
vector out aluout3 aluout2 aluout1 aluout0 
vector in s1 s0 a3 a2 a1 a0 b3 b2 b1 b0 
w in out C_out a b op 
analyzer A B op C_out out in 
setvector in 1101011010
s
setvector in 0101110011
s
setvector in 0111000001
s
setvector in 1010011100
s
setvector in 1010100110
s
setvector in 1100100110
s
setvector in 0100100101
s
setvector in 0101001101
s
setvector in 0110101001
s
setvector in 0111110110
s
setvector in 0100100101
s
setvector in 0111001100
s
setvector in 0001110100
s
setvector in 0000111010
s
setvector in 0010001101
s
setvector in 0000000111
s
setvector in 1100011111
s
setvector in 1010010001
s
setvector in 0011111001
s
setvector in 0000101110
s
setvector in 0101100000
s
setvector in 0100101101
s
setvector in 0001010011
s
setvector in 1100011001
s
setvector in 1011111011
s
setvector in 0101011000
s
setvector in 0011000010
s
setvector in 0100101101
s
setvector in 1110000101
s
setvector in 0011000111
s
setvector in 1101010010
s
setvector in 1001000001
s
setvector in 1010010101
s
setvector in 0000000001
s
setvector in 1100001110
s
setvector in 1101101100
s
setvector in 0001001111
s
setvector in 1000000010
s
setvector in 1010000111
s
setvector in 0010000100
s
setvector in 0101110110
s
setvector in 0111100100
s
setvector in 1111001110
s
setvector in 1110010101
s
setvector in 0011100101
s
setvector in 1111001010
s
setvector in 0100001001
s
setvector in 1001011100
s
setvector in 0000100100
s
setvector in 0011010101
s
setvector in 0110101001
s
setvector in 1001010101
s
setvector in 1110011101
s
setvector in 1001011101
s
setvector in 0011011111
s
setvector in 1100001100
s
setvector in 1011110011
s
setvector in 1110111110
s
setvector in 0011110010
s
setvector in 1110110001
s
setvector in 1111010110
s
setvector in 0101100100
s
setvector in 0000111111
s
setvector in 0001011101
s
setvector in 1000010010
s
setvector in 1100100100
s
setvector in 1101111000
s
setvector in 1000110000
s
setvector in 0011011101
s
setvector in 1110011000
s
setvector in 0101110010
s
setvector in 1100111100
s
setvector in 0010111110
s
setvector in 1101100010
s
setvector in 1110111111
s
setvector in 0000111110
s
setvector in 0111000111
s
setvector in 1101111101
s
setvector in 1101011010
s
setvector in 1010111001
s
setvector in 1110101001
s
setvector in 1000100010
s
setvector in 0100110001
s
setvector in 1001101000
s
setvector in 0111101011
s
setvector in 0100011110
s
setvector in 0110011100
s
setvector in 1001011011
s
setvector in 0101010110
s
setvector in 1011010110
s
setvector in 1011001001
s
setvector in 1110000100
s
setvector in 1101111101
s
setvector in 0110000000
s
setvector in 0111111011
s
setvector in 1110100001
s
setvector in 1010001101
s
setvector in 1010000100
s
setvector in 1110001010
s
setvector in 0111110101
s
logfile
exit
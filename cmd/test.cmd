logfile log/test.txt
stepsize 50
h vdd 
l GND 
vector A A3 A2 A1 A0 
vector B B3 B2 B1 B0 
vector op op1 op0 
vector sum S3 S2 S1 S0 
vector C_out C3 
vector and and3 and2 and1 and0 
vector or or3 or2 or1 or0 
vector xor xor3 xor2 xor1 xor0 
vector out out3 out2 out1 out0 
vector in op1 op0 A3 A2 A1 A0 B3 B2 B1 B0 
w in out C_out 
analyzer A B op sum C_out and or xor out in 
setvector in 1001011010
s
setvector in 1101000000
s
setvector in 1010001110
s
logfile
exit
import sys
import random

cmd_path = 'cmd/'
log_path = 'log/'

high = 'vdd'
low = 'GND'

node_opA = ['A3', 'A2', 'A1', 'A0']
node_opB = ['B3', 'B2', 'B1', 'B0']
node_sum = ['S3', 'S2', 'S1', 'S0']
node_carry = 'C3'
node_and = ['and3', 'and2', 'and1', 'and0']
node_or = ['or3', 'or2', 'or1', 'or0']
node_xor = ['xor3', 'xor2', 'xor1', 'xor0']
node_out = ['out3', 'out2', 'out1', 'out0']

vectors = { 'A': ['A', node_opA],
            'B': ['B', node_opB],
            'Sum': ['sum', node_sum],
            'Carry out': ['C_out', node_carry],
            'And': ['and', node_and],
            'Or': ['or', node_or],
            'Xor': ['xor', node_xor],
            'Out': ['out', node_out],
            }

# filename_cmd = cmd_path + 'test.txt'
filename_cmd = cmd_path + 'test.cmd'
filename_log = log_path + 'test.cmd'

file = open(filename_cmd, 'w')

#IRSIM codes
#-------------------------------------------------------
#setting up the file
file.write(f'logfile {log_path}\n')
file.write('stepsize 50\n')
file.write(f'h {high} \n')
file.write(f'l {low} \n')

#generating vectors
for vector_name in vectors:
    vector = vectors[vector_name]
    file.write(f'vector {vector[0]} ')
    for node in vector[1]:
        if vector_name == 'Carry out':
            file.write(f'{vector[1]} ')
            break
        file.write(f'{node} ')
    file.write(f'\n')

#setting up analyzer
file.write('analyzer ')
for vector_name in vectors:
    vector = vectors[vector_name]
    file.write(f'{vector[0]} ')
file.write('\n')

#running simulations
a = random.randint(0, 2**4)
b = random.randint(0, 2**4)
print(a,b)
file.write(f'setvector A {a:04b}\n')
file.write(f'setvector B {b:04b}\n')
file.write('s\n')
file.write('logfile\n')
file.write('exit')
file.close
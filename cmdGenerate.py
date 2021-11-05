import random

tests = int(input('Enter how many tests you want to perform : '))
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
node_op = ['op1', 'op0']
node_in = node_op + node_opA + node_opB

vectors = { 'A': ['A', node_opA],
            'B': ['B', node_opB],
            'Opcode': ['op', node_op],
            'Sum': ['sum', node_sum],
            'Carry out': ['C_out', node_carry],
            'And': ['and', node_and],
            'Or': ['or', node_or],
            'Xor': ['xor', node_xor],
            'Out': ['out', node_out],
            'In' : ['in', node_in]
            }

# filename_cmd = cmd_path + 'test.txt'
temp_name = input('Enter name of the cmd file: ')
filename_cmd = cmd_path + temp_name + '.cmd'
filename_log = log_path + temp_name + '.txt'

file = open(filename_cmd, 'w')

#IRSIM codes
#-------------------------------------------------------
#setting up the file
file.write(f'logfile {filename_log}\n')
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

#watching vectors
file.write(f'w in out C_out \n')

#setting up analyzer
file.write('analyzer ')
for vector_name in vectors:
    vector = vectors[vector_name]
    file.write(f'{vector[0]} ')
file.write('\n')

#running simulations
for i in range(tests):
    instruction = random.randint(0, 2**10)
    file.write(f'setvector in {instruction:010b}\n')
    file.write('s\n')
file.write('logfile\n')
file.write('exit')
file.close
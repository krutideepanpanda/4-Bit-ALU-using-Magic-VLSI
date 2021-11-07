import random

tests = int(input('Enter how many tests you want to perform : '))

high = 'vdd!'
low = 'vss!'

node_opA = ['a3', 'a2', 'a1', 'a0']
node_opB = ['b3', 'b2', 'b1', 'b0']
node_carry = 'cout'
node_out = ['aluout3', 'aluout2', 'aluout1', 'aluout0']
node_op = ['s1', 's0']
node_in = node_op + node_opA + node_opB

vectors = { 'A': ['A', node_opA],
            'B': ['B', node_opB],
            'Opcode': ['op', node_op],
            'Carry out': ['C_out', node_carry],
            'Out': ['out', node_out],
            'In' : ['in', node_in]
            }

# filename_cmd = cmd_path + 'test.txt'
filename_cmd = 'cmd/test.cmd'
filename_log = 'log/test.txt'

file = open(filename_cmd, 'w')

#IRSIM codes
#-------------------------------------------------------
#setting up the file
file.write(f'logfile {filename_log}\n')
file.write('stepsize 50\n')
file.write(f'h {high} \n')
file.write(f'l {low} \n')
file.write(f'l cin \n')

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
file.write(f'w in out C_out a b op \n')

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
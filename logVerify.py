def unsign2sign(num):
    if num>127:
        num-=256
    return num

def checkAND(opA, opB, aluout):
    expected = opA & opB
    if aluout==expected:
        return True
    return False

def checkADD(opA, opB, aluout, cout):
    expected = opA + opB
    # cout for overflow
    if aluout + 256*cout == expected:
        return True
    return False

def checkOR(opA, opB, aluout):
    expected = opA | opB
    if aluout==expected:
        return True
    return False

correct=0
testcases=0

file = open('log/test.txt', "r")
lines = file.readlines()

#reading the log file
for i in range(0, len(lines), 2):
    log = lines[i].split()

    # read data from file
    op = (int(log[1][3:], 2))
    B = (int(log[2][2:], 2))
    A = (int(log[3][2:], 2))
    cout = (int(log[4][6], 2))

    out = 0
    if op != 3:
        out = (int(log[5][4:], 2))
    else:
        out = -100
    
    if op==0:
        flag=checkOR(A, B, out)
    elif op==1:
        flag=checkAND(A, B, out)
    elif op==2:
        flag=checkADD(A, B, out, cout)
    else:
        if log[5][4:] == 'XXXX':
            flag = True
        else:
            flag = False
        
    if flag:
        correct+=1
    else:
        print("The following inputs are causing unexpected behaviour-")
        print(f"\tA: {A}, B: {B}, op:{op}")
    testcases+=1
    
accuracy = (correct*100.0)/testcases
print(f"Accuracy of simulation: {accuracy}%\n")
file.close()
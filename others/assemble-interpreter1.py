# Simple assembler interpreter wich supports a few instructions

def sipmle_assembler(program: str) -> dict:
    global registers
    global flow
    global lines
    registers = dict()
    lines = {iterations: line for iterations, line in enumerate(program)}
    flow = 0

    def mov(register: str, value: str) -> None:
        global flow
        if value.lstrip('-').isnumeric():
            registers[register] = int(value)
        elif value.isalpha():
            registers[register] = registers[value]
        else:
            print('Erorr! Wrong type.')
        flow += 1
        return


    def inc(register: str) -> None:
        global flow
        flow += 1
        registers[register] += 1
        return
    

    def dec(register: str) -> None:
        global flow
        flow += 1
        registers[register] -= 1
        return
    

    def jnz(register: str, offset: str) -> None:
        global flow
        if register.isdigit():
            if int(register) == 0:
                flow += 1
            else:
                flow += int(offset)
        elif int(registers[register]) != 0:
            flow += int(offset)
        else:
            flow += 1
        return


    # Programm cycle
    while flow < len(lines):
        line = lines[flow].split()
        if line[0] == 'mov':
            mov(line[1], line[2])
        elif line[0] == 'inc':
            inc(line[1])
        elif line[0] == 'dec':
            dec(line[1])
        elif line[0] == 'jnz':
            jnz(line[1], line[2])
        else:
            print('Erorr! Unknown instruction.')
    
    return registers


def main():
    code1 = ['mov d 100','dec d','mov b d','jnz b -2','inc d','mov a d','jnz 5 10','mov c a']
    print(sipmle_assembler(code1))

if __name__ == '__main__':
    main()

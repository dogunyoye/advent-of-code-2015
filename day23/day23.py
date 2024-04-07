import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day23.txt')


class Computer(object):

    def __init__(self, registers, program, instruction_pointer):
        self.registers = registers
        self.program = program
        self.instruction_pointer = instruction_pointer

    def __parse_instruction(self, instruction) -> tuple:
        ins = instruction.replace(",", "")
        parts = ins.split(" ")
        ins_type = parts[0]
        if ins_type == "jie" or ins_type == "jio":
            return parts[0], parts[1], eval(parts[2])
        elif ins_type == "jmp":
            return parts[0], eval(parts[1])
        return parts[0], parts[1]

    def __hlf(self, reg):
        self.registers[reg] //= 2

    def __tpl(self, reg):
        self.registers[reg] *= 3

    def __inc(self, reg):
        self.registers[reg] += 1

    def __jmp(self, offset) -> int:
        return self.instruction_pointer + offset

    def __jie(self, reg, offset) -> int:
        if self.registers[reg] % 2 == 0:
            return self.instruction_pointer + offset
        return self.instruction_pointer + 1

    def __jio(self, reg, offset) -> int:
        if self.registers[reg] == 1:
            return self.instruction_pointer + offset
        return self.instruction_pointer + 1

    def execute_program(self):
        while 0 <= self.instruction_pointer < len(self.program):
            instruction = self.program[self.instruction_pointer]
            instruction = self.__parse_instruction(instruction)
            instruction_type = instruction[0]

            if instruction_type == "hlf":
                self.__hlf(instruction[1])
            elif instruction_type == "tpl":
                self.__tpl(instruction[1])
            elif instruction_type == "inc":
                self.__inc(instruction[1])
            elif instruction_type == "jmp":
                self.instruction_pointer = self.__jmp(instruction[1])
                continue
            elif instruction_type == "jie":
                self.instruction_pointer = self.__jie(instruction[1], instruction[2])
                continue
            elif instruction_type == "jio":
                self.instruction_pointer = self.__jio(instruction[1], instruction[2])
                continue

            self.instruction_pointer += 1


def find_value_in_register_b(data) -> int:
    computer = Computer({"a": 0, "b": 0}, data.splitlines(), 0)
    computer.execute_program()
    return computer.registers["b"]


def find_value_in_register_b_when_register_a_is_initialised_to_one(data) -> int:
    computer = Computer({"a": 1, "b": 0}, data.splitlines(), 0)
    computer.execute_program()
    return computer.registers["b"]


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_value_in_register_b(data)))
        print("Part 2: " + str(find_value_in_register_b_when_register_a_is_initialised_to_one(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

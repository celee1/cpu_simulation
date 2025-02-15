class CPU:
    def __init__(self):
        self.registers = {f"${i}": 0 for i in range(32)}  # 32 general-purpose registers
        self.memory = {}  # Memory dictionary (address -> value)
        self.pc = 0  # Program Counter

        # Instruction Set using Lambda Functions
        self.instruction_set = {
            "ADD": lambda rd, rs, rt: self.registers.update({rd: self.registers[rs] + self.registers[rt]}),
            "ADDI": lambda rt, rs, imm: self.registers.update({rt: self.registers[rs] + imm}),
            "SUB": lambda rd, rs, rt: self.registers.update({rd: self.registers[rs] - self.registers[rt]}),
            "MULT": lambda rs, rt: self.registers.update({"HI": self.registers[rs] * self.registers[rt] // (2**32),
                                                           "LO": self.registers[rs] * self.registers[rt] % (2**32)}),
            "DIV": lambda rs, rt: self.registers.update({"LO": self.registers[rs] // self.registers[rt], 
                                                         "HI": self.registers[rs] % self.registers[rt]}),
            "AND": lambda rd, rs, rt: self.registers.update({rd: self.registers[rs] & self.registers[rt]}),
            "OR": lambda rd, rs, rt: self.registers.update({rd: self.registers[rs] | self.registers[rt]}),
            "XOR": lambda rd, rs, rt: self.registers.update({rd: self.registers[rs] ^ self.registers[rt]}),
            "NOR": lambda rd, rs, rt: self.registers.update({rd: ~(self.registers[rs] | self.registers[rt])}),
            "SLL": lambda rd, rt, shamt: self.registers.update({rd: self.registers[rt] << shamt}),
            "SRL": lambda rd, rt, shamt: self.registers.update({rd: self.registers[rt] >> shamt}),
            "LW": lambda rt, offset, rs: self.registers.update({rt: self.memory.get(self.registers[rs] + offset, 0)}),
            "SW": lambda rt, offset, rs: self.memory.update({self.registers[rs] + offset: self.registers[rt]}),
            "BNE": lambda rs, rt, offset: setattr(self, 'pc', self.pc + offset if self.registers[rs] != self.registers[rt] else self.pc),
            "BEQ": lambda rs, rt, offset: setattr(self, 'pc', self.pc + offset if self.registers[rs] == self.registers[rt] else self.pc),
            "BGTZ": lambda rs, offset: setattr(self, 'pc', self.pc + offset if self.registers[rs] > 0 else self.pc),
            "BLEZ": lambda rs, offset: setattr(self, 'pc', self.pc + offset if self.registers[rs] <= 0 else self.pc),
            "J": lambda target: setattr(self, 'pc', target),
            "JAL": lambda target: (self.registers.update({"$ra": self.pc}), setattr(self, 'pc', target)),
            "CACHE": lambda mode: print(f"Cache {'enabled' if mode else 'disabled'}"),
            "HALT": lambda: setattr(self, 'pc', -1)  # Halt sets pc to -1
        }

    def run(self, instructions):
        """ Executes a list of instructions. """
        while self.pc < len(instructions) and self.pc != -1:
            instr = instructions[self.pc].split()
            opcode = instr[0]
            args = [int(x) if x.isdigit() else x for x in instr[1:]]  # Convert numbers, keep register names
            if opcode in self.instruction_set:
                self.instruction_set[opcode](*args)
            self.pc += 1  # Increment PC unless modified by branch/jump

# Example Usage
cpu = CPU()
instructions = [
    "ADDI $t1 $t0 5",
    "ADD $t2 $t1 $t0",
    "SW $t2 4($t3)",
    "LW $t4 4($t3)",
    "BNE $t4 $t2 2",
    "HALT"
]
cpu.run(instructions)

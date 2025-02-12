class CPU:
    def __init__(self):
        self.registers = [0] * 32  # 32 general-purpose registers
        self.pc = 0  # Program counter
        self.memory = [0] * 1024  # Simplified memory
        self.cache_enabled = True
    
    def fetch_instruction(self, instructions):
        if self.pc < len(instructions):
            return instructions[self.pc]
        return "HALT"
    
    def execute_instruction(self, instruction):
        parts = instruction.split()
        op = parts[0]
        
        if op == "ADD":
            rd, rs, rt = map(int, parts[1:])
            self.registers[rd] = self.registers[rs] + self.registers[rt]
            print(f"Result: {self.registers[rd]}")
        elif op == "ADDI":
            rt, rs, immd = map(int, parts[1:])
            self.registers[rt] = self.registers[rs] + immd
            print(f"Result: {self.registers[rt]}")
        elif op == "SUB":
            rd, rs, rt = map(int, parts[1:])
            self.registers[rd] = self.registers[rs] - self.registers[rt]
            print(f"Result: {self.registers[rd]}")
        elif op == "SLT":
            rd, rs, rt = map(int, parts[1:])
            self.registers[rd] = 1 if self.registers[rs] < self.registers[rt] else 0
            print(f"Result: {self.registers[rd]}")
        elif op == "BNE":
            rs, rt, offset = map(int, parts[1:])
            if self.registers[rs] != self.registers[rt]:
                self.pc += offset
        elif op == "J":
            target = int(parts[1])
            self.pc = target
        elif op == "JAL":
            target = int(parts[1])
            self.registers[7] = self.pc + 1
            self.pc = target
        elif op == "LW":
            rt, offset, rs = map(int, parts[1:])
            self.registers[rt] = self.memory[self.registers[rs] + offset]
            print(f"Loaded: {self.registers[rt]}")
        elif op == "SW":
            rt, offset, rs = map(int, parts[1:])
            self.memory[self.registers[rs] + offset] = self.registers[rt]
            print(f"Stored: {self.registers[rt]}")
        elif op == "CACHE":
            code = int(parts[1])
            if code == 0:
                self.cache_enabled = False
            elif code == 1:
                self.cache_enabled = True
            elif code == 2:
                print("Cache flushed")
        elif op == "HALT":
            print("Execution halted.")
            return False
        
        self.pc += 1  # Increment PC unless changed by branch/jump
        return True
    
    def run(self, instructions):
        running = True
        while running:
            instr = self.fetch_instruction(instructions)
            print(f"Executing: {instr}")
            running = self.execute_instruction(instr)

# Example usage
if __name__ == "__main__":
    cpu = CPU()
    instruction_list = [
        "ADDI 1 0 10",  # R1 = R0 + 10
        "ADDI 2 0 5",   # R2 = R0 + 5
        "ADD 3 1 2",    # R3 = R1 + R2
        "SUB 4 3 2",    # R4 = R1 - R2
        "SLT 5 2 3",    # R5 = 1 if R2 < R3 else 0
        "BNE 1 2 2",    # If R1 != R2, skip next instruction
        "J 6",          # Jump to instruction at index 6
        "CACHE 2",      # Flush cache
        "HALT"
    ]
    cpu.run(instruction_list)
    
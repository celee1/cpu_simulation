# CPU Simulator

## Overview
This project is a simple CPU simulator that executes a subset of MIPS-like instructions. The simulator includes a register file, program counter (PC), memory, and basic instruction execution logic.

## Features
- Supports core MIPS instructions, including arithmetic, logical, branching, memory access, and cache operations.
- Implements a simple memory model.
- Provides a basic simulation of execution flow with a program counter.

## Supported Instructions
The simulator currently supports the following MIPS instructions:

### **Arithmetic and Logical Operations**
- `ADD rd, rs, rt` – rd = rs + rt
- `ADDI rt, rs, imm` – rt = rs + imm
- `SUB rd, rs, rt` – rd = rs - rt
- `MULT rs, rt` – Multiplies rs and rt, stores result in HI/LO registers
- `DIV rs, rt` – Divides rs by rt, quotient in LO, remainder in HI
- `AND rd, rs, rt` – rd = rs & rt
- `OR rd, rs, rt` – rd = rs | rt
- `XOR rd, rs, rt` – rd = rs ^ rt
- `NOR rd, rs, rt` – rd = ~(rs | rt)
- `SLL rd, rt, shamt` – rd = rt << shamt (logical shift left)
- `SRL rd, rt, shamt` – rd = rt >> shamt (logical shift right)

### **Branching and Control Flow**
- `BNE rs, rt, offset` – Branch to offset if rs ≠ rt
- `BEQ rs, rt, offset` – Branch to offset if rs == rt
- `BGTZ rs, offset` – Branch if rs > 0
- `BLEZ rs, offset` – Branch if rs ≤ 0
- `J target` – Jump to target address
- `JAL target` – Jump to target and store return address in `$ra`

### **Memory Operations**
- `LW rt, offset(rs)` – Load word from memory to register rt
- `SW rt, offset(rs)` – Store word from register rt to memory

### **Other Operations**
- `CACHE on/off` – Enables or disables cache simulation
- `HALT` – Stops execution

## Usage
To use the CPU simulator, provide a list of instructions to the `run` method:

```python
cpu = CPU()
instructions = [
    "ADD 1 2 3",
    "SW 1 0(5)",
    "LW 4 0(5)",
    "HALT"
]
cpu.run(instructions)
```

## Future Improvements
- Expand instruction set
- Implement pipeline processing
- Add I/O simulation
- Improve memory management

## License
This project is released under the MIT License.


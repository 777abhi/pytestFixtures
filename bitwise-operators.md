Bitwise operators are used in Python to perform bit-level operations on binary numbers (integers). Each bitwise operator treats their operands as a sequence of 32 or 64 bits (depending on the system), rather than as decimal, hexadecimal, or octal numbers. Here's an explanation of each bitwise operator with examples:

1. **AND Operator `&`**:
   - Compares each bit of the first operand to the corresponding bit of the second operand. If both bits are `1`, the corresponding result bit is set to `1`. Otherwise, it is set to `0`.
   - Example:
     ```python
     a = 12  # binary: 1100
     b = 6   # binary: 0110
     print(a & b)  # Output: 4 (binary: 0100)
     ```

2. **OR Operator `|`**:
   - Compares each bit of the first operand to the corresponding bit of the second operand. If either bit is `1`, the corresponding result bit is set to `1`.
   - Example:
     ```python
     a = 12  # binary: 1100
     b = 6   # binary: 0110
     print(a | b)  # Output: 14 (binary: 1110)
     ```

3. **XOR Operator `^`**:
   - Compares each bit of the first operand to the corresponding bit of the second operand. If the bits are different, the corresponding result bit is set to `1`. If the bits are the same, the result bit is `0`.
   - Example:
     ```python
     a = 12  # binary: 1100
     b = 6   # binary: 0110
     print(a ^ b)  # Output: 10 (binary: 1010)
     ```

4. **NOT Operator `~`**:
   - Inverts all the bits of the operand.
   - Example:
     ```python
     a = 12  # binary: 1100
     print(~a)  # Output: -13 (binary: ...11110011)
     ```
   - Note: The output is `-13` because Python uses a signed binary representation called two's complement.

5. **Left Shift Operator `<<`**:
   - Shifts the bits of the first operand to the left by the number of positions specified by the second operand. New bits on the right are filled with `0`.
   - Example:
     ```python
     a = 12  # binary: 1100
     print(a << 2)  # Output: 48 (binary: 110000)
     ```

6. **Right Shift Operator `>>`**:
   - Shifts the bits of the first operand to the right by the number of positions specified by the second operand. For positive numbers, new bits on the left are filled with `0`. For negative numbers, new bits are filled with `1`.
   - Example:
     ```python
     a = 12  # binary: 1100
     print(a >> 2)  # Output: 3 (binary: 0011)
     ```

These operators are particularly useful in low-level programming, such as when you're dealing with binary data in network protocols or file formats. 🐍✨
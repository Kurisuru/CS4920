# Mix-Columns.py
# This program implements the Mix-Columns step of the AES algorithm.
# The Mix-Columns step takes a 4x4 matrix of bytes (the state) and transforms it using a specific mathematical operation.
# The transformation is defined as follows:
# | s0,0 | s0,1 | s0,2 | s0,3 | --> | s0,0' | s0,1' | s0,2' | s0,3' |
# | s1,0 | s1,1 | s1,2 | s1,3 |     | s1,0' | s1,1' | s1,2' | s1,3' |
# | s2,0 | s2,1 | s2,2 | s2,3 |     | s2,0' | s2,1' | s2,2' | s2,3' |
# | s3,0 | s3,1 | s3,2 | s3,3 |     | s3,0' | s3,1' | s3,2' | s3,3' |
import numpy as np


def mix_columns(state):
    transormation_matrix = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]
    output_state = state @ transormation_matrix
    output_state = output_state % 256
    return output_state



if __name__ == "__main__":
    input_file_name = input("Enter name of input file: ").strip()
    output_file_name = input_file_name.replace("input", "output")

    with open(input_file_name, "r", encoding="utf-8") as infile, \
         open(output_file_name, "a", encoding="utf-8") as outfile:
        for line in infile:
            s = line.strip()
            if not s:
                continue
            if len(s) != 32 or any(c not in "0123456789abcdefABCDEF" for c in s):
                print(f"Invalid input line (expect 32 hex chars): {s}")
                continue

            # parse contiguous hex string into 16 bytes
            state = np.array([int(s[i:i+2], 16) for i in range(0, 32, 2)])
            # form 4x4 state matrix (4 rows of 4 bytes)
            state_matrix = np.array([state[i:i+4] for i in range(0, 16, 4)])

            output_state = mix_columns(state_matrix)

            # output as contiguous hex string (uppercase)
            output_line = "".join(f"{byte:02X}" for row in output_state for byte in row)
            print(output_line)
            outfile.write(output_line + "\n")
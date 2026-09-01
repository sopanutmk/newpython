import struct

with open('employees.dat', 'rb') as file:
    data = file.read(struct.calcsize('i20sif'))
    record = struct.unpack('i20sif', data)
    record = (record[0],record[1].decode().rstrip('\x00'), record[2], record[3])
    print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Salary: ${record[3]:.2f}")
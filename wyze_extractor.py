#!/usr/bin/env python3

import sys

class FirmwarePart:
    def __init__(self, name, offset, size):
        self.name = name
        self.offset = offset
        self.size = size

firmware_parts = [
    FirmwarePart("uimage_header", 0x0, 0x40),
    FirmwarePart("uimage_kernel", 0x40, 0x200000),
    FirmwarePart("squashfs_1", 0x200040, 0x350000),
    FirmwarePart("squashfs_2", 0x550040, 0xa0000),
    FirmwarePart("jffs2", 0x5f0040, 11075648-0x5f0040)
]

if sys.argv[1] == "unpack":
    f = open(sys.argv[2], "rb")
    for part in firmware_parts:
        outfile = open(part.name, "wb")
        f.seek(part.offset, 0)
        data = f.read(part.size)
        outfile.write(data)
        outfile.close()
        print(f"Wrote {part.name} - {hex(len(data))} bytes")
elif sys.argv[1] == "pack":
    f = open(sys.argv[2], "wb")
    for part in firmware_parts[1:]:
        i = open(part.name, "rb")
        data = i.read()
        f.write(data)
        padding = (part.size - len(data))
        print(f"Wrote {part.name} - {hex(len(data))} bytes")
        print(f"Padding: {hex(padding)}")
        f.write(b'\x00' * padding)

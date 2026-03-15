import psycopg2
import json

def read_uint(data, offset, length, endian="little"):
    """
    指定バイトを整数へ変換
    """
    return int.from_bytes(data[offset:offset+length], endian)


def parse_cond(cond_bytes):

    offset = 0
    result = {}

    # -------------------------
    # ヘッダ
    # -------------------------

    data_size = read_uint(cond_bytes, offset, 2)
    offset += 2

    data_count = read_uint(cond_bytes, offset, 2)
    offset += 2

def main():
    cord =0b00001100

    bit1   =  cord & 0b00000001
    bit2   =  cord & 0b00000010
    bit3 = cord & 0b00000100
    bit4    = cord & 0b00001000

    if bit1 or bit2:
        print("bit1 or bit2 is set")

    if bit3:
        print("bit3 is set")

    if bit4:
        print("bit4 is set")

if __name__ == "__main__":
    main()

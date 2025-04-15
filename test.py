def to_hex(n):
    return hex(n)

def from_hex(h):
    return int(h, 16)

# Example usage
if __name__ == "__main__":
    print("Hex of 255:", to_hex(255))       # Prints 0xff
    print("Decimal of 0xff:", from_hex("0xff"))  # Prints 255

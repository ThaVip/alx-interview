#!/usr/bin/python3
def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding."""
    num_bytes = 0
    
    for num in data:
        byte = num & 0xFF  # Consider only the least significant 8 bits

        if num_bytes == 0:
            # Determine the number of bytes in the current UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                # The first byte should start with '0' for 1-byte characters
                return False
        else:
            # Subsequent bytes must start with '10' (i.e., have a leading '10xxxxxx')
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If we finished and processed all expected continuation bytes, it's valid
    return num_bytes == 0

import os
import struct
import hashlib

def generate_uuid():
    """
    Generate a cryptographically random UUID.
    """
    # Get 128 random bits
    random_bits = bytearray(os.urandom(16))

    # Set the variant and version bits
    random_bits[8] = random_bits[8] & 0x3f | 0x80
    random_bits[6] = random_bits[6] & 0x0f | 0x40

    # Convert the random bits to a UUID string
    uuid = struct.unpack('>I', random_bits[0:4])[0]
    uuid = uuid << 32
    uuid = uuid | struct.unpack('>I', random_bits[4:8])[0]
    uuid = uuid << 32
    uuid = uuid | struct.unpack('>I', random_bits[8:12])[0]
    uuid = uuid << 32
    uuid = uuid | struct.unpack('>I', random_bits[12:16])[0]

    return '{:x}'.format(uuid)
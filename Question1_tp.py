def apply_permutation(data, permutation):
    return ''.join(data[i] for i in permutation)

def feistel_key_generation(key, permutation, shift_order):
    key_permuted = apply_permutation(key, permutation)
    k1 = key_permuted[:4]
    k2 = key_permuted[4:]

    k1_xor_k2 = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(k1, k2))
    k2_and_k1 = ''.join(str(int(b1) & int(b2)) for b1, b2 in zip(k2, k1))

    k1_shifted = k1_xor_k2[shift_order:] + k1_xor_k2[:shift_order]
    k2_shifted = k2_and_k1[-shift_order:] + k2_and_k1[:-shift_order]

    return k1_shifted, k2_shifted

def feistel_encryption(block, permutation, shift_order, key):
    permutation_pi = apply_permutation(block, permutation)

    left_half = permutation_pi[:4]
    right_half = permutation_pi[4:]

    k1, k2 = feistel_key_generation(key, permutation, shift_order)

    d1 = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(left_half, k1))
    g1 = ''.join(str(int(b1) ^ (int(b2) | int(k1))) for b1, b2 in zip(right_half, k1))

    d2 = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(g1, k2))
    g2 = ''.join(str(int(b1) ^ (int(b2) | int(k2))) for b1, b2 in zip(d1, k2))

    encrypted_block = g2 + d2

    return apply_permutation(encrypted_block, permutation)


# Exemple d'utilisation
permutation = [4, 6, 0, 2, 7, 3, 1, 5]
shift_order = 2
key = '10101010'
block = '11001100'

encrypted_block = feistel_encryption(block, permutation, shift_order, key)

print(f"Texte clair : {block}")
print(f"Texte chiffré : {encrypted_block}")
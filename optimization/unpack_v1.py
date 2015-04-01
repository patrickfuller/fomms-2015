"""
Unpacking atoms by applying symmetry operators. Uses atom-atom collision
detection to remove duplicates.
"""
import json
from math import sqrt
from sys import argv


def unpack(packed_crystal):
    """Apply symmetry operators to atoms. Returns a list of unique atoms."""
    unpacked_atoms = []
    for operation in packed_crystal["symmetry"]:
        op_1, op_2, op_3 = operation.split(",")
        for atom in packed_crystal["atoms"]:

            # Apply symmetry operator to atom location
            x, y, z = atom["location"]
            x1, y1, z1 = [i % 1 for i in eval(operation)]

            # Test if unpacked atom is colliding with an existing atom
            is_unique = True
            for unique_atom in unpacked_atoms:
                x2, y2, z2 = unique_atom["location"]
                distance = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
                if distance < 1e-3:
                    is_unique = False
                    break

            # If the atom is not colliding, add to list
            if is_unique:
                unpacked_atoms.append({"location": [x1, y1, z1],
                                       "element": atom["element"],
                                       "label": atom["label"]})

    return {"atoms": unpacked_atoms, "unitcell": packed_crystal["unitcell"]}


# Load crystal data through Python's json support, unpack, and print output
with open(argv[-1]) as in_file:
    crystal = json.load(in_file)
unpacked = unpack(crystal)
print(json.dumps(unpacked))

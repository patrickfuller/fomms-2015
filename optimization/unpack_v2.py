"""
Unpacking atoms by applying symmetry operators. Uses atom-atom collision
detection to remove duplicates.
"""
import json
from sys import argv


def unpack(packed_crystal):
    """Apply symmetry operators to atoms. Returns a list of unique atoms."""
    unpacked_atoms = []
    location_hashes = set()
    for operation in packed_crystal["symmetry"]:
        op_1, op_2, op_3 = operation.split(",")
        for atom in packed_crystal["atoms"]:

            # Apply symmetry operator to atom location
            x, y, z = atom["location"]
            x1, y1, z1 = [i % 1 for i in eval(operation)]

            # Test if unpacked atom is colliding with an existing atom
            location_hash = "{x:.2f},{y:.2f},{z:.2f}".format(x=x1, y=y1, z=z1)
            if location_hash not in location_hashes:
                location_hashes.add(location_hash)
                unpacked_atoms.append({"location": [x1, y1, z1],
                                       "element": atom["element"],
                                       "label": atom["label"]})

    return {"atoms": unpacked_atoms, "unitcell": packed_crystal["unitcell"]}


# Load crystal data through Python's json support, unpack, and print output
with open(argv[-1]) as in_file:
    crystal = json.load(in_file)
unpacked = unpack(crystal)
print(json.dumps(unpacked))

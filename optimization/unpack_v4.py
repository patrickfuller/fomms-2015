"""
Unpacking atoms by applying symmetry operators. Uses atom-atom collision
detection to remove duplicates.
"""
from ctypes import cdll, c_char_p, c_float, POINTER
import json
import os
from sys import argv

folder = os.path.normpath(os.path.dirname(__file__))
lib = cdll.LoadLibrary(os.path.join(folder, "unpack.so"))
CFloat3 = c_float * 3
lib.applySymmetry.argtypes = (CFloat3, c_char_p)
lib.applySymmetry.restype = POINTER(CFloat3)


def unpack(packed_crystal):
    """Apply symmetry operators to atoms. Returns a list of unique atoms."""
    unpacked_atoms = []
    location_hashes = set()
    for operation in packed_crystal["symmetry"]:
        for atom in packed_crystal["atoms"]:

            # Apply symmetry operator to atom location
            x1, y1, z1 = lib.applySymmetry(CFloat3(*atom["location"]),
                                           operation.encode("utf-8")).contents

            # Test if unpacked atom is colliding with an existing atom
            location_hash = "{x:.2f},{y:.2f},{z:.2f}".format(x=x1, y=y1, z=z1)
            if location_hash not in location_hashes:
                location_hashes.add(location_hash)
                unpacked_atoms.append({"location": [x1, y1, z1],
                                       "element": atom["element"],
                                       "label": atom["label"]})

    return {"atoms": unpacked_atoms, "unitcell": packed_crystal["unitcell"]}


# Load crystal data through Python's json support, unpack, and write output
with open(argv[-1]) as in_file:
    crystal = json.load(in_file)
unpacked = unpack(crystal)
with open("unpacked_v4.json", "w") as out_file:
    json.dump(unpacked, out_file)

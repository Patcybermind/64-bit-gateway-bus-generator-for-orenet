import mcschematic as mcs
import os
from eight_b_bus_gen import eight_bit_bus  # the function that generates a single gateway
# up there all I did was import all the necessary packages

# create a schematic
schem = mcs.MCSchematic()

# generating the gateways

# get coords from user
X = int(input("X : "))
Y = int(input("Y : "))
Z = int(input("Z : "))

xpos = int(input("X position : "))
ypos = int(input("Y position : "))
zpos = int(input("Z position : "))
alignment = input(
    "on what axis do you want it to be alignment on (x or z note that it is case sensitive so use lowercase) : ")
# ask for the axis to align it on x or z for blender users or other types of 3d software users, I know, I know usually
# the z axis is the vertical axis, but I didn't decide that, notch did or at least I think so
if alignment == "x":
    for byte in range(0, 8):
        schem = eight_bit_bus(xpos + byte * 2, ypos, zpos, X + byte * 2, Y, Z, schem)

elif alignment == "z":
    for byte in range(0, 8):
        schem = eight_bit_bus(xpos, ypos, zpos + byte * 2, X, Y, Z + byte * 2, schem)

# time to save
rootpath = os.path.expanduser('~')
print(f"your rootpath is {rootpath}")

savepath = r"\AppData\Roaming\.minecraft\config\worldedit\schematics"
print(f"your save path is {savepath}")

savepath = os.path.join(rootpath + savepath)
print(f"saving to {savepath}")

# time to write the save
try:
    schem.save("output", "_most recent", mcs.Version.JE_1_18_2)
except all:
    pass
# now to WE folder
try:
    schem.save(savepath, "1gateway", mcs.Version.JE_1_18_2)
    print("success! saved to your World Edit schematics folder and to the folder this program is running from")

except all:  # if the World Edit schematics folder isn't found

    print("looks like you don't have a World Edit schematics folder but don't worry the generated .schem file was still"
          "saved to the folder this program is running from")

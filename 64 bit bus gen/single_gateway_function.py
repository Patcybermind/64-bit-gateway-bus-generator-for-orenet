import mcschematic


def single_gateway(relx, rely, relz, xout, yout, zout, schem):
    # set up the nbt tag
    nbt_tag = "minecraft:end_gateway{Age:180,ExactTeleport:1,ExitPortal:" \
              "{X:" + str(xout) + ",Y:" + str(yout) + ",Z:" + str(zout) + "}}"
    print(nbt_tag)
    # place the blocks
    schem.setBlock((relx, rely, relz), nbt_tag)
    return schem

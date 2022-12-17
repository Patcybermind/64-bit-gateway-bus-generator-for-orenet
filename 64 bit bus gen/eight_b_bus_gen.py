from single_gateway_function import single_gateway
import mcschematic


def eight_bit_bus(relx, rely, relz, xout, yout, zout, schem):
    for bit in range(0, 8):
        print(f"iteration {bit}")
        offrely = rely - (bit * 2)
        offyout = int(yout) - (bit * 2)
        schem = single_gateway(relx, offrely, relz, xout, offyout, zout, schem)  # generates a gateway

    return schem
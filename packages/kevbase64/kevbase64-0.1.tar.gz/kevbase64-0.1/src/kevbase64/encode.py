from kevbase64.table import create_table


def base64_encode(data: bytes):
    binary_to_char = create_table()
    buffer = []

    for byte in data:
        # https://stackoverflow.com/questions/16926130/convert-to-binary-and-keep-leading-zeros
        for bit in format(byte, "08b"):
            buffer.append(bit)
            if len(buffer) == 6:
                yield binary_to_char[tuple(buffer)]
                buffer.clear()

    # remaining bits by taking N bits mod 6, should be 0, 2, or 4
    if len(buffer) > 0:
        padding = ["0"] * (6 - len(buffer))
        buffer += padding

        yield (binary_to_char[tuple(buffer)])

        if len(padding) == 4:
            yield (binary_to_char["padding"])
            yield (binary_to_char["padding"])
        elif len(padding) == 2:
            yield (binary_to_char["padding"])

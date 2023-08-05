from kevbase64.table import create_table


def base64_decode(data: str):
    char_to_binary = {v: k for k, v in create_table().items()}
    buffer = []

    for char in data:
        if char != "=":
            for bit in char_to_binary[char]:
                buffer.append(bit)
                if len(buffer) == 8:
                    yield chr(int("".join(buffer), 2))
                    buffer.clear()

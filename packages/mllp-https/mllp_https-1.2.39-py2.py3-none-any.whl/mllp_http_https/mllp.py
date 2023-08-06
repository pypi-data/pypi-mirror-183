import functools
import logging


class Format:
    START_BLOCK = 0x0B
    END_BLOCK = 0x1C
    CARRIAGE_RETURN = 0x0D


class State:
    AFTER_BLOCK = 0
    BEFORE_BLOCK = 1
    BLOCK = 2


def to_hex(byte):
    return "EOF" if byte is None else hex(byte)


def read_mllp(it):
    logger = logging.getLogger("mllp.parse")

    content = None
    state = State.BEFORE_BLOCK
    byte = None
    i = -1

    def advance():
        nonlocal byte
        nonlocal i
        byte = next(it, None)
        i += 1

    advance()
    while True:
        if state == State.AFTER_BLOCK:
            if byte == Format.CARRIAGE_RETURN:
                state = State.BEFORE_BLOCK
                advance()
            else:
                logger.error(
                    "Expected %s instead of %s (byte:%s)",
                    to_hex(Format.CARRIAGE_RETURN),
                    to_hex(byte),
                    i,
                )
                break
        elif state == State.BEFORE_BLOCK:
            if byte is None:
                break
            if byte == Format.START_BLOCK:
                content = bytearray()
                state = State.BLOCK
                advance()
            else:
                logger.error(
                    "Expected %s instead of %s (byte:%s)",
                    to_hex(Format.START_BLOCK),
                    to_hex(byte),
                    i,
                )
                break
        elif state == State.BLOCK:
            if byte == Format.START_BLOCK:
                logger.error(
                    "Expected content instead of %s (byte:%s)",
                    to_hex(Format.CARRIAGE_RETURN),
                    to_hex(byte),
                    i,
                )
                break
            elif byte == Format.END_BLOCK:
                yield bytes(content)
                content = None
                state = State.AFTER_BLOCK
                advance()
            else:
                content.append(byte)
                advance()


def parse_mllp(mllp_data):
    hl7_text = mllp_data.decode("utf-8")
    hl7_text = hl7_text.replace('\x0b', '')
    hl7_text = hl7_text.replace('\x1c\r', '')
    if not hl7_text.find("\r\n"):
        hl7_text = hl7_text.replace('\r', '\r\n')
    # if hl7_text.find("\x0d"):
    #     hl7_text = hl7_text.replace('\x0d', '\r\n')
    mllp_data = bytes(hl7_text, 'utf-8')
    return mllp_data


def write_mllp(wfile, content):
    wfile.write(bytes([Format.START_BLOCK]))
    wfile.write(content)
    wfile.write(bytes([Format.END_BLOCK, Format.CARRIAGE_RETURN]))
    # wfile.sendall(bytes([Format.START_BLOCK]))
    # wfile.sendall(content)
    # wfile.sendall(bytes([Format.END_BLOCK, Format.CARRIAGE_RETURN]))


def send_mllp(socket, content):
    # Send all data on MLLP
    socket.sendall(bytes([Format.START_BLOCK]))
    socket.sendall(content)
    socket.sendall(bytes([Format.END_BLOCK, Format.CARRIAGE_RETURN]))

    # Wait for the ACK/NACK
    response = socket.recv(4096)
    return response


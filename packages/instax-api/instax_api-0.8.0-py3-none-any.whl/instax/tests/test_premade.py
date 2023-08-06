"""
Instax SP2 Test File.

@jpwsutton 2016/17
"""
import unittest

from instax.packet import Packet, PacketFactory


class PacketTests(unittest.TestCase):
    """
    Instax-SP2 Premade Packet Test Class.

    A series of tests to verify that existing commands and responses can be
    correctly decoded.
    """

    def helper_verify_header(
        self,
        header,
        direction,
        type,
        length,
        time,
        pin=None,
        returnCode=None,
        unknown1=None,
        ejecting=None,
        battery=None,
        printCount=None,
    ):
        """Verify the Header of a packet."""
        self.assertEqual(header["startByte"], direction)
        self.assertEqual(header["cmdByte"], type)
        self.assertEqual(header["packetLength"], length)
        self.assertEqual(header["sessionTime"], time)
        if direction == Packet.MESSAGE_MODE_COMMAND:
            self.assertEqual(header["password"], pin)
        if direction == Packet.MESSAGE_MODE_RESPONSE:
            self.assertEqual(header["returnCode"], returnCode)
            # self.assertEqual(header['unknown1'], unknown1)
            self.assertEqual(header["ejecting"], ejecting)
            self.assertEqual(header["battery"], battery)
            self.assertEqual(header["printCount"], printCount)

    def test_premade_resp_specifications(self):
        """Test Decoding a Specifications Response with an existing payload."""
        msg = bytearray.fromhex(
            "2a4f 0030 e759 eede 0000 0000 0000 0027 0258"
            " 0320 0100 000a 0000 0000 ea60 1000 0000 0000"
            " 0000 0000 0000 0000 fa41 0d0a"
        )
        packetFactory = PacketFactory()
        decodedPacket = packetFactory.decode(msg)
        self.assertEqual(decodedPacket.payload["maxHeight"], 800)
        self.assertEqual(decodedPacket.payload["maxWidth"], 600)
        self.assertEqual(decodedPacket.payload["maxColours"], 256)
        self.assertEqual(decodedPacket.payload["unknown1"], 10)
        self.assertEqual(decodedPacket.payload["maxMsgSize"], 60000)
        self.assertEqual(decodedPacket.payload["unknown2"], 16)
        self.assertEqual(decodedPacket.payload["unknown3"], 0)

    def test_premade_resp_version(self):
        """Test Decoding a Version Response with an existing payload."""
        msg = bytearray.fromhex("2ac0 001c e759 eede 0000" " 0000 0000 0027 0101 0113" " 0000 0000 fbb0 0d0a")
        packetFactory = PacketFactory()
        decodedPacket = packetFactory.decode(msg)
        self.assertEqual(decodedPacket.payload["unknown1"], 257)
        self.assertEqual(decodedPacket.payload["firmware"], "01.13")
        self.assertEqual(decodedPacket.payload["hardware"], "00.00")

    def test_premade_resp_printCount(self):
        """Test Decoding a Print Count Response with an existing payload."""
        msg = bytearray.fromhex(
            "2ac1 0024 e759 eede 0000" " 0000 0000 0027 0000 0003" " 00f3 c048 0000 1645 001e" " 0000 f946 0d0a"
        )
        packetFactory = PacketFactory()
        decodedPacket = packetFactory.decode(msg)
        self.assertEqual(decodedPacket.payload["printHistory"], 3)

    def test_premade_cmd_modelName(self):
        """Test Decoding a Model Name Command."""
        msg = bytearray.fromhex("24c2 0010 0b8d c2b4 0457 0000 fca0 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_cmd_prePrint(self):
        """Test Decoding a Pre Print Command."""
        msg = bytearray.fromhex("24c4 0014 4e40 684c 0457" " 0000 0000 0008 fd5e 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_cmd_lock(self):
        """Test Decoding a Lock Command."""
        msg = bytearray.fromhex("24b3 0014 9619 02df 0457" " 0000 0100 0000 fd28 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_resp_lock(self):
        """Test Decoding a Lock Response."""
        msg = bytearray.fromhex("2ab3 0014 75b8 bd8e 0000" " 0000 0000 003a fc5c 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_cmd_reset(self):
        """Test Decoding a Reset Command."""
        msg = bytearray.fromhex("2450 0010 96c9 aada 0457" " 0000 fc3d 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_resp_reset(self):
        """Test Decoding a Reset Response."""
        msg = bytearray.fromhex("2a50 0014 75b8 bd8e 0000" " 0000 0000 003a fcbf 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_resp_prep(self):
        """Test Decoding a Prep Response."""
        msg = bytearray.fromhex("2451 001c 9b60 d511 0457" " 0000 1000 0015 f900 0000" "  0000 0000 fc14 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_resp_send(self):
        """Test decoding a send response."""
        msg = bytearray.fromhex("2a52 0018 75b8 bd8e 0000" " 0000 0000 003a 0000 0014 fca5 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_cmd_83(self):
        """Test decoding a type 83 command."""
        msg = bytearray.fromhex("2453 0010 c9a9 b71e 0457 0000 fcd6 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_resp_83(self):
        """Test decoding a type 83 response."""
        msg = bytearray.fromhex("2a53 0014 75b8 bd8e 0000" " 0000 0000 003a fcbc 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_cmd_lock_state(self):
        """Test decoding a Lock state command."""
        msg = bytearray.fromhex("24b0 0010 f776 ecbe 0457 0000 fba9 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_resp_lock_state(self):
        """Test decoding a Lock state response."""
        msg = bytearray.fromhex("2ab0 0018 f130 d7cc 0000 0000" " 0000 0036 0000 0064 fbaf 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_cmd_195(self):
        """Test decoding a 195 command."""
        msg = bytearray.fromhex("24c3 0010 f130 d7cc 0457 0000 fbe9 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_resp_195_first(self):
        """Test decoding a 195 first response."""
        msg = bytearray.fromhex("2ac3 0014 f130 d7cc 0000 0000" " 7f00 0436 fb81 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)

    def test_premade_resp_195_last(self):
        """Test decoding a 195 last response."""
        msg = bytearray.fromhex("2ac3 0014 f130 d7cc 0000 0000" " 0000 0035 fc05 0d0a")
        packetFactory = PacketFactory()
        packetFactory.decode(msg)


if __name__ == "__main__":

    unittest.main()

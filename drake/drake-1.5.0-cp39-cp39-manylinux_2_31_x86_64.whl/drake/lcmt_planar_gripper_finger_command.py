"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class lcmt_planar_gripper_finger_command(object):
    __slots__ = ["joint_position", "joint_velocity", "joint_torque"]

    __typenames__ = ["double", "double", "double"]

    __dimensions__ = [[2], [2], [2]]

    def __init__(self):
        self.joint_position = [ 0.0 for dim0 in range(2) ]
        self.joint_velocity = [ 0.0 for dim0 in range(2) ]
        self.joint_torque = [ 0.0 for dim0 in range(2) ]

    def encode(self):
        buf = BytesIO()
        buf.write(lcmt_planar_gripper_finger_command._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack('>2d', *self.joint_position[:2]))
        buf.write(struct.pack('>2d', *self.joint_velocity[:2]))
        buf.write(struct.pack('>2d', *self.joint_torque[:2]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != lcmt_planar_gripper_finger_command._get_packed_fingerprint():
            raise ValueError("Decode error")
        return lcmt_planar_gripper_finger_command._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = lcmt_planar_gripper_finger_command()
        self.joint_position = struct.unpack('>2d', buf.read(16))
        self.joint_velocity = struct.unpack('>2d', buf.read(16))
        self.joint_torque = struct.unpack('>2d', buf.read(16))
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if lcmt_planar_gripper_finger_command in parents: return 0
        tmphash = (0x1c9f9975f0aea67b) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if lcmt_planar_gripper_finger_command._packed_fingerprint is None:
            lcmt_planar_gripper_finger_command._packed_fingerprint = struct.pack(">Q", lcmt_planar_gripper_finger_command._get_hash_recursive([]))
        return lcmt_planar_gripper_finger_command._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", lcmt_planar_gripper_finger_command._get_packed_fingerprint())[0]


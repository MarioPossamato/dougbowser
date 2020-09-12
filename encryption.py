#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DougBowser
# Version 0.1
# Created by MarioPossamato

# This file is part of DougBowser.



from Crypto.Hash import CMAC
from Crypto.Cipher import AES
from Crypto import Random

from nintendo.sead import random
from nintendo.enl import crypto

import struct
import binascii
import zlib


KeyTable = [
	0x7AB1C9D2, 0xCA750936, 0x3003E59C, 0xF261014B,
	0x2E25160A, 0xED614811, 0xF1AC6240, 0xD59272CD,
	0xF38549BF, 0x6CF5B327, 0xDA4DB82A, 0x820C435A,
	0xC95609BA, 0x19BE08B0, 0x738E2B81, 0xED3C349A,
	0x045275D1, 0xE0A73635, 0x1DEBF4DA, 0x9924B0DE,
	0x6A1FC367, 0x71970467, 0xFC55ABEB, 0x368D7489,
	0x0CC97D1D, 0x17CC441E, 0x3528D152, 0xD0129B53,
	0xE12A69E9, 0x13D1BDB7, 0x32EAA9ED, 0x42F41D1B,
	0xAEA5F51F, 0x42C5D23C, 0x7CC742ED, 0x723BA5F9,
	0xDE5B99E3, 0x2C0055A4, 0xC38807B4, 0x4C099B61,
	0xC4E4568E, 0x8C29C901, 0xE13B34AC, 0xE7C3F212,
	0xB67EF941, 0x08038965, 0x8AFD1E6A, 0x8E5341A3,
	0xA4C61107, 0xFBAF1418, 0x9B05EF64, 0x3C91734E,
	0x82EC6646, 0xFB19F33E, 0x3BDE6FE2, 0x17A84CCA,
	0xCCDF0CE9, 0x50E4135C, 0xFF2658B2, 0x3780F156,
	0x7D8F5D68, 0x517CBED1, 0x1FCDDF0D, 0x77A58C94
]


CourseMagic = bytes.hex(b'SCDL')


def DecryptCourse(Buffer):

    HeaderSize = 0x10
    CryptoConfig = Buffer[-0x30:]
    Data = Buffer[0x10:-0x30]
    Context = struct.unpack_from("<IIII", CryptoConfig, 0x10)

    rand = random.Random(*Context)
    key = crypto.create_key(rand, KeyTable, 0x10)
    aes = AES.new(key, AES.MODE_CBC, CryptoConfig[:0x10])
    Decrypted = aes.decrypt(Data)

    key = crypto.create_key(rand, KeyTable, 0x10)
    mac = CMAC.new(key, ciphermod=AES)
    mac.update(Decrypted)
    mac.verify(CryptoConfig[0x20:])

    return Buffer[:HeaderSize] + Decrypted


def EncryptCourse(Buffer):

    Header = Buffer[0:0x10]
    Decrypted = Buffer[0x10:]

    checksum = zlib.crc32(Decrypted) % (1 << 32)
    Header = bytearray(Header)
    Header[0x8:0xC] = checksum.to_bytes(4, "big")

    rand = Random.get_random_bytes(0x30)
    Context = struct.unpack_from("<IIII", rand, 0x10)
    rand = random.Random(*Context)
    key = crypto.create_key(rand, KeyTable, 0x10)
    iv = Random.get_random_bytes(0x10)
    RandomSeed = Random.get_random_bytes(0x10)
    aes = AES.new(key, AES.MODE_CBC, iv)
    Encrypted = aes.encrypt(Buffer)

    key = crypto.create_key(rand, KeyTable, 0x10)
    mac = CMAC.new(key, ciphermod=AES)
    mac.update(Encrypted)

    CryptoConfig = iv + RandomSeed + mac.digest()

    return Header + Encrypted + CryptoConfig


import struct
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Header:
    keep_name : bool
    suffix_len : int
    name_len : int = 0


    VERSION: ClassVar[int] = 0
    MAGIC: ClassVar[bytes] = "♥LILY".encode()
    FMT: ClassVar[str] = f">{len(MAGIC)}sxBHHx" # 14 bytes
    SIZE: ClassVar[int] = struct.calcsize(FMT)

    def pack(self):

        if self.VERSION > 127:
            raise ValueError("Version too large! max 127")
        flag_ver = (0x80 if self.keep_name else 0x00 ) | self.VERSION

        return struct.pack(self.FMT, self.MAGIC, flag_ver, self.suffix_len, self.name_len)

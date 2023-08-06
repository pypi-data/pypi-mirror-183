import hashlib


class Hasher:
    @staticmethod
    def read(hasher, file, blocksize=65536, blocks=16):
        blocks_read = 0
        buf = file.read(blocksize)
        while len(buf) > 0 and blocks_read < blocks:
            blocks_read = blocks_read + 1
            hasher.update(buf)
            buf = file.read(blocksize)

    @staticmethod
    def hashstring(files, blocks=16):
        hasher = hashlib.md5()
        for file in files:
            with open(file, "rb") as afile:
                Hasher.read(
                    hasher=hasher,
                    file=afile,
                    blocksize=65536,
                    blocks=blocks,
                )
        return str(hasher.hexdigest())

    @staticmethod
    def hashstring_one_file(file, blocks=16):
        return Hasher.hashstring(files=[file], blocks=blocks)

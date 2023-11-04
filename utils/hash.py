import hashlib


def md5(data: str | bytes, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.md5(data).hexdigest()
        if encoding == decoding:
            return hashlib.md5(data).hexdigest()
        return hashlib.md5(
            data.decode(decoding).encode(encoding)
        ).hexdigest()
    return hashlib.md5(data.encode(encoding)).hexdigest()


def sha256(data: str | bytes, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.sha256(data).hexdigest()
        if encoding == decoding:
            return hashlib.sha256(data).hexdigest()
        return hashlib.sha256(
            data.decode(decoding).encode(encoding)
        ).hexdigest()
    return hashlib.sha256(data.encode(encoding)).hexdigest()


def sha512(data: str | bytes, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.sha512(data).hexdigest()
        if encoding == decoding:
            return hashlib.sha512(data).hexdigest()
        return hashlib.sha512(
            data.decode(decoding).encode(encoding)
        ).hexdigest()
    return hashlib.sha512(data.encode(encoding)).hexdigest()


def sha384(data: str | bytes, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.sha384(data).hexdigest()
        if encoding == decoding:
            return hashlib.sha384(data).hexdigest()
        return hashlib.sha384(
            data.decode(decoding).encode(encoding)
        ).hexdigest()
    return hashlib.sha384(data.encode(encoding)).hexdigest()


def sha1(data: str | bytes, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.sha1(data).hexdigest()
        if encoding == decoding:
            return hashlib.sha1(data).hexdigest()
        return hashlib.sha1(
            data.decode(decoding).encode(encoding)
        ).hexdigest()
    return hashlib.sha1(data.encode(encoding)).hexdigest()


def sha224(data: str | bytes, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.sha224(data).hexdigest()
        if encoding == decoding:
            return hashlib.sha224(data).hexdigest()
        return hashlib.sha224(
            data.decode(decoding).encode(encoding)
        ).hexdigest()
    return hashlib.sha224(data.encode(encoding)).hexdigest()


def sha3_224(data: str | bytes, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.sha3_224(data).hexdigest()
        if encoding == decoding:
            return hashlib.sha3_224(data).hexdigest()
        return hashlib.sha3_224(
            data.decode(decoding).encode(encoding)
        ).hexdigest()
    return hashlib.sha3_224(data.encode(encoding)).hexdigest()


def sha3_256(data: str | bytes, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.sha3_256(data).hexdigest()
        if encoding == decoding:
            return hashlib.sha3_256(data).hexdigest()
        return hashlib.sha3_256(
            data.decode(decoding).encode(encoding)
        ).hexdigest()
    return hashlib.sha3_256(data.encode(encoding)).hexdigest()


def sha3_384(data: str | bytes, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.sha3_384(data).hexdigest()
        if encoding == decoding:
            return hashlib.sha3_384(data).hexdigest()
        return hashlib.sha3_384(
            data.decode(decoding).encode(encoding)
        ).hexdigest()
    return hashlib.sha3_384(data.encode(encoding)).hexdigest()


def sha3_512(data: str | bytes, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.sha3_512(data).hexdigest()
        if encoding == decoding:
            return hashlib.sha3_512(data).hexdigest()
        return hashlib.sha3_512(
            data.decode(decoding).encode(encoding)
        ).hexdigest()
    return hashlib.sha3_512(data.encode(encoding)).hexdigest()


def blake2b(data: str | bytes, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.blake2b(data).hexdigest()
        if encoding == decoding:
            return hashlib.blake2b(data).hexdigest()
        return hashlib.blake2b(
            data.decode(decoding).encode(encoding)
        ).hexdigest()
    return hashlib.blake2b(data.encode(encoding)).hexdigest()


def blake2s(data: str | bytes, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.blake2s(data).hexdigest()
        if encoding == decoding:
            return hashlib.blake2s(data).hexdigest()
        return hashlib.blake2s(
            data.decode(decoding).encode(encoding)
        ).hexdigest()
    return hashlib.blake2s(data.encode(encoding)).hexdigest()


def shake128(data: str | bytes, length: int, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.shake_128(data).hexdigest(length)
        if encoding == decoding:
            return hashlib.shake_128(data).hexdigest(length)
        return hashlib.shake_128(
            data.decode(decoding).encode(encoding)
        ).hexdigest(length)
    return hashlib.shake_128(data.encode(encoding)).hexdigest(length)


def shake256(data: str | bytes, length, *, encoding='utf-8', decoding=None) -> str:
    if isinstance(data, bytes):
        if decoding is None:
            return hashlib.shake_256(data).hexdigest(length)
        if encoding == decoding:
            return hashlib.shake_256(data).hexdigest(length)
        return hashlib.shake_256(
            data.decode(decoding).encode(encoding)
        ).hexdigest(length)
    return hashlib.shake_256(data.encode(encoding)).hexdigest(length)

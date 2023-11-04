from typing import Tuple

from . import hash


def md5(
    *datas: str | bytes,
    encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.md5(
            data,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def sha1(
    *datas: str | bytes,
    encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.sha1(
            data,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def sha224(
    *datas: str | bytes,
    encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.sha224(
            data,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def sha256(
    *datas: str | bytes,
    encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.sha256(
            data,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def sha384(
    *datas: str | bytes,
    encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.sha384(
            data,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def sha512(
    *datas: str | bytes,
    encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.sha512(
            data,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def sha3_224(
    *datas: str | bytes,
    encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.sha3_224(
            data,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def sha3_256(
    *datas: str | bytes,
    encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.sha3_256(
            data,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def sha3_384(
    *datas: str | bytes,
    encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.sha3_384(
            data,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def sha3_512(
    *datas: str | bytes,
    encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.sha3_512(
            data,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def blake2b(
    *datas: str | bytes,
    encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.blake2b(
            data,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def blake2s(
    *datas: str | bytes,
    encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.blake2s(
            data,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def shake128(
    *datas: str | bytes,
    length=32, encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.shake128(
            data, 
            length,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),


def shake256(
    *datas: str | bytes,
    length=32, encoding='utf-8',
    decoding=None
) -> Tuple[str]:

    return *(
        hash.shake256(
            data,
            length,
            encoding=encoding,
            decoding=decoding
        ) for data in datas
    ),



import hashlib


def sha256(data: str | bytes, *, encode='utf-8', decode='gbk'):
    if isinstance(data, bytes):
        return \
            hashlib.sha256(
                data.decode(decode).encode(encode)
            ).hexdigest()
    
    return \
        hashlib.sha256(data.encode(encode)).hexdigest()


def md5(data: str | bytes, *, encode='utf-8', decode='gbk'):
    if isinstance(data, bytes):
        return \
            hashlib.md5(
                data.decode(decode).encode(encode)
            ).hexdigest()
    
    return \
        hashlib.md5(data.encode(encode)).hexdigest()


def sha512(data: str | bytes, *, encode='utf-8', decode='gbk'):
    if isinstance(data, bytes):
        return \
            hashlib.sha512(
                data.decode(decode).encode(encode)
            ).hexdigest()
    
    return \
        hashlib.sha512(data.encode(encode)).hexdigest()


def sha384(data: str | bytes, *, encode='utf-8', decode='gbk'):
    if isinstance(data, bytes):
        return \
            hashlib.sha384(
                data.decode(decode).encode(encode)
            ).hexdigest()
    
    return \
        hashlib.sha384(data.encode(encode)).hexdigest()


def sha1(data: str | bytes, *, encode='utf-8', decode='gbk'):
    if isinstance(data, bytes):
        return \
            hashlib.sha1(
                data.decode(decode).encode(encode)
            ).hexdigest()
    
    return \
        hashlib.sha1(data.encode(encode)).hexdigest()


def sha224(data: str | bytes, *, encode='utf-8', decode='gbk'):
    if isinstance(data, bytes):
        return \
            hashlib.sha224(
                data.decode(decode).encode(encode)
            ).hexdigest()
    
    return \
        hashlib.sha224(data.encode(encode)).hexdigest()

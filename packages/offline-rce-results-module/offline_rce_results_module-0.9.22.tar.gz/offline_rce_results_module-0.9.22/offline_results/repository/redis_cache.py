import gzip
import hashlib
from typing import ByteString, AnyStr, Union, ClassVar

import redis


def hash_string(test: str) -> str:
    """Hash text as sha1 algorithm and return has string
    :param test: string plain text string
    :return:
    """
    return hashlib.sha1(test.encode("utf-8")).hexdigest()


class Redis:
    def __init__(self, uri: str):
        self._conn = redis.from_url(uri)

    @classmethod
    def from_uri(cls, uri: str) -> ClassVar:
        """Initialize connection based in specified uri
        :param uri: string uri
        :return: object class
        """
        return cls(uri)

    def set(
        self,
        key: str,
        value: Union[ByteString, AnyStr, int, float],
        ttl: int = 60 * 10,
        compression: bool = True,
    ) -> bool:
        """Store data into redis as bytes string, string, int or float data type
        :param key: string key
        :param ttl: integer value time to live, how much time do you want to store this variable inside cache,
            default is 10 minutes, unit in seconds
        :param value: it can be string, bytes string, int or float
        :param compression: compression method when inserting to cache default is true
        :return: bool true or false
        """
        if compression is True:
            return self._conn.set(key, gzip.compress(value.encode("utf-8")))

        if ttl == 0:
            return self._conn.set(key, value)

        return self._conn.set(key, value, ex=ttl)

    def get(
        self, key: str, with_hash: bool = True
    ) -> Union[ByteString, AnyStr, int, float, None]:
        """Get value from redis based on specified key
        :param key: string key
        :param with_hash: hash string when get value from cache
        :return: it can be string bytes string, int or float
        """
        v = self._conn.get(key)
        # if any value from it then decode to utf 8, cause default data type is bytes
        if v is not None and len(v) > 0:
            try:
                return v.decode("utf-8")
            except Exception as e:
                # if the object is bytetype only then return as it is without utf-8 encoding, as it will through error
                # it will help to store files in byte format in redis
                return v

        return None

    def get_data(self, key: str):
        return gzip.decompress(self._conn.get(key)).decode("utf-8")

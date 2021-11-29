# TODO - Add - Hadoop - The Definitive Guide Texts

Snappy - Snappy is one of the fastest compression techniques and most used in industries because it maintains a good balance of speed of compression and compression ration.But snappy is a non splittable compression technique and hence should be used with splittable file format Like Orc,parquet and avro.

LZO- LZO is also quite fast compression technique but not as much as snappy.It is a splittable compression technique and can be used with non splittable file formats like json and xml.

Gzip - Gzip provides 2.5X better compression then snappy but is also non splittable like snappy and hence should be used with splittable file formats like orc,parquet and avro.Because it provides good compression the overhead of compressing and uncompression also comes along with it.

Bzip2-Bzip2 is the best compeession technique and should be used only when you have to archieve files.

# How to call scala code from PySpark:

**Scala Code:**  

```scala
package com.example

object Hello {
  def hello = println("hello")
}
```

**Step to Invoke:**

create the jar containing scala code and place into spark's classpath.  
And then invoke the scala code from python like below:  
```python
>>> h = sc._jvm.com.example.Hello
```
In case of generic methods, like below:

```scala
object KafkaSource extends LazyLogging {

  def kafkaStream[K: ClassTag, V: ClassTag, KD <: Decoder[K] : ClassTag, VD <: Decoder[V] : ClassTag]
    (ssc: StreamingContext, brokers: String, offsetsStore: OffsetsStore, topic: String): InputDStream[(K, V)] {
    ...
```
we need to create a helper class and provide generic-free arugments, so that it can be callable from python or PySpark  
```scala
object KafkaSourcePythonHelper {

  def kafkaStream(jssc: JavaStreamingContext, brokers: String, offsetsStore: OffsetsStore,
                  topic: String): JavaDStream[(String, String)] = {
    val dstream = KafkaSource.kafkaStream[String, String, StringDecoder, StringDecoder](jssc.ssc, brokers, offsetsStore, topic)
    val jdstream = new JavaDStream(dstream)
    jdstream
  }
}
```
and then invoke it like this:

```python
>>> zkStore = sc._jvm.com.ippontech.kafka.stores.ZooKeeperOffsetsStore("localhost:2181", "/my_topic/offsets")
```

**Reference:**  
1. http://aseigneurin.github.io/2016/09/01/spark-calling-scala-code-from-pyspark.html


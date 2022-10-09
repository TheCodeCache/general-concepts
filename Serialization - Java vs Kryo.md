# Pros and Cons of `Java` Serialization vs `Kryo` serialization?  

Kryo is significantly faster and more compact than Java serialization (often as much as 10x),  
but does not support all Serializable types and requires you to register the classes  
you’ll use in the program in advance for best performance.  

So it is not used by default because:

1. Not every java.io.Serializable is supported out of the box -  
  if you have custom class that extends Serializable it still cannot be serialized with Kryo, unless registered.  
2. One needs to register custom classes.  

Spark automatically includes Kryo serializers for the many commonly-used core Scala classes  
that covered in the AllScalaRegistrar from the Twitter chill library.  

# Why Java Serialization is Slow - 

Reasons -  
- Java serialization is slow because it uses reflection
- crawls up the Class hierarchy for each Object doing several calls to read/writeObject per Object in case.
- Partially poor coding (improved with 1.7)
- Some often used classes make use of old slow + outdated serialization features such as putfield/getfield etc.
- Too much temporary Object allocation
- A lot of validation (versioning, implemented interfaces)
- Slow Java Input/Output streams
- Reflection to set/get field values.
- use of JDK collections requiring "big numbers" such as Integer or Long instead of primitives.
- implementation lacks certain algorithmic optimizations :-)
- primitives are reordered into network byte order (in java code, not native) on x86.


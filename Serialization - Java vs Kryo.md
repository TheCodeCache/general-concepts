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


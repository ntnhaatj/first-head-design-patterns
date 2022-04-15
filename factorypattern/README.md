# Factory Patterns

## Simple Factory
- just one implementation without subclassing to get the object creation method  

## Factory Method
- superclass contains `abstract factory method` to instantiate object. 
- other methods in superclass could use this interface to get the object instance without any knowledge about what is the kind of object instantiated.
- subclasses are able to implement which object should be created.

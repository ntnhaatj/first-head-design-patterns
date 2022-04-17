# Singleton pattern
- one-of-a-kind object, which always only has one instance in program
- use cases: threadpool, db connection, registry settings, device drivers,...

## Native singleton
- simple usage for single thread program
- cannot deal with multithread program, many object instances could be created

## Thread-safe singleton
- synchronize the object instantiation in multi thread program

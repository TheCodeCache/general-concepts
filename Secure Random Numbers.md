# ToDo
# Secure Random Numbers:

Standard JDK implementations of `java.util.Random` use a `Linear Congruential Generator` (`LCG`) algorithm for providing random numbers.  
The problem with this algorithm is that `it’s not cryptographically strong`.  
In other words, `the generated values are **much more predictable**`,  
therefore attackers could use it to compromise our system.  

To overcome this issue, we should use `java.security.SecureRandom` in any security decisions.  
It produces cryptographically strong random values by using a `cryptographically strong pseudo-random number generator` (`CSPRNG`).  

For a better understanding of the difference between `LCG` and `CSPRNG`,  
let us look at the below chart presenting a distribution of values for both algorithms:  

![image](https://user-images.githubusercontent.com/26399543/146452085-416c54a2-bf2e-4452-a2fc-7cf23f415a72.png)


# Hardware Random Number Generator:

**Reference:**  
1. https://stackoverflow.com/a/2450098/6842300
2. https://en.wikipedia.org/wiki/Hardware_random_number_generator
3. https://www.baeldung.com/java-secure-random

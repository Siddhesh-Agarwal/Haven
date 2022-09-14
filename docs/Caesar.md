# Caesar Cipher

## What is Caesar Cipher?

It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. 

The method is named after Julius Caesar.

## Encryption and Decryption Algorithms

The encryption can also be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A → 0, B → 1, ..., Z → 25. Encryption of a letter $x$ by a shift $n$ can be described mathematically as,

$$ E_{n}(x)=(x+n)\mod {26} $$

Decryption is performed similarly,

$$ D_{n}(x)=(x-n)\mod {26} $$

## Limitation of the Caesar cipher

The English language has 26 alphabets. Therefore, for a plaintext letter, there can be only 25 different possible cipher text letters. Obviously, we must not consider that cipher text letter which is identical to the plaintext letter. The Caesar cipher, therefore, is evidently quite limited in terms of the encryption capabilities that it can offer.

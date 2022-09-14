# Caesar Cipher

![Caesar Cipher](https://github.com/Siddhesh-Agarwal/Secure-Spark/blob/6d51c571923ddcbaa12a13ac6b404a74e0f9e7c0/docs/static/Caesar.png)

> In this article, we will learn about a simple substitution cipher, the Caesar cipher.
>
> The Caesar cipher, also known as a _shift cipher_, is credited to Julius Caesar, and thus the name "Caesar cipher".

## What is Caesar Cipher?

> The Caesar cipher is a simple encryption scheme that is used to obscure the meaning of a message by shifting each letter comprising the message a few places in the alphabet
>
> The Caesar cipher belongs to a subset of encryption schemes called substitution ciphers.

## Caesar cipher Key Generation Algorithm

> The key generation algorithm simply tells us how to choose the key for the Caesar cipher encryption scheme. The key in a Caesar cipher is simply the number of places each letter constituting the message should be moved.

## Caesar cipher Encryption Algorithm

>The Caesar cipher encryption algorithm encrypts/converts a plaintext message m into a cipher text message c.
>
> In order to encrypt a plaintext message m using the Caesar cipher, each letter constituting the plaintext message m must be moved the same number of places, as determined by the key.
>
> The Caesar cipher encryption algorithm lays down the set of instructions to help achieve the plaintext message encryption process to produce a cipher text message.

## Caesar cipher Decryption Algorithm

> So, by now, we have the Caesar cipher key generation and encryption algorithms and therefore, the only thing that is missing is the Caesar cipher decryption algorithm. The decryption algorithm will take the cipher text message c and decrypt/convert that back into the plaintext message m. The decryption algorithm simply undoes the operations performed by the encryption algorithm.

## Fun Fact

> In the 20th century, the Caesar cipher was used many a times by lovers in order to send romantic messages in the public section of The Times newspaper. Now, that's what I call "Cryptic ROMANCE"!!!

## Limitation of the Caesar cipher

> The English language has 26 alphabets. Therefore, for a plaintext letter, there can be only 25 different possible cipher text letters. Obviously, we must not consider that cipher text letter which is identical to the plaintext letter. The Caesar cipher, therefore, is evidently quite limited in terms of the encryption capabilities that it can offer.

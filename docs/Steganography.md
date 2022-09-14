# Steganography

## What is Steganography?

Steganography is the a process of embedding a secret piece of text within a text, picture, or audio. The message could be a message or script within a document file or a picture file. A form of covert communication, the main purpose of steganography is concealing and deceiving.

## How does it work?

The working of Steganography is quite simple. It works by replacing some parts of useless or unused data in usual computer files with bits of invisible and different information.

## Types of Steganography

### Steganography in Images

Digital images are used widely and since they are available in various formats the algorithm used differs completely. Some common kinds are:

- Least significant bit insertion.
- Masking and filtering.
- Redundant Pattern Encoding.
- Encrypt and Scatter.
- Algorithms and transformations.
- Least significant bit insertion.

### Steganography in Audio

Implanting a secret message in audio is most difficult as the human brain has a wide range of auditory capacity. A few methods used are:

- LSB coding.
- Parity coding.
- Phase coding.
- Spread spectrum.
- Echo hiding.

### Steganography in Video

In this, a video file will be embedded with supplementary data that will hide the secret message. Some widely known approaches are

- Least Significant Bit Insertion.
- Real-time Video Steganography.

### Steganography in Documents

This involves focusing on altering the characteristics of documents. Most people can read documents and therefore there are several ways in which this can be achieved. A few ways this is done are:

- Hiding information in plain text by adding white space and tabs to the end of the lines of documents.
- The use of background color and font is another widely used technique for steganography. It is widely used in Microsoft Word documents.

## Techniques

Steganography techniques used help in concealing the message to the best possible extent to ensure that it is revealed only at the destination. Some of the techniques used are:

**Least Significant bit**: The attacker identifies the least significant bits of information in the carrier file and substitutes it with the secret message, in most cases, malicious code.

**Palette Based Technique**: This uses digital images as malware carriers where attackers first encrypt the message, hide it in a wide palette of the cover image.

**Secure Cover Selection**: A very complex technique, cyber criminals have to compare blocks of the carrier image to specific blocks of specific malware. It involves finding the right match to carry the malware.

## Examples

Steganography is more an art than a science. It involves using careful techniques to hide the message and execute it. There is no limit to the ways steganography can be used with such a wide range of technology available today. A few examples are:

- Playing a video at a faster frame rate to unveil a hidden message.
- Inserting a message in the red, green, or blue channel of an RGB image.
- Playing an audio track backward to reveal a hidden message.
- Encrypting a message or image within a photo through the addition of noise or sound.
- Hiding information with the file header or metadata.

## Steganography in Secure Spark

Generally, there is no encryption in Steganography but in Secure Spark we're going to use **2-way asymmetric encryption** to encrypt the plain text. Thereby ensuring in the case of third-party interception there is no compromise in security

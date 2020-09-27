# Decipher an encrypted text


## Problem description

Someone has used a simple substitution cipher to encrypt an extract from Conan Doyle's [A Scandal in Bohemia](https://www.gutenberg.org/files/1661/1661-h/1661-h.htm#chap01). Your task is to find the key they used to encrypt it.  

## Specifications
The key will be random. The key will work the same for uppercase and lowercase but punctuation and spaces will be left alone. The extract will be large (c.85% of the whole text). Input is the encrypted extract as a string (which you can see with print(extract)), output is the key as a string.

### Simple subsitution cipher
[Simple subsituation cipher](https://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution) is a type of substitution cipher that uses a key of 26 characters that maps to the alphabet.  

For example the quarty keyboard map **`qwertyuiopasdfghjklzxcvbnm`**, which can map to the alphabet as follows:

```
alphabet: |a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|
key1:     |q|w|e|r|t|y|u|i|o|p|a|s|d|f|g|h|j|k|l|z|x|c|v|b|n|m|
```

There are a set of brackets and an ampersand in the original text. They have been changed to commas and the word 'and' respectively to makes thing a little harder

## Access the data

In order to access the data, the The book is preloaded. It may be accessed as

```python
from preloaded import a_scandal_in_bohemia
```


## Solution

In order to avoid the complexity caused by the brackets, we will try to find sensences that don't have comma.  

To avoid the complexity caused by the ampersand, let us find a sentence in the encoded text, and find another sentence in the original text which matches exactly the number of characters and the number of letters in each word.  

For example, if we find in the original text this sentence:

```
Zg Litksgea Igsdtl lit ol qsvqnl zit vgdqf.
```

Then we search in the original text a sentence (which end with period), that match the exact pattern in number of words and length of each word.  

We find this:  

```
To Sherlock Holmes she is always the woman.
```

The longer the sentence, the more accurate our method is to find the correct original sentence.  


# RSA Encryption
## The Process
RSA Encryption requires two (really large) prime numbers to generate a public key: $`n  = pq`$. Values $`p and q`$ are kept secret and are used to find $`λ(n) = lcm(p-1, q-1)`$. Once you have $`λ(n)`$ you can pick a number $`e`$ that is co-prime to $`λ(n)`$ and that is $`1 < e < λ(n)`$. To be co-prime the $`gcd(e, λ(n)) = 1`$. Value $`e`$ should be relatively large also, but for the sake of my computer I hardcoded "3" because it is the smallest and fastest number to use.
After this easy stuff, now comes the challenge of finding $`d`$. At least, it was challenging for me. I had to do some more research and look back at some old school notes. Basically $`d \equiv e^{-1}\modλ(n)`$. Now the math I had to dig up was about the [extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm). The code I used doesn't feel like the most efficient. 

```python
def mod_multi_inverse(e, lambda_n):
    for d in range(3, lambda_n):
        if (d * e) % lambda_n == 1:
            return d
        else:
            continue
```
Especially if you're using huge numbers. But there's a number of reasons why it slows down around 8 bit numbers. I don't have the processing power to generate and compute the "recommended" 2,048 to 4,096 bit key sizes.
At the end of all this the public keys are just $`n`$ and $`e`$. The private numbers are $`λ(n), p, q,`$ and, the private key, $`d`$. The private key is shared between the sender and receiver.
## The Text Files
I wanted to add here about why I have an encryption file and a decryption file. Apart from reading the code, I wanted the visitor of this repository (yes, you) to see that I'm not just copying the Unicode message back into the same file. I wanted a clear distinction that I'm getting back to the Unicode from the encrypted Unicode. I guess I could've done this anyway in a seperate file, but to me the code shows a clear distinction that it's not copied from the original message.

# The Math
## Encryption
After you have all your numbers, encryption and decryption are pretty easy. You have a message $`m`$ that you want to encrypt. So you raise $`m`$ to the power of $`e`$ and modulate that by $`n`$. Such that: $`c = m^e\mod n`$. Now I took the users input and took each characters' Unicode to encrypt those numbers, but I'm sure there's a way to encode a specific file. That will be in part 2: Electric Boogaloo. 

## Decryption
To decrypt the Unicode numbers, the receiver will take the private key $`d`$ and use it as an exponent on $`c`$. Quite beautifully this results to $`m = c^d\mod n`$ allowing you to turn the Unicode back into letters to read the message.

# Sources
If you'd like to read more, I'd recommend the [Wiki](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) page. And also [this video](https://www.youtube.com/watch?v=qph77bTKJTM&pp=ygUOcnNhIGVuY3J5cHRpb24%3D) on a more in depth explanation behind the math.

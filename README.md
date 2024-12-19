# SOLFLARE CONVERT

This is a Python script to convert a list of integers into a Base58 encoded string. The script reads a list of integers from the user, converts it into a byte array, and then encodes the byte array into a Base58 string using the specified alphabet. The resulting Base58 encoded string is then printed to the console.

The code uses the following Base58 alphabet:  
`123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz`.  

It defines a function `base58_encode(data: bytes)` that takes a byte array as input and returns the Base58 encoded string.

This script supports exporting data from Solflare to Phantom Wallet or other wallets.

---

## How to Use?

1. Input your list of integers.

   Example input to the prompt:
   ```plaintext
   214,161,14,138,217,210,95,163,37,183,121,218,162,69,217,209,39,115,61,187,143,43,206,42,34,30,234,160,35,54,106,53,156,61,97,93,55,113,131,185,112,193,111,116,23,30,116,54,249,87,121,131,193,9,145,1,253,42,63,16,206,118,120,247
2. The script processes the input and outputs the result.

    Example result:
   ```plaintext
   5HtLjQi436eZE9BWWzFts5WRd5uTFfWpLEgpoz49eot92nVJehtxZye5V7BUpbFzmsZvsSxJhDTzAtVpFZzz9S14!



![image](https://github.com/user-attachments/assets/cd52ef2e-5a7f-4912-a2e1-ae6c9291f5eb)

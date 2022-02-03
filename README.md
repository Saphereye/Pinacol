# Pinacol
Python program for encryptIoN And COmpression of fiLes

Currently works only for textual files(Image compression in progress)

## How it works
  1) Breaks down the text and detects the frequency of words  
  2) Out of a unique 'key' list, each word, starting from the highest frequency is given the corresponding element of the 'key' list(eg : first is given 'A', then 'B', then after they are done we give 'AA' then 'AB' and so on)  
  3) First word is replaced by empty string for efficiency  
  4) Then an encrypted sentence and a 'secret' list(containing the order by frequency) are released.  
  5) If single character encrypted word are together, we do not use a separator, but for multiple character we do use  

## Example working
 Lets say you wish to encrypt the sentence : 'never gonna give you up never gonna let you down'  
 and our key list is [0,1](Can be anything until it's a list of unique elements)  
 
 Then on ordering by frequency : 
 ```
never:2
gonna:2
give:1
you:2   
up:1   
let:1   
down:1
```
 Then on exchanging the values with new values;  
 ```
never:<blank>   
gonna:0  
you:1  
give:00  
up:11  
let:10  
down:001  		    
```
Then we will create two files,  
	1) One our encrypted file, outputFile.das -> ```.000.111..010.1001.``` ('.' is separator, you can use anything else)  
	2) Second a secret file, secret.das -> ```never gonna you give up let down``` 

## Thoughts 
Pinacol acts like a wonderful compression algorithm for large files with lot of patterns  

Example an average book has about 10,000 words out of which 1000 are unique and an average length of words is 5 which   
my algorithm(witha big enough key) can compress down to 2 letters(maximum)  

Thus ```~50,000 letters + ~1000 whitespaces = ~51,000 bytes  ```
is compressed down to ```~2000 letters + ~1000 separators = ~3000 bytes ```i.e. 6% of original  

## Room for improvement
Instead of single words the program should take group of patterns as it's elements  
eg in the sentence 'never gonna give you up never gonna let you down'  

we can take  
 ```
never gonna:2   
give:1  
you:2   
up:1   
let:1   
down:1  
```
which gives =>   
 ```
never gonna:<blank>   
give:0  
you:1   
up:00   
let:01   
down:10  
```  
finally the code being => ```.0100..01.110.```

## Some results of experimentation
1)
On using the paragraph
```
In signal processing, data compression, source coding, or bit-rate reduction is the process of encoding information using fewer bits than the original representation. Any particular compression is either lossy or lossless. Lossless compression reduces bits by identifying and eliminating statistical redundancy. No information is lost in lossless compression. Lossy compression reduces bits by removing unnecessary or less important information. Typically, a device that performs data compression is referred to as an encoder, and one that performs the reversal of the process (decompression) as a decoder.

The process of reducing the size of a data file is often referred to as data compression. In the context of data transmission, it is called source coding; encoding done at the source of the data before it is stored or transmitted. Source coding should not be confused with channel coding, for error detection and correction or line coding, the means for mapping data onto a signal.

Compression is useful because it reduces the resources required to store and transmit data. Computational resources are consumed in the compression and decompression processes. Data compression is subject to a space–time complexity trade-off. For instance, a compression scheme for video may require expensive hardware for the video to be decompressed fast enough to be viewed as it is being decompressed, and the option to decompress the video in full before watching it may be inconvenient or require additional storage. The design of data compression schemes involves trade-offs among various factors, including the degree of compression, the amount of distortion introduced (when using lossy data compression), and the computational resources required to compress and decompress the data.
```

The program gives 
```
Compression Ratio = 1.1391193363114231 (input length / output length)
Compression Percent = 21.288515406162464 (output length / input length *  100)
```

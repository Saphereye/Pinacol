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

Of course, this is based on the assumption that there would be so much repetition, which is perhaps not the case in real life.

In the case of encryption:
1) If you don't have the 'secret', it's is impossible to find out what words were used
2) In the case you have both the encoded and secret file, without applying language logic, it would be ```n!``` combinations of the key list
3) But this can be solved by simply taking into account frequency of symbols in encrypted string and mathcing it with the 'secret' string, unless it is also shuffled which would make it snother ```n!``` cased for the secret.
	

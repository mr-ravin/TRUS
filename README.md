# TRUS: Triple Relation Using Syntaxnet

### TRUS is designed with the aim of providing triple relations. It is written in Python 2.7 ans is used over syntaxnet to retrieve the triple relations. 

#### Author: [Ravin Kumar](https://mr-ravin.github.io)

## Working Demonstration

[![Working Demonstration](https://github.com/mr-ravin/TRUS/blob/master/TRUS.gif)](https://github.com/mr-ravin/TRUS/blob/master/TRUS.gif)
### Installation Steps:-

1. Install python 2.7

2. Install Syntaxnet.

For the details of installing above packages refer to it's github ![repository](https://github.com/tensorflow/models/tree/master/research/syntaxnet)

3. Download TRUS and place "TRUS.py" inside the "/model/syntaxnet/" directory of Syntaxnet.

4. To use TRUS, type this in the terminal:

```   
 > python2 TRUS.pyc
```

### Example:

```
> python2 TRUS.pyc
``` 

      Developed by: Mr.Ravin Kumar.  Email id: mr.ravin_kumar@hotmail.com
      Linkedin: https://www.linkedin.com/in/ravinkumar21 
      enter sentence:
      cat sat on a mat

      
### Output:

 ```
       ['cat','sat','mat',1]
 ```      
       
The last value here, i.e. 1 is of no use for now, but since this software is under development, It is left for prioritization. 
Right now, you will receive all relations of same priority (here priority means, Possibility that information is complete).
Otherwise, If I had removed ( Which I have not ) that condition from the software, you may receive other relations like:
['cat','' ,'',0 ] ......... ['cat ','','mat',0] ...etc too. 

```python
Copyright (c) 2017 Ravin Kumar
Website: https://mr-ravin.github.io

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

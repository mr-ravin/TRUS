# TRUS

It contains a program written in python 2.7 , which provides triple relations from the sentences.

# TRUS: Triple Relation Using Syntaxnet

Developer: Mr.Ravin Kumar

[Email id: mr.ravin_kumar@hotmail.com](mr.ravin_kumar@hotmail.com)

[Linkedin: https://www.linkedin.com/in/ravinkumar21/](https://www.linkedin.com/in/ravinkumar21/)


### TRUS is designed with the aim of providing triple relations. It is used over syntaxnet to retrieve the triple relations. 

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

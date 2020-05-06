# Basics

## Task: basic pattern  

You have a test string .
Your task is to write a regular expression that matches only and exactly strings of form: `abc.def.ghi.klm`, where each variable `a,b,c..m` can be any single character except the newline.

### Solution:

The dot (.) matches anything (except for a newline).  
To match exactly the (.) we have to escape it using (\), and to repeat it n times we use {n}.


```js
let inputString = '123.456.abc.def';
const match = inputString.match(/^(.{3}\.){3}.{3}$/g);
cosole.log(match);
```

```python
regex_pattern = r"^(.{3}\.){3}.{3}$"
test_string = '123.456.abc.def'
import re
match = re.match(regex_pattern, test_string) is not None

print(str(match))
```

## Task: white space

You have a test string. 
Your task is to match the pattern XXsXXsXX.

Here, s denotes whitespace characters, and X denotes non-white space characters.

### Solution: 

To match whitespace character use: `\s` which include: ` [ \r\n\t\f ] `.  
And `\S` is non-white space character.

```js
let inputString = '12 11 15';
const match = inputString.match(/^(\S{2}\s){2}\S{2}$/g);
cosole.log(match);
```

```python
regex_pattern = r"(\S{2}\s){2}\S{2}$"	
test_string = '12 11 15'
import re
match = re.match(regex_pattern, test_string) is not None

print(str(match))
```

## Task: email address:

Your task is to match email address.

### solution:

The character `\w` match any word character, which means any alphabetic a-z or A-Z and any number 0-9 and underscore `_`. To add the `(.)` to it, we add character class `[]`, which include any character in it. Note that the `(.)` doesn't need an escape inside the character class.  
The email domains in the first example are restricted to: com, net and org.  
Because we are adding those groups to choose only one and not capturing the group so we escape the group by `?:`.

```python
regex_pattern = r"\b[\w.]+@\w+\.(?:com|net|org)\b"
```
to have it more general

```python
exp = r'\b[\w.]+@\w+(?:\.[a-zA-Z]{2,})*\b'
```

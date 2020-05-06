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

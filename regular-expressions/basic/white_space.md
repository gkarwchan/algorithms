## Task: white space

You have a test string. 
Your task is to match the pattern XXsXXsXX.

Here, s denotes whitespace characters, and X denotes non-white space characters.

### Solution: 

To match whitespace character use: `\s` which include: ` [ \r\n\t\f ] `.  
And `\S` is non-white space character.

```js
// javascript
let inputString = '12 11 15';
const match = inputString.match(/^(\S{2}\s){2}\S{2}$/g);
cosole.log(match);
```

```python
# python
regex_pattern = r"(\S{2}\s){2}\S{2}$"	
test_string = '12 11 15'
import re
match = re.match(regex_pattern, test_string) is not None

print(str(match))
```

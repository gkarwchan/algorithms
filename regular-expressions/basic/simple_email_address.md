
## Task: match simple email address:

Your task is to match email address.

### solution:

The character `\w` match any word character, which means any alphabetic a-z or A-Z and any number 0-9 and underscore `_`. To add the `(.)` to it, we add character class `[]`, which include any character in it. Note that the `(.)` doesn't need an escape inside the character class.  
The email domains in the first example are restricted to: com, net and org.  
Because we are adding those groups to choose only one and not capturing the group so we escape the group by `?:`.

```python
# python
regex_pattern = r"\b[\w.]+@\w+\.(?:com|net|org)\b"
```
to have it more general

```python
# python
exp = r'\b[\w.]+@\w+(?:\.[a-zA-Z]{2,})*\b'
```

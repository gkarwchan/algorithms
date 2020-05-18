## Task : Get the initials of a name

```js
//javascript
Regex initials = new Regex(@"(\b[a-zA-Z])[a-zA-Z]* ?");
string init = initials.Replace(nameString, "$1");
print (init)
```
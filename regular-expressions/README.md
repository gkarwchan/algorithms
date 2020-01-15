# Regular Expressions:

Regular Expressions are very powerful, and can be very complicated.  
Here you will find a list of very helpful tips.

## Features:

### Grouping:
By placing part of a regular expression inside round brackets or parentheses, you can group that part of the regular expression together.  
There are two benefits for this:  

1. Deal with the entire group as one entity, so you can apply **`quantifier`** or **`alteration`**.
2. Using text matched by the capturing group with a process called `backreference`.

Examples of first case:

```js
Set(Value)? 
```

Matches either:  

1. "Set".
2. "SetValue".

For the second case, we are going to cover it in more details in section called `backreference`.


#### Backreference:

Example of checking if a string has duplicate characters (Isogram):

```js
function isIsogram(str){ 
  return !/(\w).*\1/i.test(str)
}
```
# CheatSheet Organized Structure

1. **Concept Name**: Briefly write the name of the tool and its main purpose.
2. **Syntax**: The basic and abstract format for writing the code.
3. **Practical Example**: A very short and direct code snippet demonstrating how the concept works.
**How To Write The Code**

```python
# write your code here
```

**This is cheatsheet for Regular Expressions of Python**: <https://www.debuggex.com/cheatsheet/regex/python>
**Use This WebSite to Test Your Regex Special Characters**: <https://pythex.org/>
**Use This WebSite if You Want to Understand your RegEx Code, cuz it will explain each charater for you**: <https://regex101.com/>

you can use normal character followed by regex, for example you can use "A" and "\w" to get the followed charater
Example: Esam => E\w => Result: Es
and you can write more regex as you want but on condition the thing you are searching for is no more than your regex
Example "ABCDE": if i want to search for "A" as a character and any charaters behind it, i write A\w\w\w => Result: ABCD, and you can reverse
\w\w\wD Result: ABCD

## RegEx Quantifiers

quantifiers is that instead of writing \w\w to get 2 charaters you can use \w{2} like slicing in normal python code
Example "ABCD": \w\w => Result: AB, \w{2} => Result: AB
and you can change the number between the {} as you want
**Read The Quantifiers CheatSheet For More Info**

lets imagine that you have a set of data and you want to extract only the phone number
\\
015 596 00-6-71
esam haraz
hello
123456789
\\
to extract the phone number you will need to write: \d{3}\s\d{3}\s\d{2}-\d-\d{2} => Result: 015 596 00-6-71

### Regex Characters Classes

you can use [] to select range of charaters
Example "my name is esam": [a-m] => Result: m ame i e am
Explain: It Starts from A and End at M
and if you want to stack them, you just stick them together in the same [] => [a-mA-M0-9] and so on
and you can revers it by adding ^ inside the []
Example "my name is esam": [^a-m] => Result: y  n  s  s

you can use ? charater to check if the regex is there or not
for example: you have (012 345 67-89) and (012 345 67 89)
first numbers has - and second has space but i want to get the two numbers
to do that you write: \d{3}\s\d{3}\s\d{2}-?\s?\d{2}
this way your regex code will get the two numbers example, its like "if - there get it, if not ignore, and same goes to whitespace"

#### Regex Assertions

you can choose to make your code start or end your regex code with your code
for example i have two number (012 345 67-89) and (=>012 345 67-89) and i want to select the number without =>
you can't do that by just place your regex code cuz it will select the two numbers, to just choose one:
to start you use ^ before your regex code **^\d{3}\s\d{3}\s\d{2}-?\s?\d{2}** and in this case it will choose (012 345 67-89) and not the another one
to end you use $ **$\d{3}\s\d{3}\s\d{2}-?\s?\d{2}** and it will choose (=>012 345 67-89)

^ asserts that the string must start with this exact pattern. Similarly, $ asserts that the string must end with this exact pattern. They are used to ensure the position of the match, not to exclude characters.

now you have some emails and you want to valid them
<esam.haraz@haraz.com>
<esam.fahmy@gmail.com>
<ahmedibrahim125@hotmail.net>
<mohamed74_ali@mail.ru>
regex code will be: [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
and if you want only "com" emails only you can do that by: [A-z0-9\.]+@[A-z0-9]+\.(com)
more than "com" you seperte them by |: [A-z0-9\.]+@[A-z0-9]+\.(com|net)

##### Regex Logical Or And Escaping

you can put your regex code in group using (regex code)
Example: (\d-)(\w+)
and you can use Quantifiers on the whole group

you can use | to use it like "or"
Example: you have 2 groups of items
1- HTML
2- CSS
3) Python
4) Java
and you want to choose all of them but they have different start
you can choose all of them by using | in your regex code
\d-|\d\)\s\w+
this code will get all of them
Note: we used backslash with ) to escape it

###### Regex Re Module Search And FindAll

search(Pattern, String) => search a string for a match and return a first match only
findall(Pattern, String) => returns a list of all matches and empty list if no match

re.search() function never returns more than one single match. When you add a quantifier like {2} to your pattern, you are not instructing it to find more matches; you are instructing it to find the very first occurrence of exactly two consecutive characters. If your goal is to extract all possible matches from the entire text, you must use the re.findall() function.

```python
import re # to import Regex Module

my_string = re.search(r"[A-Z]", "EsamHaraz")
print(my_string)
```

note: "r" before regex code to make python understand its a raw string

print(my_string) will return something called span which will tell you the postion of the match that it found
and match will tell you the object that it match with your regex code
you can only call span my "print(my_string.span())"

you can edit the quantifier of "search()" command to make it get more matches by

```python
my_string = re.search(r"[A-Z]{2}", "EsamHaraz")
```

###### Regex Re Module Split And Sub

split(Pattern, String, MaxSplit) => Return a list of Elements Splitted On Each Match
sub(Pattern, String, ReplaceCount) => Replace Matches With What You Want

```python
import re
string_one = "Love Python"
search_one = re.split(r"\s", string_one)
print(search_one)
# output => ["Love", "Python"]
string_two = "I Love Python Programming"
search_two = re.split(r"\s", string_two, 2)
print(search_two)
# output => ["I", "Love", "Python Programming"]
```

###### Last Video is important and its summary all the other videoes

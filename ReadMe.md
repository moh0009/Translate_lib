# Translate library
### it's so simple to start
```python
from Translate import Translate
output = Translate(text = "hi", fromlang = "en", tolang = "it")
print(output.GetTranslatedText())
```

### the output well be `Ciao`
### want see all the response

```python
from Translate import Translate
output = Translate(text = "hi", fromlang = "en", tolang = "it")
print(output.GetAll())
```
### do want just matches you can
```python
from Translate import Translate
output = Translate(text = "hi", fromlang = "en", tolang = "it")
print(output.GetMatches())
```
### do you want in more formated way
```python
from Translate import Translate
output = Translate(text = "hi", fromlang = "en", tolang = "it")
print(output.GetFormatedMatches())
```
### want see languages
```python
from Translate import Translate

print(Translate.GetLanguages())
```
### just simple as this

#### note: you have up to 5000 chars/day as referenced [here](https://mymemory.translated.net/doc/usagelimits.php)

#### note: if you want quality check [this library](https://github.com/ssut/py-googletrans) 

## thanks to [mymemory](https://mymemory.translated.net/) for the api 
## thanks to [googletrans](https://github.com/ssut/py-googletrans) for language list that i used in `Translate.GetLanguages()`

#### License
```
MIT License

Copyright (c) 2024 moh0009

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
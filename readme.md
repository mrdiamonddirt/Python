# Readme

<img src='https://www.python.org/static/img/python-logo.png' width='50%'>

## Description

a couple of python scripts to get information from urls written in a file,
written by me Rowan Wood (RowDog) for the purpose of learning python
[Github Repo](https://github.com/mrdiamonddirt)
some of the files require the use of additional python modules, there are instructions on how to install them in the files for each script in a comment at the top of the file.
**_note:_** _these scripts are not intended for use in production, they are for learning purposes only_

<hr/>

## Usage

### run.py

a really simple cli menu to run the other scripts
<br/>

`py run.py`
<br/>
<br/>
<img src='./images/menu.png' width='200px'>

type the number of the script you want to run and press enter

### 1. getpagetopdf.py

set the url in the script and run
<br/>
`py getpagetopdf.py`
<br/>
returns a pdf of the url and saves to a .pdf file in the same directory as the script

### 2. getpokemon.py

just run the script
<br/>
`py getpokemon.py`
<br/>
requests a pokemon number off the user and returns the name and image of the pokemon

### 3. lookforform.py

`py lookforform.py`
<br/>
returns a list of all the forms on a url

### 4. postcodecrime.py

`py postcodecrime.py`
<br/>
requests a postcode and a date from the user and returns the crimes details and location for that date
saves to a json file in the crimes folder in the same directory as the script

### 5. saveallimages.py

set the url in the script and run
<br/>
`py saveallimages.py`
<br/>
returns all images from a url and saves to a the images folder in the same directory as the script

### 6. savemapofpostcode.py

`py savemapofpostcode.py`
<br/>
requests a postcode from the user and returns a map of the postcode and saves to a .html file in a folder called map in the same directory as the script,
and opens the map in the default browser,
can also plot crime data on the map if the streetlevelcrime.py script is run first to generate the crimedata json file

### 7. scarpehtml.py

set the url in the script and run
<br/>
`py scrapehtml.py`
<br/>
returns html from a url and saves to a .html file
in the same directory as the script

### 8. streetlevelcrime.py

`py streetlevelcrime.py`
<br/>
requests a postcode from the user and returns a json file of all the crimes in that postcode with an optional date and saves to a folder called crimes in the same directory as the script

---

## contributing

if you want to contribute to this project, please fork the repo and make a pull request, i will review it and if it is good i will merge it into the main branch and give you credit for your contribution in the readme file and in the script itself

---

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

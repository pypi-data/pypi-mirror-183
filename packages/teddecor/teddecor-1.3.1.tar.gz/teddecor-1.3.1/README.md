# TEDDecor
This is a easy to use library with testing, a custom inline markup language, pretty exceptions, and diagramming. Dive in with minimal effort and get great results. 

> NOTE: This library only uses builtin python and only requires python v3.7 or higher

- [TEDDecor](#teddecor)
  - [TED](#ted)
    - [Markup Parsing](#markup-parsing)
    - [Color Function](#color-function)
  - [Decorators](#decorators)
    - [Config](#config)
    - [Deprecated](#deprecated)
    - [Not Implemented](#not-implemented)
    - [Debug](#debug)

___

## TED

### Markup Parsing

TED is the name for the inline markup language for this library. This allows the user to customize strings and prettyprint different information to stdout.

Includes:

* parse -> returns formatted strings
* pprint -> parse TED markup strings and display them to stdout
* More to come...

Syntax:

Brackets `[]` indicate a macro. Macros can do 1 of three things; Assign a foreground/background color,
create a hyperlink, and call a builtin function. All macros will ignore extra whitespace and focus on the identifiers; `@`, `~`, and `^`.

1. Colors
    * Colors start with a leading identifier `@`. To indicate foreground or background use the specifier `F` and `B` respectively.
    Following the `@` and the specifier you can then enter the color. 
        * This can be a predifined color such as; black, red, green, yellow, blue, magenta, cyan, white. `[@F black]`.
        * It can be a hex code `#ead1a8`. `[@F #ead1a8]`.
        * It can be a XTerm code 0-256. `[@F 9]`.
        * Lastely, it can be an rgb color where the 3 numbers can be seperated by a `,` or a `;`. `[@F 114;12,212]`.
    * Colors can be reset with `[@F]` or `[@B]` to reset foreground or background respectively or `[@]` can be use to reset both.
    * Foreground and background can be specified in the same macro `[@F 1 @B 2]`, but they can not be reset in the same macro `[@F @B]`, 
    * When wanting to change foreground and background to the same value or reset them at the same time, use the `[@]` shorthand.
    * While the macro will ignore white space and you can do something like `[@F#005f00@B7]` it is preferred to use whitespace for readability `[@F #005f00 @B 7]`.
  
<p align="center">
  <img src="https://raw.githubusercontent.com/Tired-Fox/TEDDecor/main/images/TED_example_0.png" alt="Example Test Results">
</p>


2. Hyperlinks
    * Hyperlinks start with a leading identifier `~`.
    * Hyperlinks will surround plain text blocks. `[~https://example.com]Example` -> ``Example``.
        *   Links end on the next macro with the simpl `~` or at the end of the string
            * `[~https://example.com]Example[~] Not part of the link`
            * `[~https://example.com]Link1 [~https://example.com]Link2`
<p align="center">
  <img src="https://raw.githubusercontent.com/Tired-Fox/TEDDecor/main/images/TED_example_1.png" alt="Example Test Results">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/Tired-Fox/TEDDecor/main/images/TED_example_2.png" alt="Example Test Results">
</p>


3. Builtin functions
    * Builtin functions start with the identifier `^`. The text block following the function will have it's string value passed as a parameter.
    * You can also specify your own function or override the provided ones by calling TED.define("Macro Name", Callable)
    * The custom function needs to take a string and return a string. If it does not return a string it will not have an affect.
        * Example:
            ```python
            def hello_world(string: str) → str:
                return "Hello World"
            
            TED.define("hw", hello_world)
            TED.print("[^hw]Cat goes moo")
            ```
        * The above example lets TED know about the function hello_world and says it can be called with `hw`
        * Then all that needs to happen is to call it with `[^hw]`
    * Example:
        * `[^rainbow]Rainbow Text` will return the string with a rainbow foreground color.

<p align="center">
  <img src="https://raw.githubusercontent.com/Tired-Fox/TEDDecor/main/images/TED_example_3.png" alt="Example Test Results">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/Tired-Fox/TEDDecor/main/images/TED_example_4.png" alt="Example Test Results">
</p>
TED also follows some inspiration from markdown where `*` means toggle bold and `_` means to toggle underline.
To reset all attributes, color and formatting, use the empty brackets `[]`.

<p align="center">
  <img src="https://raw.githubusercontent.com/Tired-Fox/TEDDecor/main/images/TED_example_6.png" alt="Example Test Results">
</p>

<p align="center" style="bold">
  See <a href="https://raw.githubusercontent.com/Tired-Fox/TEDDecor/main/images/TED/basics.py" title="Docs" target="_blank">examples/TED/basics.py</a> to see how TED could be used along with seeing the outputs.
<p>

### Color Function

The color function works similar to how the markup works. However, instead of markup inside the string, you pass in properties. 

The first parameter is the string you would like to style, while the rest of the parameters are keyword arguments changing the style. You may use the `foreground`, `background`, `bold`, `reversed`, `underline`, and `url` arguments to style the text.

The colors are set with either a `str`, `int`, or `tuple`. This represents hex code, xterm code, or rgb respectively. If you want other color formats you may used the `Color` class. This gives you access to hex, rgb, hsl, hsv, yiq, and xterm colors, along with a way of convert to rgb and from rgb to any of the other formats.

___

## Decorators

### Config
### Deprecated
### Not Implemented
### Debug
# range

## tldr;

    -📦 ranged is a library for generating sequences of numbers
    -🚀 aims to be a more feature-rich version of the built-in range function
    -💪 performant and dependency-free
    -🧪 currently in beta (0.x)
    -🔍 full test coverage and thorough documentation coming in versions after 1.x
    -😊 easy to learn and use
    -💾 install with python3 -m pip install ranged
    -🙏 feedback and support appreciated!

## introduction

Welcome to ranged, a simple yet feature-rich library created with the goal of providing an alternative to the standard library's range function. Ranged is designed to be a more feature-rich version of range while still maintaining excellent performance. It is dependency-free and easy to learn, making it a great choice for any Python project.

Currently, ranged is in beta (0.x), but work is underway to ensure that every version after 1.x will have full test coverage and thorough documentation. Feedback and support are appreciated as this library continues to be improved and developed. Thank you for choosing ranged!

## install

`python3 -m pip install ranged`

or

`pip3 install ranged`

## example

```
for i in Range(10, 90, func=lambda a:a+1, filt=lambda a:a < 15):
	print(i)
```

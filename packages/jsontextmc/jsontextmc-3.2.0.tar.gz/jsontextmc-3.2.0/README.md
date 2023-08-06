<h1><img src="https://gitlab.com/whoatemybutte7/jsontextmc/-/raw/master/logo.png" width="64" height="64"> JSONTextMC</h1>

Minecraft uses two main systems for formatting text.

The Legacy format uses section symbols and hexadecimal color coding,
while the JSON format uses key-value pairs to color individual parts of text.

JSONTextMC is a module for translating legacy messages to and from JSON-formatted text.
Output is not valid JSON by itself, it must be translated into JSON with `json.loads()`.

Strict modes and inheritance of various JSON elements can be controlled.

Requires Python 3.10+.

## Table of Contents

- [Installation](#installation)
- [Supprt](#support)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install **JSONTextMC**.

```shell script
python3 -m pip install jsontextmc
```

See the package page on PyPi [here](https://pypi.org/project/jsontextmc).

Use the output in any place where a JsonTextComponent is accepted *(e.g. **/tellraw**, **/title**, **.json files**)*.

## Support

Supports all Vanilla Minecraft formatting codes:

- All [color codes](https://minecraft.gamepedia.com/Formatting_codes#Color_codes)
- All formatting codes
- Hexidecimal
  - Alows both `#` and `x` as prefix codes

## Usage

Read the PyDocs in the module for details about usage. Essentially:
* ``to_json()``: Legacy -> JSON
* ``from_json()``: JSON -> Legacy

Strict and inheritance modes control how legacy text is handled and translated into JSON.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

If there is an individual issue you would like to bring attention to, please
[open one here](https://gitlab.com/whoatemybutter/jsontextmc/issues/new).

## License

Distributed under the [GPLv3](https://choosealicense.com/licenses/gpl-3.0/) license.
*(visit [GNU's website](https://www.gnu.org/licenses/gpl-3.0.en.html))*

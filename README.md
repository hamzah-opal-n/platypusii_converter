# Platypus II Level Data Converter

This is a tool for use on level data files from Platypus II (2007). Level data can be decompiled from its original .dat files into .json files for easier reading and modification. Decompiled .json files can also be recompiled into .dat files for use in-game.


## Tutorial

1. Install Python from the official site [here](https://www.python.org/) (if you don't already have it)
2. Download this source code
3. Open your command prompt/terminal and navigate to your preferred output directory (where converted files should be saved)
4. Run the script by typing the following:

`python <path/to/source/code/>platypusii_converter.py`


## General Info

- Make a backup of your original level data files, just in case they are overwritten.
- Text string values in a decompiled .json file (actions, enemy/scenery types) can be replaced with integer values and recompilation to .dat will still work. This can be useful for testing or finding unused content.

For more information about the level data format, action and enemy/scenery types, please look at the [docs](docs) folder.


## Contributing

Want a spot in the "Special Thanks" section below? The docs are filled with sections marked "(HELP WANTED)". If you are able to test those things, please let me know your findings by opening an issue or pull request. Alternatively, you can contact me on Discord through the [Claymatic Games server](https://discord.com/invite/claymatic) or by messaging me @vileworx


## Special Thanks

MAKYUNI - testing and helping to figure out most of the action, enemy and scenery types
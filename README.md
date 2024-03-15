# IDA-MapSymbolParser

This script is designed for use within the IDA Pro disassembler to facilitate the renaming of symbols based on information extracted from `.map` files. It automates the process of symbol naming, enhancing the reverse engineering workflow by incorporating meaningful names into the IDA database from the provided map files.

## Features

- **File Selection Dialog**: Allows users to select a `.map` file directly from the IDA Pro interface.
- **Automatic Symbol Renaming**: Parses the selected `.map` file to extract symbol names and their corresponding addresses (RVA + Base) and renames symbols within IDA Pro to reflect these names, improving readability and navigability of the disassembled code.
- **Hexadecimal Conversion**: Converts extracted addresses to hexadecimal format for compatibility with IDA Pro's addressing.

## Usage

1. Ensure that IDA Pro is running and that you have a project open.
2. Execute the script within IDA Pro's scripting console or load it through the File -> Script file menu option.
3. A file selection dialog will appear. Navigate to and select the `.map` file you wish to parse.
4. The script will process the file, renaming symbols in IDA Pro based on the extracted data.

## Requirements

- IDA Pro with IDAPython plugin installed.





# pyside6_extensions

pyside6_extensions is an extension package for PySide6 to enhance the functionality of Magic Shortcut while complying with the **LGPL license**.

## Installation

To use pyside6_extensions with Magic Shortcut, follow these steps:

1. Clone or download this repository to your local machine.
2. Ensure you have Python 3.11 or higher installed.
3. Install the required dependencies using pip:
   ```bash
   pip install .
   ```
4. Compile the project using Nuitka by running the provided `compile.sh` script:
   ```bash
   ./compile.sh
   ```
5. After compilation, copy all content from the `build/pyside6_extensions.dist` directory to the Magic Shortcut program directory.

## Changing PySide6 in Magic Shortcut

Magic Shortcut relies on PySide6 for its functionality. You can freely replace the existing PySide6 in Magic Shortcut with the version compiled from this project. Note that older versions of Magic Shortcut may not work with newer versions of PySide6. It is recommended to check compatibility before making any changes.

**Compatibility**: This version of pyside6_extensions is currently compatible with Magic Shortcut v1.0 (BETA).

## License

This project is licensed under the GNU Lesser General Public License v3.0 (LGPL-3.0). See the [LICENSE](LICENSE) file for more details.

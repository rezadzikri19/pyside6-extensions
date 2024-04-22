python -m nuitka --standalone --plugin-enable=pyside6 --plugin-enable=tk-inter --disable-console --output-dir=build pyside6_extensions.py
rm build/pyside6_extensions.dist/pyside6_extensions.exe
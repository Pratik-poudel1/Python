# Unit Converter GUI

This is a simple graphical application that converts units of distance, weight, and temperature. The user can type a value, select the type of conversion, and see the result immediately.

## Features

* Convert between kilometers and miles
* Convert between pounds and kilograms
* Convert between Celsius and Fahrenheit
* Instant results as you type or change the conversion type
* Simple and clean interface

## How It Works

1. Enter a number in the input box.
2. Select the type of conversion from the dropdown menu.
3. The result appears below automatically.
4. If an invalid number is entered, a message asks for a valid number.

## Requirements

* Python 3
* CustomTkinter library

Install CustomTkinter with:

```bash
pip install customtkinter
```

## Usage

1. Run the Python file:

```bash
python unit_converter.py
```

2. A window will open with an input box, dropdown menu, and result display.
3. Type a value in the input box.
4. Choose a conversion type from the menu.
5. The result will update automatically.

## Supported Conversions

* Kilometers to miles
* Miles to kilometers
* Kilograms to pounds
* Pounds to kilograms
* Celsius to Fahrenheit
* Fahrenheit to Celsius

## Notes

* The window size is set to 300 by 300 pixels.
* The application uses a dark theme with a blue accent.
* The conversion updates automatically whenever the input or selection changes.

## File

* `unit_converter.py` - The main Python program to run the application.

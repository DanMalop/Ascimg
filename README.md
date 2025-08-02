
# Ascimg: Your Image to ASCII Art Converter 🎨

![Project logo](https://github.com/DanMalop/Ascimg/blob/main/assets/ASCIMG.png?raw=true)

---

**Ascimg** is a command-line tool written in Python that allows you to transform any image into vibrant (or not so vibrant) ASCII art. With customization options for scaling and characters, you can create unique artworks directly in your terminal or save them to a file.

---

## Features ✨

* **Grayscale Conversion:** Processes your images in black and white for ASCII conversion.

* **Flexible Resizing:** Scale your image by a given factor or specify a fixed width for the ASCII output, maintaining aspect ratio.

* **Customizable Character Set:** Define your own brightness scale using any sequence of ASCII characters.

* **Console or File Output:** Prints the ASCII art directly to your terminal or saves it to a text file.

* **Compiled with Nuitka:** The program is distributed as a single executable file for easy installation and use without Python dependencies.

---

## Installation and Usage 🚀

### Requirements

* A Unix-like operating system (Linux, macOS) is the primary target for global installation.

* Python 3 (to run the compilation script).

* `pip` (Python package manager).

* `sudo` (to install the executable globally on Linux/macOS).

### Compilation and Global Installation

The easiest way to install `Ascimg` is by using the `build_and_deploy_py.py` automation script, which compiles the program and copies it to `/usr/local/bin`.

1. **Clone the repository:**

    ```bash
    git clone https://github.com/DanMalop/Ascimg.git
    cd ascimg
    ```

2. **Ensure you have the `requirements.txt` file:**
    `Ascimg` requires `opencv-python` and `numpy`. These will be automatically installed in a virtual environment during the compilation process. Your `requirements.txt` file should contain:

    ```
    opencv-python
    numpy
    ```

3. **Run the compilation and deployment script:**
    This script will create a virtual environment, install dependencies, compile `main.py` into an executable named `ascimg` (using Nuitka), and copy it to `/usr/local/bin`.

    ```bash
    sudo ./install.sh
    ```

    You will be prompted for your `sudo` password to copy the executable to the system directory.

4. **Done!**
    You can now run `ascimg` from anywhere in your terminal.

### Basic Usage

Once installed, `ascimg` is simple to use:

```bash
ascimg <path_to_your_image> [options]
```

**Examples:**

* **Convert an image with the default scale factor (0.3) and print to console:**

    ```bash
    ascimg photos/my_image.png
    ```

* **Scale the image to 5% of its original size:**

    ```bash
    ascimg selfie.jpeg --scale 0.05
    ```

* **Invert the order of ASCII characters, lighter characters will be used for darker pixels and vice versa (False by default):**

    ```bash
    ascimg my_image.png --invert True
    # Or the short form:
    ascimg my_image.png -i True
    ```

* **Save the output to a text file:**

    ```bash
    ascimg my_photo.png --output ascii_art.txt
    ```

* **Combine options:**

    ```bash
    ascimg path/to/my_photo.png -s 0.2 -o output.txt -i True
    ```

---

## Command-Line Options ⚙️

Here are all the available options for `ascimg`:

```
usage: ascimg [-h] [--scale SCALE] [--invert INVERT] [--output OUTPUT] image_path

Converts an image to ASCII art.

positional arguments:
  image_path            Path to the image file (e.g., 'monio.png').

options:
  -h, --help            show this help message and exit
  --scale SCALE, -s SCALE
                        Scale factor to resize the image before conversion.
                        A smaller value (e.g., 0.05) produces denser ASCII art.
                        This value is ignored if --width is used.
                        Default: 0.1
  --invert, -i          Inverts the order of ASCII characters. Lighter characters
                        will be used for darker pixels and vice versa.
  --output OUTPUT, -o OUTPUT
                        Path to the file where the ASCII art will be saved.
                        If not specified, it will be printed to the console.
```

---

## Contributions 🤝

Contributions are welcome! If you have ideas to improve `Ascimg`, feel free to open an `issue` or submit a `pull request`.

---

## License 📄

This project is licensed under the GPL License. See the `LICENSE` file for more details.

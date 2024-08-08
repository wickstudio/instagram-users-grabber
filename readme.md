# Wick Studio Instagram Usernames Grabber Tool

![Wick Studio Tool](https://media.discordapp.net/attachments/875162620502626387/1181774688599425034/Screenshot_34.png?ex=65824872&is=656fd372&hm=9dbe62cb474f53decad7d471f4c1df85ad72e4c784c2ebd2068775eb47df0f7f&=&format=webp&quality=lossless&width=1149&height=675)

Wick Tool is a Python script that allows you to check the availability of usernames on Instagram. It provides a simple command-line interface for checking multiple usernames and categorizing them as available or unavailable.

## Features

- Check the availability of usernames on Instagram.
- Categorize usernames into available and unavailable lists.
- Easy-to-use command-line interface.
- **New Update:** Usernames are now directly written to their respective files (`available_usernames.txt` and `unavailable_usernames.txt`) as they are checked, without waiting for the entire process to finish.

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/wickstudio/instagram-users-grabber.git
   ```

2. Run the `install.bat` file:

   ```shell
   install.bat
   ```

   This will install the required Python packages.

## Usage

1. Run the `start.bat` file to start the tool:

   ```shell
   start.bat
   ```

2. Choose an option from the menu:
   - **Check Usernames in file.txt**: Check the availability of usernames stored in the "file.txt" file and categorize them.
   - **Exit**: Exit the tool.

3. If you choose to check usernames, the tool will immediately write each checked username to its respective file:
   - **available_usernames.txt**: Contains available usernames.
   - **unavailable_usernames.txt**: Contains unavailable usernames.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [colorama](https://pypi.org/project/colorama/): A Python package for adding colored output to the terminal.
- [pyfiglet](https://pypi.org/project/pyfiglet/): A Python package for creating ASCII art text.
- [selenium](https://pypi.org/project/selenium/): A Python package for automating web browsers.

## Author

- Wick Studio
- GitHub: [Wick Studio](https://github.com/wickstudio)

## Contact

- Email: wick@wick-studio.com
- Website: https://wickdev.me
- Discord: https://discord.gg/wicks
- YouTube: https://www.youtube.com/@wick_studio

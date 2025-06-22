# String Reverser

A professional GUI application that reverses any input string with support for multiple languages and Unicode characters.

![String Reverser](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)

## 🌟 Features

- **Clean, modern GUI** built with tkinter
- **Multi-language support** (English, Chinese, Japanese, Arabic, etc.)
- **Unicode character handling** including emojis
- **Professional installer** with Inno Setup
- **Cross-platform compatibility** (Windows executable)
- **Real-time input** with button-triggered reversal
- **Clear functionality** to reset input and output

## 📸 Screenshots

![license agreement](https://github.com/user-attachments/assets/cae02cef-fb7a-4142-8e34-168dd8071bea)

### License Agreement


![create shortcut](https://github.com/user-attachments/assets/1582f5a9-5cf6-4598-88da-2791467a6b59)

### Create Shortcut


![icon](https://github.com/user-attachments/assets/eb588e34-268b-4496-a931-83a924a0f6c5)

### Desktop Icon

![reverse string demo](https://github.com/user-attachments/assets/30d8fd75-9259-4738-aa5f-1a5d60acdf43)

### Reverse String Demo


## 🚀 Quick Start

### For End Users (No Python Required)

1. **Download the installer:**
   - Go to [Releases](https://github.com/yourusername/string-reverser/releases)
   - Download `StringReverser_Setup.exe`
   - Run the installer and follow the wizard

2. **Use the application:**
   - Type any text in the input field
   - Click "Reverse" to see the reversed version
   - Click "Clear" to start over

### For Developers

#### Prerequisites
- Python 3.6 or higher
- Windows (for executable building)

#### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/string-reverser.git
cd string-reverser

# Install dependencies
pip install -r requirements.txt

# Run the application
python string_reverser.py
```

## 🛠️ Building from Source

### Create Executable
```bash
# Simple executable
python build_exe.py

# With custom icon (place app_icon.ico in project folder)
python build_with_icon.py
```

### Create Installer
```bash
# Install Inno Setup from https://jrsoftware.org/isdl.php
python build_installer.py
```

## 📁 Project Structure

```
string-reverser/
├── string_reverser.py          # Main GUI application
├── simple_reverser.py          # Command-line version
├── build_exe.py               # Executable builder
├── build_with_icon.py         # Icon-enabled builder
├── build_installer.py         # Installer builder
├── build_any_exe.py           # Generic builder for any Python app
├── installer_script.iss       # Inno Setup configuration
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── LICENSE.txt                # MIT License
├── .gitignore                 # Git ignore rules
└── app_icon.ico              # Custom icon (optional)
```

## 🎯 Usage Examples

### Supported Input Types
- **English**: "Hello World" → "dlroW olleH"
- **Numbers**: "12345" → "54321"
- **Mixed content**: "Hello123!" → "!321olleH"
- **Unicode**: "café" → "éfac"
- **Asian languages**: "こんにちは" → "はちにんこ"
- **Arabic**: "مرحبا" → "ابحرم"
- **Emojis**: "Hello 🌍" → "🌍 olleH"

## 🔧 Development

### Running Tests
```bash
# Test the GUI version
python string_reverser.py

# Test the command-line version
python simple_reverser.py
```

### Adding Features
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📦 Distribution

### Creating Releases
1. Build the installer: `python build_installer.py`
2. Create a new GitHub release
3. Upload `installer/StringReverser_Setup.exe`
4. Add release notes and changelog

### Alternative Distribution Methods
- **Direct download**: Share the installer file
- **Cloud storage**: Upload to Google Drive, Dropbox
- **Software sites**: Submit to Softpedia, Download.com

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Contribution Guidelines
1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## 🙏 Acknowledgments

- **tkinter** for the GUI framework
- **PyInstaller** for executable creation
- **Inno Setup** for professional installer creation
- **Python community** for excellent documentation

## 📞 Support

If you encounter any issues or have questions:

1. **Check existing issues** on GitHub
2. **Create a new issue** with detailed information
3. **Contact the maintainer** via GitHub

## 🔄 Changelog

### Version 1.0.0
- Initial release
- GUI application with tkinter
- Multi-language support
- Professional installer
- Custom icon support

---

**Made with ❤️ using Python and tkinter**

*Star this repository if you find it useful!* 

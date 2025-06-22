"""
Build Script for String Reverser Installer
This script builds the executable and creates an installer
"""

import subprocess
import sys
import os
import shutil

def check_requirements():
    """Check if required tools are installed"""
    print("Checking requirements...")
    
    # Check if PyInstaller is available
    try:
        import PyInstaller
        print("✅ PyInstaller is available")
    except ImportError:
        print("❌ PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller installed")
    
    # Check if Inno Setup is installed
    inno_paths = [
        r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe",
        r"C:\Program Files\Inno Setup 6\ISCC.exe",
        r"C:\Program Files (x86)\Inno Setup 5\ISCC.exe",
        r"C:\Program Files\Inno Setup 5\ISCC.exe"
    ]
    
    inno_compiler = None
    for path in inno_paths:
        if os.path.exists(path):
            inno_compiler = path
            break
    
    if inno_compiler:
        print(f"✅ Inno Setup found: {inno_compiler}")
        return inno_compiler
    else:
        print("❌ Inno Setup not found")
        print("📥 Download from: https://jrsoftware.org/isdl.php")
        print("💡 Install Inno Setup and run this script again")
        return None

def build_executable():
    """Build the executable using PyInstaller"""
    print("\n🔨 Building executable...")
    
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=StringReverser",
        "string_reverser.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print("✅ Executable built successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to build executable: {e}")
        return False

def create_installer_files():
    """Create necessary files for the installer"""
    print("\n📝 Creating installer files...")
    
    # Create LICENSE.txt if it doesn't exist
    if not os.path.exists("LICENSE.txt"):
        with open("LICENSE.txt", "w") as f:
            f.write("""MIT License

Copyright (c) 2024 String Reverser

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")
        print("✅ LICENSE.txt created")
    
    # Create installer directory
    if not os.path.exists("installer"):
        os.makedirs("installer")
        print("✅ installer directory created")

def build_installer(inno_compiler):
    """Build the installer using Inno Setup"""
    print("\n🔨 Building installer...")
    
    cmd = [inno_compiler, "installer_script.iss"]
    
    try:
        subprocess.check_call(cmd)
        print("✅ Installer built successfully")
        print(f"📁 Installer location: installer/StringReverser_Setup.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to build installer: {e}")
        return False

def main():
    print("=== String Reverser - Installer Builder ===")
    print("This will create both an executable and a professional installer.\n")
    
    # Check if source file exists
    if not os.path.exists("string_reverser.py"):
        print("❌ Error: string_reverser.py not found!")
        return
    
    # Check requirements
    inno_compiler = check_requirements()
    if not inno_compiler:
        return
    
    # Build executable
    if not build_executable():
        return
    
    # Create installer files
    create_installer_files()
    
    # Build installer
    if build_installer(inno_compiler):
        print("\n🎉 Success! Your installer is ready for distribution.")
        print("📤 Share installer/StringReverser_Setup.exe with users")
        print("💡 Users can now install your program like any other Windows application!")
    else:
        print("\n❌ Failed to create installer.")

if __name__ == "__main__":
    main() 
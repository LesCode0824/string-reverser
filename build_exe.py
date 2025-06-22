"""
Build script for String Reverser
This script helps create an executable file using PyInstaller
"""

import subprocess
import sys
import os

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("PyInstaller is already installed.")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installed successfully!")

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building executable...")
    
    # PyInstaller command with options
    cmd = [
        "pyinstaller",
        "--onefile",           # Create a single executable file
        "--windowed",          # Don't show console window (for GUI apps)
        "--name=StringReverser",  # Name of the executable
        "--icon=icon.ico",     # Optional: add an icon (if you have one)
        "string_reverser.py"
    ]
    
    # Remove icon option if no icon file exists
    if not os.path.exists("icon.ico"):
        cmd.remove("--icon=icon.ico")
    
    try:
        subprocess.check_call(cmd)
        print("\n✅ Build successful!")
        print("📁 Executable created in: dist/StringReverser.exe")
        print("📦 You can now distribute the .exe file to other users!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    
    return True

def main():
    print("=== String Reverser - Build Script ===")
    print("This will create an executable file that others can run without Python.\n")
    
    # Check if source file exists
    if not os.path.exists("string_reverser.py"):
        print("❌ Error: string_reverser.py not found in current directory!")
        return
    
    # Install PyInstaller
    install_pyinstaller()
    
    # Build executable
    if build_executable():
        print("\n🎉 Success! Your program is now packaged as an executable.")
        print("📤 Share the .exe file from the 'dist' folder with others.")
    else:
        print("\n❌ Failed to build executable. Please check the error messages above.")

if __name__ == "__main__":
    main() 
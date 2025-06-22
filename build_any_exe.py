"""
Generic Build Script for Python Programs
This script can package any Python program into an executable
"""

import subprocess
import sys
import os
import argparse

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("PyInstaller is already installed.")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installed successfully!")

def build_executable(python_file, output_name=None, show_console=False):
    """Build the executable using PyInstaller"""
    if not output_name:
        # Use the Python file name without .py extension
        output_name = os.path.splitext(python_file)[0]
    
    print(f"Building executable for: {python_file}")
    print(f"Output name: {output_name}")
    
    # PyInstaller command with options
    cmd = [
        "pyinstaller",
        "--onefile",           # Create a single executable file
        "--name=" + output_name,  # Name of the executable
        python_file
    ]
    
    # Add --windowed flag for GUI apps (no console window)
    if not show_console:
        cmd.insert(1, "--windowed")
    
    try:
        subprocess.check_call(cmd)
        print(f"\n✅ Build successful!")
        print(f"📁 Executable created in: dist/{output_name}.exe")
        print("📦 You can now distribute the .exe file to other users!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Build Python programs into executables")
    parser.add_argument("python_file", help="The Python file to build (e.g., my_program.py)")
    parser.add_argument("--name", "-n", help="Name for the executable (optional)")
    parser.add_argument("--console", "-c", action="store_true", 
                       help="Show console window (default: hidden for GUI apps)")
    
    args = parser.parse_args()
    
    # Check if source file exists
    if not os.path.exists(args.python_file):
        print(f"❌ Error: {args.python_file} not found!")
        return
    
    print("=== Generic Python to EXE Builder ===")
    print(f"Building: {args.python_file}")
    print(f"Console: {'Yes' if args.console else 'No'}\n")
    
    # Install PyInstaller
    install_pyinstaller()
    
    # Build executable
    if build_executable(args.python_file, args.name, args.console):
        print(f"\n🎉 Success! {args.python_file} is now packaged as an executable.")
        print("📤 Share the .exe file from the 'dist' folder with others.")
    else:
        print("\n❌ Failed to build executable. Please check the error messages above.")

if __name__ == "__main__":
    # If no arguments provided, show usage
    if len(sys.argv) == 1:
        print("=== Generic Python to EXE Builder ===")
        print("Usage examples:")
        print("  python build_any_exe.py my_program.py")
        print("  python build_any_exe.py my_program.py --name MyApp")
        print("  python build_any_exe.py my_program.py --console")
        print("\nFor help: python build_any_exe.py --help")
    else:
        main() 
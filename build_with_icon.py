"""
Build Script with Icon Support for String Reverser
This script builds the executable and installer with custom icons
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
        return None

def create_default_icon():
    """Create a simple default icon if none exists"""
    if not os.path.exists("app_icon.ico"):
        print("📝 Creating default icon...")
        # You can replace this with a real icon creation process
        # For now, we'll just create a placeholder
        print("💡 Place your app_icon.ico file in this directory for a custom icon")
        return False
    return True

def build_executable_with_icon():
    """Build the executable using PyInstaller with icon"""
    print("\n🔨 Building executable with icon...")
    
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=StringReverser",
        "string_reverser.py"
    ]
    
    # Add icon if it exists
    if os.path.exists("app_icon.ico"):
        cmd.append("--icon=app_icon.ico")
        print("✅ Using custom icon: app_icon.ico")
    else:
        print("ℹ️  Using default icon")
    
    try:
        subprocess.check_call(cmd)
        print("✅ Executable built successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to build executable: {e}")
        return False

def create_installer_with_icon():
    """Create installer script with icon support"""
    print("\n📝 Creating installer script with icon...")
    
    installer_script = """; Inno Setup Script for String Reverser with Icon
; This creates a professional Windows installer

[Setup]
; Basic setup information
AppName=String Reverser
AppVersion=1.0
AppPublisher=Your Name
AppPublisherURL=https://your-website.com
AppSupportURL=https://your-website.com/support
AppUpdatesURL=https://your-website.com/updates
DefaultDirName={autopf}\\String Reverser
DefaultGroupName=String Reverser
AllowNoIcons=yes
LicenseFile=LICENSE.txt
OutputDir=installer
OutputBaseFilename=StringReverser_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

; Minimum Windows version
MinVersion=6.1

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1

[Files]
; Main executable
Source: "dist\\StringReverser.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\\String Reverser"; Filename: "{app}\\StringReverser.exe"
Name: "{group}\\{cm:UninstallProgram,String Reverser}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\\String Reverser"; Filename: "{app}\\StringReverser.exe"; Tasks: desktopicon
Name: "{userappdata}\\Microsoft\\Internet Explorer\\Quick Launch\\String Reverser"; Filename: "{app}\\StringReverser.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\\StringReverser.exe"; Description: "{cm:LaunchProgram,String Reverser}"; Flags: nowait postinstall skipifsilent

[Code]
// Optional: Add custom installation logic here
function InitializeSetup(): Boolean;
begin
  Result := True;
end;
"""
    
    with open("installer_script.iss", "w") as f:
        f.write(installer_script)
    
    print("✅ Installer script created")

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

def create_license_file():
    """Create LICENSE.txt if it doesn't exist"""
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

def main():
    print("=== String Reverser - Icon Builder ===")
    print("This will create an executable and installer with custom icons.\n")
    
    # Check if source file exists
    if not os.path.exists("string_reverser.py"):
        print("❌ Error: string_reverser.py not found!")
        return
    
    # Check requirements
    inno_compiler = check_requirements()
    if not inno_compiler:
        return
    
    # Check for icon
    create_default_icon()
    
    # Build executable with icon
    if not build_executable_with_icon():
        return
    
    # Create installer files
    create_license_file()
    create_installer_with_icon()
    
    # Create installer directory
    if not os.path.exists("installer"):
        os.makedirs("installer")
    
    # Build installer
    if build_installer(inno_compiler):
        print("\n🎉 Success! Your installer with icon is ready for distribution.")
        print("📤 Share installer/StringReverser_Setup.exe with users")
        print("💡 Users can now install your program like any other Windows application!")
    else:
        print("\n❌ Failed to create installer.")

if __name__ == "__main__":
    main() 
; Inno Setup Script for String Reverser with Icon
; This creates a professional Windows installer

[Setup]
; Basic setup information
AppName=String Reverser
AppVersion=1.0
AppPublisher=Your Name
AppPublisherURL=https://your-website.com
AppSupportURL=https://your-website.com/support
AppUpdatesURL=https://your-website.com/updates
DefaultDirName={autopf}\String Reverser
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
Source: "dist\StringReverser.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\String Reverser"; Filename: "{app}\StringReverser.exe"
Name: "{group}\{cm:UninstallProgram,String Reverser}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\String Reverser"; Filename: "{app}\StringReverser.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\String Reverser"; Filename: "{app}\StringReverser.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\StringReverser.exe"; Description: "{cm:LaunchProgram,String Reverser}"; Flags: nowait postinstall skipifsilent

[Code]
// Optional: Add custom installation logic here
function InitializeSetup(): Boolean;
begin
  Result := True;
end;

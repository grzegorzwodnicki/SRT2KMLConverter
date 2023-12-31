; Script generated by the Inno Script Studio Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!
[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{AE61073F-3D89-432C-9D9B-EE7C2C13C756}
AppName=SRT/KML Converter
AppVersion=1.01
AppPublisher=USRI
DefaultDirName={commonpf}\SRT2KML Converter\
DefaultGroupName=SRT KML Converter
AllowNoIcons=yes
OutputBaseFilename=SRT2KML Converter-1.01
Compression=lzma
SolidCompression=yes
DisableDirPage=no
ArchitecturesInstallIn64BitMode=
SetupIconFile=assets\g2\logo.ico

;LicenseFile=SRT KML Converter eula.txt

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}";

[Files]
Source: "dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "ui\assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs createallsubdirs

;Source: "ui\assets\Audiowide-Regular.ttf"; DestDir: "{autofonts}"; FontInstall: "Audiowide Regular"; Flags: onlyifdoesntexist;
;Source: "ui\assets\Saira-SemiBold.ttf"; DestDir: "{autofonts}"; FontInstall: "Saira SemiBold"; Flags: onlyifdoesntexist;
;Source: "ui\assets\Saira-ExtraBold.ttf"; DestDir: "{autofonts}"; FontInstall: "Saira ExtraBold"; Flags: onlyifdoesntexist;
;Source: "ui\assets\Saira-Medium.ttf"; DestDir: "{autofonts}"; FontInstall: "Saira Medium"; Flags: onlyifdoesntexist;
;Source: "ui\assets\Saira-Medium.ttf"; DestDir: "{autofonts}"; FontInstall: "Saira Medium"; Flags: onlyifdoesntexist;

; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\SRT KML Converter"; Filename: "{app}\SRT2KML Converter.exe"
Name: "{group}\{cm:UninstallProgram,SARTopo KML Converter}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\SRT KML Converter"; Filename: "{app}\SRT2KML Converter.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\SRT2KML Converter.exe"; Description: "{cm:LaunchProgram,SRT KML Converter}"; Flags: nowait postinstall skipifsilent

[InstallDelete]
Type: filesandordirs; name: "{app}\cryptography"

[Setup]
UninstallDisplayIcon={app}\SRT2KML Converter.exe

[Registry]
Root: HKCU; Subkey: "Software\USRI\SRT2KML Converter\scale_factor"; ValueType: string; ValueData: "1.0"
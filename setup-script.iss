[Setup]
AppName=OneProjectWed
AppVersion=1.0.0
DefaultDirName={autopf}\OneProjectWed
DefaultGroupName=OneProjectWed
OutputDir=output
OutputBaseFilename=OneProjectWed-Setup
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=lowest

[Files]
Source: "build\libs\*.jar"; DestDir: "{app}"; DestName: "App.jar"; Flags: ignoreversion

[Icons]
Name: "{group}\OneProjectWed"; Filename: "javaw.exe"; Parameters: "-jar ""{app}\App.jar"""; WorkingDir: "{app}"
Name: "{group}\Uninstall OneProjectWed"; Filename: "{uninstallexe}"

[Run]
Filename: "javaw.exe"; Parameters: "-jar ""{app}\App.jar"""; Description: "Launch OneProjectWed"; Flags: postinstall nowait skipifsilent

#define AppName AppName
#define AppVersion AppVersion
#define JarFileName JarFileName
#define OutputBaseName OutputBaseName

[Setup]
AppName={#AppName}
AppVersion={#AppVersion}
DefaultDirName={autopf}\{#AppName}
DefaultGroupName={#AppName}
OutputDir=output
OutputBaseFilename={#OutputBaseName}
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=lowest

[Files]
Source: "build\libs\{#JarFileName}"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#AppName}"; Filename: "javaw.exe"; Parameters: "-jar ""{app}\{#JarFileName}"""; WorkingDir: "{app}"
Name: "{group}\Uninstall {#AppName}"; Filename: "{uninstallexe}"

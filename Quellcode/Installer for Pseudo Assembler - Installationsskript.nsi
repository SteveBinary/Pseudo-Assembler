!define MUI_ICON "C:\Users\steve\Schule\Seminararbeit\Programm\Installer\PseudoAssembler\P.ico"
!define MUI_COMPONENTSPAGE_NODESC
CRCCheck On

!include "MUI.nsh"

Name "PseudoAssembler"
OutFile "Install PseudoAssembler.exe"
InstallDir "$PROGRAMFILES\PseudoAssembler"


!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_LANGUAGE "German"

Section ""
SetOutPath $INSTDIR
  File C:\Users\steve\Schule\Seminararbeit\Programm\Installer\PseudoAssembler\PseudoAssembler.exe
  File C:\Users\steve\Schule\Seminararbeit\Programm\Installer\PseudoAssembler\instruction_set.txt
  File C:\Users\steve\Schule\Seminararbeit\Programm\Installer\PseudoAssembler\P.ico
  File C:\Users\steve\Schule\Seminararbeit\Programm\Installer\PseudoAssembler\Dokumentation.pdf
  WriteUninstaller "$INSTDIR\uninstall PseudoAssembler.exe"
SectionEnd


Section "Startmenü Verknüpfung erstellen"
  CreateShortCut "$SMPROGRAMS\PseudoAssembler.lnk" "$INSTDIR\PseudoAssembler.exe"
  CreateShortCut "$SMPROGRAMS\uninstall PseudoAssembler.lnk" "$INSTDIR\uninstall PseudoAssembler.exe"
SectionEnd


Section "Desktop Verknüpfung erstellen"
  CreateShortCut "$DESKTOP\PseudoAssembler.lnk" "$INSTDIR\PseudoAssembler.exe"
SectionEnd


Section "Uninstall"
  Delete "$INSTDIR\uninstall PseudoAssembler.exe"
  Delete $INSTDIR\PseudoAssembler.exe
  Delete $INSTDIR\instruction_set.txt
  Delete $INSTDIR\P.ico
  Delete $INSTDIR\Dokumentation.pdf
  Delete $SMPROGRAMS\PseudoAssembler.lnk
  Delete "$SMPROGRAMS\uninstall PseudoAssembler.lnk"
  Delete $DESKTOP\PseudoAssembler.lnk
  RMDir $INSTDIR
SectionEnd
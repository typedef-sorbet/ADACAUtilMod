# Overview

_Very_ basic mod for ADACA routing/theorycrafting assistance.

## Features

- Level exits, damage volumes, blocking volumes, and checkpoint volumes are visible
- Player position readout
- Level exit readout
- Data module and reader position readout
- Weapon and item spawn menus
- Speedometer (both base and absolute)
- _Kinda_ `mat_fullbright` equivalent 

## Keybinds

- `Alt-Q`: Toggle weapon spawn menu 
- `Alt-E`: Toggle item spawn menu 
- `Alt-D`: Toggle damage volume visibility
- `Alt-I`: Toggle blocking volume (invisible wall) visibility
- `Alt-C`: Toggle checkpoint volume visibility
- `Alt-F`: Toggle "`mat_fullbright` at home" 

## Notes

Checkpoint and blocking volume visualizers do not currently represent the
true extent of collision -- hoping to address this in the future. For now,
though, you should be able to at least get a general sense of their position.

# Installation

- Install [UE4SS](https://github.com/UE4SS-RE/RE-UE4SS/releases) in your ADACA install folder
- In `ADACA/Content/Paks`, create a new folder (if one doesn't exist) called `LogicMods`
- Place `ADACAUtilMod.pak` into the `LogicMods` folder

If UE4SS was installed correctly, the mod should automatically be loaded.

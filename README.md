# TS4 Block Generate Outfit

This mods prevents that TS4 generates new outfits for sims if an outfit exist.

If an outfit is missing the mod always allows the creation of the missing outfit.

Mods can still replace outfits without generating them, they will not be blocked. 
There might be other ways for TS4 to replace outfits, so it is not 100 % safe.

## Usage
To replace special outfit with a custom one the easiest thing is to copy the outfit from an existing outfit.
I suggest to use [CopyOutfits](https://github.com/Oops19/TS4-CopyOutfits) and create the desired outfit in CAS as Everyday.1 or something like this.
Back in game change the outfit to Everyday.1 and copy it.
Paste it to the special outfit which should be replaced permanently.

### Configuration
The default configuration is stored in `The Sims 4/mod_data/block_generate_outfits/block_generate_outfits.txt` and can be easily altered.
It blocks only BATHING.0 and SPECIAL.1.

To use cheat commands enable the cheat console (Shift+Ctrl+C `testingcheats true`).
* `o19.bgo.help` shows a brief help.
* `o19.bgo.toggle` to disable and enable this mod temporarily.
* `o19.bgo.edit + EVERYDAY 4` will prevent that also the 5th 'Everyday' outfit gets replaced, even though this should never be re-generated.
* `o19.bgo.edit - SPECIAL 1` will remove the Special.1 outfit from the list.

All edit and toggle commands are not persisted, after starting the game the mod is active and the settings read from the configuration file apply.


# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.108.329, S4CL 3.6, TS4Lib 0.3.24 (2024-07-25).
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
Download the ZIP file, not the sources.
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not installed download and install TS4 and these mods.
All are available for free.

## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*`
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this. 
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2024 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 / o19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
* or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check the XML structure of custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).

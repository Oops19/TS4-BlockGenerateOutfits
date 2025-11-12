# 👗 TS4 Keep Outfit
## 🚫 Block Outfit Generation

This mod prevents The Sims 4 from generating new outfits for Sims **if an outfit already exists**.

- If an outfit is missing, the game is still allowed to generate it.
- Mods that **replace** outfits (without generating them) are not blocked.
- Note: There may be other ways TS4 replaces outfits, so this mod is not 100% foolproof.


## 👕 Usage
Just install the mod, it blocks the replacement of these outfits:
* `BATHING.0` (nude)
* * `SPECIAL.1` (towel)

## 🧵 Customization of Special Outfits
Outfit customization is **not** part of this mod.  
To replace a special or standard outfit with a custom one:

1. Use [Copy Outfits](https://github.com/Oops19/TS4-CopyOutfits).
2. In CAS, create the desired outfit as `Everyday.1` or similar.
3. Back in-game, switch to `Everyday.1` and copy it using Copy Outfits.
4. Paste it to the special outfit slot you want to replace permanently.

## 🧑‍💻 Cheat Commands
Enable the cheat console with `Shift+Ctrl+C` and enter `testingcheats true`.

- `o19.bgo.help` — Show a brief help message
- `o19.bgo.toggle` — Temporarily enable/disable the mod
- `o19.bgo.edit + EVERYDAY 4` — Block generation of the 5th Everyday outfit
- `o19.bgo.edit - SPECIAL 1` — Unblock generation of the Special.1 outfit

> ⚠️ Changes made via cheat commands are **not saved**.  
> On game restart, the mod reloads settings from the configuration file.

## ⚙️ Configuration
The default config file is located at `The Sims 4/mod_data/block_generate_outfits/block_generate_outfits.txt`

By default, it blocks:
- `BATHING.0`
- `SPECIAL.1`

You can edit this file to block or unblock specific outfit slots.  
For example, you might choose to block additional Everyday or Party outfits depending on your gameplay needs.

## 🗂️ Configuration Format
It uses a simple Python-style set structure to define which outfits should be blocked from automatic generation:

```python
{
    ('BATHING', 0),
    ('SPECIAL', 1),
}
```
### ➕ To block another outfit:
Add a new line inside the {} with the outfit category and index in parentheses, followed by a comma:
```python
{
    ('BATHING', 0),
    ('SPECIAL', 1),
    ('EVERYDAY', 4),
}
```

* Each entry must end with a comma.
* Index numbers start at 0 (e.g., EVERYDAY 0 is the first Everyday outfit).

## 🎽 Supported Outfit Categories

The following outfit categories are supported and must be written in **UPPER CASE** in the configuration file:

- EVERYDAY
- FORMAL
- ATHLETIC
- SLEEP
- PARTY
- BATHING
- CAREER
- SITUATION
- SPECIAL
- SWIMWEAR
- HOTWEATHER
- COLDWEATHER
- BATUU
- SMALL_BUSINESS

Each category may support different index ranges. For example:
- `EVERYDAY`, `FORMAL`, `ATHLETIC`, etc. typically support indices `0–4`
- `CAREER` supports `0–2`
- `BATHING`, `SITUATION` usually support only `0`
- `SPECIAL` supports `0–2` (0 = Default, 1 = Towel, 2 = Fashion)

Make sure to follow the exact format shown in the sample lines. Incorrect entries will be ignored.


---

# 📝 Addendum

## 🔄 Game compatibility
This mod has been tested with `The Sims 4` 1.119.109, S4CL 3.17, TS4Lib 0.3.42.
It is expected to remain compatible with future releases of TS4, S4CL, and TS4Lib.

## 📦 Dependencies
Download the ZIP file - not the source code.
Required components:
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not already installed, download and install TS4 and the listed mods. All are available for free.

## 📥 Installation
* Locate the localized `The Sims 4` folder (it contains the `Mods` folder).
* Extract the ZIP file directly into this folder.

This will create:
* `Mods/_o19_/$mod_name.ts4script`
* `Mods/_o19_/$mod_name.package`
* `mod_data/$mod_name/*`
* `mod_documentation/$mod_name/*` (optional)
* `mod_sources/$mod_name/*` (optional)

Additional notes:
* CAS and Build/Buy UGC without scripts will create `Mods/o19/$mod_name.package`.
* A log file `mod_logs/$mod_name.txt` will be created once data is logged.
* You may safely delete `mod_documentation/` and `mod_sources/` folders if not needed.

### 📂 Manual Installation
If you prefer not to extract directly into `The Sims 4`, you can extract to a temporary location and copy files manually:
* Copy `mod_data/` contents to `The Sims 4/mod_data/` (usually required).
* `mod_documentation/` is for reference only — not required.
* `mod_sources/` is not needed to run the mod.
* `.ts4script` files can be placed in a folder inside `Mods/`, but storing them in `_o19_` is recommended for clarity.
* `.package` files can be placed in a anywhere inside `Mods/`.

## 🛠️ Troubleshooting
If installed correctly, no troubleshooting should be necessary.
For manual installs, verify the following:
* Does your localized `The Sims 4` folder exist? (e.g. localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...)
  * Does it contain a `Mods/` folder?
    * Does Mods/_o19_/ contain:
      * `ts4lib.ts4script` and `ts4lib.package`?
      * `{mod_name}.ts4script` and/or `{mod_name}.package`
* Does `mod_data/` contain `{mod_name}/` with files?
* Does `mod_logs/` contain:
  * `Sims4CommunityLib_*_Messages.txt`?
  * `TS4-Library_*_Messages.txt`?
  * `{mod_name}_*_Messages.txt`?
* Are there any `last_exception.txt` or `last_exception*.txt` files in `The Sims 4`?


* When installed properly this is not necessary at all.
For manual installations check these things and make sure each question can be answered with 'yes'.
* Does 'The Sims 4' (localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...) exist?
  * Does `The Sims 4` contain the folder `Mods`?
    * Does `Mods` contain the folder `_o19_`? 
      * Does `_19_` contain `ts4lib.ts4script` and `ts4lib.package` files?
      * Does `_19_` contain `{mod_name}.ts4script` and/or `{mod_name}.package` files?
  * Does `The Sims 4` contain the folder `mod_data`?
    * Does `mod_data` contain the folder `{mod_name}`?
      * Does `{mod_name}` contain files or folders?
  * Does `The Sims 4` contain the `mod_logs` ?
    * Does `mod_logs` contain the file `Sims4CommunityLib_*_Messages.txt`?
    * Does `mod_logs` contain the file `TS4-Library_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
    * Does `mod_logs` contain the file `{mod_name}_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
  * Doesn't `The Sims 4` contain the file(s) `last_exception.txt`  and/or `last_exception*.txt` ?
* Share the `The Sims 4/mod_logs/Sims4CommunityLib_*_Messages.txt` and `The Sims 4/mod_logs/{mod_name}_*_Messages.txt`  file.

If issues persist, share:
`mod_logs/Sims4CommunityLib_*_Messages.txt`
`mod_logs/{mod_name}_*_Messages.txt`

## 🕵️ Usage Tracking / Privacy
This mod does not send any data to external servers.
The code is open source, unobfuscated, and fully reviewable.

Note: Some log entries (especially warnings or errors) may include your local username if file paths are involved.
Share such logs with care.

## 🔗 External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## ⚖️ Copyright and License
* © 2020-2025 [Oops19](https://github.com/Oops19)
* `.package` files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* All other content (unless otherwise noted): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 

You may use and adapt this mod and its code — even without owning The Sims 4.
Have fun extending or integrating it into your own mods!

Oops19 / o19 is not affiliated with or endorsed by Electronic Arts or its licensors.
Game content and materials © Electronic Arts Inc. and its licensors.
All trademarks are the property of their respective owners.

## 🧾 Terms of Service
* Do not place this mod behind a paywall.
* Avoid creating mods that break with every TS4 update.
* For simple tuning mods, consider using:
  * [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
  * [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To verify custom tuning structures, use:
  * [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).

## 🗑️ Removing the Mod
Installing this mod creates files in several directories. To fully remove it, delete:
* `The Sims 4/Mods/_o19_/$mod_name.*`
* `The Sims 4/mod_data/_o19_/$mod_name/`
* `The Sims 4/mod_documentation/_o19_/$mod_name/`
* `The Sims 4/mod_sources/_o19_/$mod_name/`

To remove all of my mods, delete the following folders:
* `The Sims 4/Mods/_o19_/`
* `The Sims 4/mod_data/_o19_/`
* `The Sims 4/mod_documentation/_o19_/`
* `The Sims 4/mod_sources/_o19_/`

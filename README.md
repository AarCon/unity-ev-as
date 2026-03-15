# EvScript
EvScript refers to scripts with an assembly-like syntax that use EvCmd's as defined by BDSP. All currently known EvCmd's can be found in ev_cmd.csv and commands.json, and examples for EvScripts can be found in the examples directly.</br>
If you want to edit existing scripts the best way is by dumping all the scripts with ev-parse and then editing them before assembling and repacking them with this program.

## Tool Setup
pip install -r requirements.txt

## ev-as
Assembler for EvScripts from Pokemon BDSP

### ev-as Usage
Takes an EvScript (.ev) file and assembles it and repacks it into the Unity ev_script bundle.

Example:
```python
src/ev_as.py -i d05r0114.ev -o Dpr/ev_scripts -s d05r0114
```

### ev-as Yaml Mode Usage 
Takes an EvScript (.ev) file and assembles it into the corresposonding Unity .asset file

Example:
```python
python .\src\ev_as.py --input .\Assets\evscriptdata\eventasset --mode yaml
```

## ev-parse
Parser for EvScripts from Pokemon BDSP

### ev-parse Usage
Takes an ev_script file and extracts and parses all of the individual script files

Example:
```python
src/ev_parse.py -i Dpr/ev_script
```

### ev-parse Yaml mode Usage
Takes the unity .asset files and parses all of the individual script files

Example:
```python
python .\src\ev_parse.py -i Assets\evscriptdata\eventasset -m yaml
```

You can also define where you want the output of the `ev_parse` with the `-o` or `--output` tags.

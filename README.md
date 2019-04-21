# PARSE EmlenMUD

Parser for Everwar Emlen MUD .are files

Generates a JSON file with all the vnums, connections, and sector types to display it in a nice format

You can generate a JSON file of the whole mud like so:

`
python area.py playarea.lst mud.json
`

Or just individual areas:

`
python area.py arborloom.are arborloom.json
`

This file can then be used to generate a map.

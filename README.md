# jsonpretty
Pipe in a json string and output a a pretty version

`chmod +x jsonpretty.py`

put it in your `bin`

`ln -s ~/bin/jsonpretty ./jsonpretty.py`

Pipe some stuff in

`echo '{ "test" : "test", "list" :[1,2,4]}' | jsonpretty`

Then pipe it out

`echo '{ "test" : "test", "list" :[1,2,4]}' | jsonpretty > pretty.json`

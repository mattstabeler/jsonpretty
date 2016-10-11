# jsonpretty
Pipe in a json string and output a a pretty version

`chmod +x jsonpretty.py`

put it in your `bin`

`ln -s ~/path/to/jsonpretty/jsonpretty.py ~/bin/jsonpretty`

Pipe some stuff in

`echo '{ "test" : "test", "list" :[1,2,4]}' | jsonpretty`

outputs
```
{
    "list": [
        1,
        2,
        4
    ],
    "test": "test"
}
```

Then pipe it out

`echo '{ "test" : "test", "list" :[1,2,4]}' | jsonpretty > pretty.json`

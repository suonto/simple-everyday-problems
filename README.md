# Simple Everyday Problems

## Problem 1: JSON Pretty Print
You received a bit of JSON data and you just want to format it nicely so that for each value in the document, the nested path for it would be clearly visible. Example:
```
data = {
    "toyota": {
        "wheels": [
            "big",
            "small"
        ],
        "models": [
            {
                "corolla": {
                    "color": {
                        "light": "grey",
                        "dark": "blue"
                    }
                }
            }
        ]
    }
}
```
Would produce a pretty print like this:
```
toyota.wheels.0 = big
toyota.wheels.1 = small
toyota.models.0.corolla.color.light = grey
toyota.models.0.corolla.color.dark = blue
```

Lucky for you, everything is set up for you!

All you need to do is to open `answer.py` fill in the contents for `def serialize(data):`. The function needs to return a flattened dictionary where both keys and values are strings.


Testing:
```
python3 json_serialization.py
```

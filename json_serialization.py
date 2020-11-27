import answer

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

if __name__ == '__main__':
    serialized = answer.serialize(data)
    for k, v in serialized.items():
        print(k, '=', v)

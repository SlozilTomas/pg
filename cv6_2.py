import json

data = [
    {"jmeno" : "Alice", "vek" : 20},
    {"jmeno" : "Bob", "vek" : 25},
    {"jmeno" : "Dave", "vek" : 30},
]


if __name__ == "__main__":

    """
    data[2]["vek"] = 31
    data.append({"jmeno" : "Monika", "vek" : 28})
    
    json_data = json.dumps(data)

    with open("data.json", "w") as fp:
        fp.write(json_data)
    """

    with open("data.json", "r") as fp:
        content = fp.read()
        data2 = json.loads(content)
        print(data2)
        data2.pop(3)
        print(data2)

        
Data = [
    {
        "question": "What is the correct syntax to create an empty dictionary?",
        "options": ["[]", "()", "{}", "dict()"],
        "answer": "{}"
    },
    {
        "question": "How do you add a new key-value pair to a dictionary called `my_dict`?",
        "options": [
            "my_dict.add('key', 'value')",
            "my_dict['key'] = 'value'",
            "my_dict.append({'key': 'value'})",
            "my_dict.insert('key', 'value')"
        ],
        "answer": "my_dict['key'] = 'value'"
    },
    {
        "question": "Which method can you use to safely get a value for a key in a dictionary?",
        "options": ["get()", "find()", "fetch()", "select()"],
        "answer": "get()"
    },
    {
        "question": "What does the `dict.items()` method return?",
        "options": [
            "A list of keys",
            "A list of values",
            "A list of key-value pairs as tuples",
            "Nothing"
        ],
        "answer": "A list of key-value pairs as tuples"
    },
    {
        "question": "What happens if you try to access a key that doesn’t exist using square brackets `[]`?",
        "options": [
            "It returns `None`",
            "It creates the key",
            "It raises a `KeyError`",
            "It prints `undefined`"
        ],
        "answer": "It raises a `KeyError`"
    },
    {
        "question": "Which of the following removes all items from a dictionary?",
        "options": [
            "remove()",
            "clear()",
            "pop()",
            "del()"
        ],
        "answer": "clear()"
    },
    {
        "question": "How can you get all the keys from a dictionary?",
        "options": [
            "dict.keys()",
            "dict.getKeys()",
            "dict.allKeys()",
            "dict.get('keys')"
        ],
        "answer": "dict.keys()"
    },
    {
        "question": "Which method removes a specific key and returns its value?",
        "options": [
            "remove()",
            "pop()",
            "del",
            "clear()"
        ],
        "answer": "pop()"
    },
    {
        "question": "How do you check if a key exists in a dictionary?",
        "options": [
            "`key` in dict",
            "`dict` has `key`",
            "`dict`.exists(`key`)",
            "`dict`.contains(`key`)"
        ],
        "answer": "`key` in dict"
    },
    {
        "question": "What does `dict.update({'x': 5})` do?",
        "options": [
            "Adds 'x': 5 only if it doesn't exist",
            "Replaces all existing values in dict",
            "Adds or updates 'x' with the value 5",
            "Deletes 'x' if it exists"
        ],
        "answer": "Adds or updates 'x' with the value 5"
    }
]

"""
You are free to download and edit the code according to your wish 
To edit the data add the following in pairs:
[ "Your Query",
["List of Responses"]
],
"""
pairs = [
    [
        r"my name is (.*)|hi |hey |hello",
        ["Hello %1, How are you today ?", "Hello", "Hey there"],
    ],
    [r"what is your name ?", ["My name is Hat"]],
    [
        r"how are you ?",
        [
            "I'm doing good How about You ?",
            "Thx for asking I'm Happy",
        ],
    ],
    [
        r"sorry (.*)",
        [
            "Its alright",
            "Its OK, never mind",
        ],
    ],
    [
        r"(.*) fine | i'm (.*) doing good | (.*) happy |(.*) Good |(.*) Gr8 |(.*) Great",
        [
            "Great to hear that, How can I help you?",
        ],
    ],
    [
        r"(.*) sad |(.*) angry |(.*) depressed |(.*) not well |(.*) feel so good |(.*) give up",
        [
            "Oh I'm sorry Let me help you",
        ],
    ],
    [
        r"",
        [
            "Nice to hear that",
            "How can I help you?:)",
        ],
    ],
    [
        r"(.*) age?",
        [
            "I'm a computer program So I cant age",
        ],
    ],
    [
        r"what (.*) want ? |how can you help |what can you do",
        ["You can ask me questions or You can play games or you can look something up"],
    ],
    [
        r"how (.*) health(.*)",
        [
            "I'm a computer program, so I'm always healthy ",
        ],
    ],
    [
        r"(.*) (sports|game) ?",
        [
            "I'm a very big fan of Cricket and Badminton",
        ],
    ],
    [
        r"quit",
        [
            "BBye take care. See you soon :) ",
            "It was nice talking to you. See you soon :)",
        ],
    ],
    [
        r"Thx |Thank you |Thanks a lot",
         ["No Problem", "Anytime", "Your Welcome"]
         ],
    [
        r"who (.*) you ",
         ["I was coded by Hat1412 in python To know more type help"]
         ],
    [
        "(.*) hobbies|(.*) free time", 
    ["Youtube", "PLaying Video Games"]
    ],]

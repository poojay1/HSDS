#vocab_helpers.py

strong_negation = ["नहीं", "कभी नहीं", "कोई नहीं", "कुछ नहीं", "न तो", "कहीं नहीं"]

strong_affirmatives =  ["हाँ", "हमेशा", "सब", "कोई", "हर", "सबको", "हर जगह", "कभी"]

punctuation = ["?", "!", "..."]

intensifiers = ["आश्चर्यजनक", "भयानक", "नंगे", "खूनी", "पागल", "डरावना",
                "विशाल रूप से", "विशेष रूप से", "अपवाद", "अत्यधिक", "अत्यंत",
                "असाधारण", "शानदार", "डरावना", "कमबख्त", "पूरी तरह से",
                "पवित्र", "अविश्वसनीय रूप से", "बेहद", "शाब्दिक", "शायद", "मामूली", "सबसे अधिक",
                "अपमानजनक", "असाधारण रूप से", "कीमती", "काफी", "मूल रूप से", "बल्कि",
                "वास्तव में", "उल्लेखनीय", "दाएं", "बीमार", "हड़ताली", "सुपर", "सर्वोच्च",
                "आश्चर्यजनक रूप से", "बहुत", "भयानक", "भी", "पूरी तरह से", "असामान्य रूप से",
                "असामान्य रूप से", "सत्य", "बहुत", "दुष्ट"]

interjections = ["ओह", "वाह", "आह", "अहम", "अ", "बाम", "ब्लाह", "बिंगो", "बू", "ब्रावो",
                 "चीयर्स", "बधाई", "बधाई", "दुह", "एह", "जी", "हे", "हम्म",
                 "हुह", "हरे", "ओह", "ओह प्रिय", "ओह माय", "ओह वेल", "ओप्स", "आउच", "ओउ",
                  "उह", "उह-हुह", "उघ", "अच्छा", "वाह", "हाँ", "यिक्स", "यो"]



emotiocons_to_emojis = {
    ':{': 'ðŸ˜ž', ':c)': 'ðŸ˜ƒ', ':-||': 'ðŸ˜ž', ':(': 'ðŸ˜ž', ':-))': 'ðŸ˜‚', 'dx': 'ðŸ˜§',
    ':-d': 'ðŸ˜€', '))': 'ðŸ˜‚', ':-*': 'ðŸ˜—', ':d': 'ðŸ˜€', ":'((": 'ðŸ˜¢', ':â€‘Ãž': 'ðŸ˜›',
    ':-[': 'ðŸ˜ž', ':-<': 'ðŸ˜ž', ":'-)": 'ðŸ˜‚', ":'-(": 'ðŸ˜¢', ':Ã¾': 'ðŸ˜›', ':â€‘,': 'ðŸ˜‰',
    '=]': 'ðŸ˜ƒ', '>:[': 'ðŸ˜ž', ':Ãž': 'ðŸ˜›', ':â€‘|': 'ðŸ˜', 'd8': 'ðŸ˜§', 'O:â€‘)': 'ðŸ˜ƒ',
    ';)': 'ðŸ˜‰', ':â€‘b': 'ðŸ˜›', ":')": 'ðŸ˜‚', '>:(': 'ðŸ˜ž', '8-0': 'ðŸ˜²', ';-)': 'ðŸ˜ƒ',
    ':o)': 'ðŸ˜²', ':â€‘Ã¾': 'ðŸ˜›', ':o': 'ðŸ˜²', ':-)': 'ðŸ˜ƒ', ':-o': 'ðŸ˜²', '(-:': 'ðŸ˜ƒ',
    ';d': 'ðŸ˜‰', ':))': 'ðŸ˜‚', ':x': 'ðŸ˜—', ';^)': 'ðŸ˜‰', '(:': 'ðŸ˜ƒ', ':$': 'ðŸ˜³', 'd;': 'ðŸ˜§',
    'd:<': 'ðŸ˜§', ':O': 'ðŸ˜²', ':-c': 'ðŸ˜ž', 'xoxo': 'ðŸ’‹', ':â€‘p': 'ðŸ˜›', '8)': 'ðŸ˜ƒ',
    '0:)': 'ðŸ˜ƒ', '0;^)': 'ðŸ˜ƒ', ':@': 'ðŸ˜ž', 'xx': 'â™¥', ':-}': 'ðŸ˜ƒ', '::': 'ðŸ˜•', ';â€‘)': 'ðŸ˜‰',
    'x': 'â™¥', ':-]': 'ðŸ˜ƒ', ':*': 'ðŸ˜—', ':-(': 'ðŸ˜ž', ']]': 'ðŸ˜‚', '\\m/': 'ðŸŽ¶', '*)': 'ðŸ˜‰',
    ':}': 'ðŸ˜ƒ', ':)': 'ðŸ˜ƒ', '=/': 'ðŸ˜•', ';;': 'ðŸ˜•', '>:o': 'ðŸ˜²', '=d': 'ðŸ˜€', ':L': 'ðŸ˜•',
    ':((': 'ðŸ˜¢', '=3': 'ðŸ˜€', '0:â€‘)': 'ðŸ˜ƒ', ':-O': 'ðŸ˜²', ':<': 'ðŸ˜ž', 'd=': 'ðŸ˜§', '0:3': 'ðŸ˜ƒ',
    ';]': 'ðŸ˜‰', ';p': 'ðŸ˜›', ':P': 'ðŸ˜›', 'xâ€‘p': 'ðŸ˜›', '=)': 'ðŸ˜ƒ', 'O:)': 'ðŸ˜ƒ', ':p': 'ðŸ˜›',
    'x-d': 'ðŸ˜€', '8-)': 'ðŸ˜ƒ', ':S': 'ðŸ˜•', "d-':": 'ðŸ˜§', ':c': 'ðŸ˜ž', ':|': 'ðŸ˜', '0:â€‘3': 'ðŸ˜ƒ',
    '>:p': 'ðŸ˜›', '>:\\': 'ðŸ˜•', ':/': 'ðŸ˜•', ':]': 'ðŸ˜ƒ', ':3': 'ðŸ˜ƒ', ':b': 'ðŸ˜›', ';â€‘]': 'ðŸ˜‰',
    '8d': 'ðŸ˜€', 'xo': 'ðŸ’‹', '>:/': 'ðŸ˜•', '((': 'ðŸ˜¢', ':[': 'ðŸ˜ž', ':â€‘/': 'ðŸ˜•', ':->': 'ðŸ˜ƒ',
    ';(': 'ðŸ˜ž', '=))': 'ðŸ˜‚', '=\\': 'ðŸ˜•', ":'(": 'ðŸ˜¢', '*-)': 'ðŸ˜‰', ':\\': 'ðŸ˜•', 'xd': 'ðŸ˜€',
    'xp': 'ðŸ˜›', ':-3': 'ðŸ˜ƒ', '=l': 'ðŸ˜•', ':^)': 'ðŸ˜ƒ', '=p': 'ðŸ˜›', ':>': 'ðŸ˜ƒ', '8-d': 'ðŸ˜€',
    ':-0': 'ðŸ˜²', 'd:': 'ðŸ˜›', ':â€‘.': 'ðŸ˜•'
}

implicit_emoticons = {
    ":)": "खुले मुंह से मुस्कुराते हुए चेहरे",
    "=)": "खुले मुंह से मुस्कुराते हुए चेहरे",
    ":-)": "खुले मुंह से मुस्कुराते हुए चेहरे",
    ";-)": "झुर्रियों वाला चेहरा",
    "(:": "खुले मुंह से मुस्कुराते हुए चेहरे",
    "(-:": "खुले मुंह से मुस्कुराते हुए चेहरे",
    "(':": "खुले मुंह से मुस्कुराते हुए चेहरे",
    "='d": "प्रसन्न चेहरा",
    ":d": "मुस्कुराते हुए चेहरे",
    ";d": "मुस्कुराते हुए चेहरे",
    "xd": "मुस्कुराते हुए चेहरे",
    "dx": "मुस्कुराते हुए चेहरे",
    ":))": "खुशी के आँसू के साथ चेहरा",
    ":-))": "खुशी के आँसू के साथ चेहरा",
    "=))": "खुशी के आँसू के साथ चेहरा",
    ";)": "झुर्रियों वाला चेहरा",
    ":x": "खुले मुंह से मुस्कुराते हुए चेहरे दिल के आकार की आंखों के साथ",
    "p": "फंसे हुए जीभ के साथ चेहरा",
    ":p": "फंसे हुए जीभ के साथ चेहरा",
    ";p": "फंसे हुए जीभ के साथ चेहरा",
    ":-p": "फंसे हुए जीभ के साथ चेहरा",
    ":(": "निराश चेहरा",
    ":-(": "निराश चेहरा",
    ";(": "निराश चेहरा",
    ";;": "भ्रमित चेहरा",
    "::": "भ्रमित चेहरा",
    ":'(": "रोना चेहरा",
    ":((": "रोना चेहरा",
    ":/": "व्यंग्यात्मक दास",
    ":|": "तटस्थ चेहरा",
    ":3": "प्यारा चेहरा",
    "x": "मोहब्बत",
    "xx": "मोहब्बत",
    "xoxo": "आलिंगन और चुंबन",
    "xo": "आलिंगन और चुंबन",
    ":o": "खुले मुंह के साथ चेहरा",
    ":-o": "खुले मुंह के साथ चेहरा",
    "\m/": "धातु संगीत"
}

# Processed from https://en.wikipedia.org/wiki/List_of_emoticons
wikipedia_emoticons = {
    ':-)': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    '8-)': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    ':]': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    ':)': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    ':-3': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    ':->': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    ':-}': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    '(-:': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    "(:": "खुले मुंह से मुस्कुराते हुए चेहरे",
    ':-]': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    '=]': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    '=)': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    ':3': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    ':c)': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    ':^)': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    ':}': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    ':>': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    '8)': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    '=d': 'मुस्कुराते हुए चेहरे',
    ":d": "मुस्कुराते हुए चेहरे",
    'xd': 'मुस्कुराते हुए चेहरे',
    '8-d': 'मुस्कुराते हुए चेहरे',
    '8d': 'मुस्कुराते हुए चेहरे',
    ':-d': 'मुस्कुराते हुए चेहरे',
    '=3': 'मुस्कुराते हुए चेहरे',
    'x-d': 'मुस्कुराते हुए चेहरे',
    ':-))': 'खुशी के आँसू के साथ चेहरा',
    ':))': 'खुशी के आँसू के साथ चेहरा',
    '))': 'खुशी के आँसू के साथ चेहरा',
    ']]': 'खुशी के आँसू के साथ चेहरा',
    '=))': 'खुशी के आँसू के साथ चेहरा',
    ':<': 'निराश चेहरा',
    ':(': 'निराश चेहरा',
    ':@': 'निराश चेहरा',
    ':-<': 'निराश चेहरा',
    '>:[': 'निराश चेहरा',
    ':[': 'निराश चेहरा',
    ':{': 'निराश चेहरा',
    ':c': 'निराश चेहरा',
    '>:(': 'निराश चेहरा',
    ':-c': 'निराश चेहरा',
    ':-(': 'निराश चेहरा',
    ':-||': 'निराश चेहरा',
    ':-[': 'निराश चेहरा',
    ":-(": "निराश चेहरा",
    ";(": "निराश चेहरा",
    ";;": "भ्रमित चेहरा",
    "::": "भ्रमित चेहरा",
    ":'-(": 'रोना चेहरा',
    ":'(": 'रोना चेहरा',
    ":'((": 'रोना चेहरा',
    ":((": 'रोना चेहरा',
    "((": 'रोना चेहरा',
    ":'-)": 'खुशी के आँसू के साथ चेहरा',
    ":')": 'खुशी के आँसू के साथ चेहरा',
    'd=': 'पीड़ा का चेहरा',
    'd:<': 'पीड़ा का चेहरा',
    'd8': 'पीड़ा का चेहरा',
    'd;': 'पीड़ा का चेहरा',
    'dx': 'पीड़ा का चेहरा',
    "d-':": 'पीड़ा का चेहरा',
    ':-o': 'आश्चर्यचकित चेहरा',
    ':o)': 'आश्चर्यचकित चेहरा',
    '8-0': 'आश्चर्यचकित चेहरा',
    ':-O': 'आश्चर्यचकित चेहरा',
    ':O': 'आश्चर्यचकित चेहरा',
    ':-0': 'आश्चर्यचकित चेहरा',
    ':o': 'आश्चर्यचकित चेहरा',
    '>:o': 'आश्चर्यचकित चेहरा',
    ':x': 'चुंबन चेहरा',
    ':*': 'चुंबन चेहरा',
    ':-*': 'चुंबन चेहरा',
    'xx': 'काला दिल सूट',
    'x': 'काला दिल सूट',
    'xoxo': 'चुम्मन के निशान',
    'xo': 'चुम्मन के निशान',
    ':-,': 'झुर्रियों वाला चेहरा',
    ';^)': 'झुर्रियों वाला चेहरा',
    ';d': 'झुर्रियों वाला चेहरा',
    ';-]': 'झुर्रियों वाला चेहरा',
    ';]': 'झुर्रियों वाला चेहरा',
    '*)': 'झुर्रियों वाला चेहरा',
    ';-)': 'झुर्रियों वाला चेहरा',
    '*-)': 'झुर्रियों वाला चेहरा',
    ';)': 'झुर्रियों वाला चेहरा',
    'x-p': 'फंसे हुए जीभ के साथ चेहरा',
    '=p': 'फंसे हुए जीभ के साथ चेहरा',
    'd:': 'फंसे हुए जीभ के साथ चेहरा',
    ':p': 'फंसे हुए जीभ के साथ चेहरा',
    ':b': 'फंसे हुए जीभ के साथ चेहरा',
    ':-b': 'फंसे हुए जीभ के साथ चेहरा',
    ':-p': 'फंसे हुए जीभ के साथ चेहरा',
    ';p': 'फंसे हुए जीभ के साथ चेहरा',
    ':P': 'फंसे हुए जीभ के साथ चेहरा',
    '>:p': 'फंसे हुए जीभ के साथ चेहरा',
    'xp': 'फंसे हुए जीभ के साथ चेहरा',
    '>:/': 'भ्रमित चेहरा',
    ':L': 'भ्रमित चेहरा',
    '=\\': 'भ्रमित चेहरा',
    ':S': 'भ्रमित चेहरा',
    ':-.': 'भ्रमित चेहरा',
    '=/': 'भ्रमित चेहरा',
    '>:\\': 'भ्रमित चेहरा',
    ':-/': 'भ्रमित चेहरा',
    ':\\': 'भ्रमित चेहरा',
    '=l': 'भ्रमित चेहरा',
    ':/': 'भ्रमित चेहरा',
    ':|': 'तटस्थ चेहरा',
    ':-|': 'तटस्थ चेहरा',
    ':$': 'धोया चेहरा',
    '0;^)': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    'O:-)': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    '0:3': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    '0:-)': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    '0:)': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    '0:-3': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    'O:)': 'खुले मुंह से मुस्कुराते हुए चेहरे',
    "\m/": "एकाधिक संगीत नोट्स"
}
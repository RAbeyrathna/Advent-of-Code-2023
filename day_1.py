calibration_strings = [
    "fivepqxlpninevh2xxsnsgg63pbvdnqptmg",
    "eight8zlctbmsixhrvbpjb84nnmlcqkzrsix",
    "hkxqfrqmsixfplbkpkdfzzszjxmdjtdkjlprrvr3gghlrqckqtbng",
    "zkjkctxvssix1dqb22five",
    "4dtlmkfnm",
    "four539tkqrc",
    "blxqb7onetvmfjlvglrnbtdonegfourfour",
    "lqzrclnlzrvdstgtoneseven1xrvdchn29",
    "tczmtfkqhthreetwo7five",
    "kncvqpzdtfs7",
    "6seveneighttwonine2",
    "sixbfgxndseven9nvzr6ftsqb1",
    "ddgjgcrssevensix37twooneightgt",
    "zclvhfz91zbdkrreightbzqttdxrone",
    "five18twofiveclqqsrsfdbrt",
    "ninedflcfblvjhr3",
    "32eightnmlv5lgbckz",
    "nine7xqz81dtpld",
    "2tmbddjl9cgcrvnrpgl",
    "5twofivedlk1pfjjmctjh",
    "nvcchgjnine9sixtwompfrp",
    "685",
    "54two7twobsfpkxjninefoureight",
    "fgsvpxcx4zzxfqdkssixgbssrqmnpz9threethreefour",
    "three3sixnine38bprqqkpdr6seven",
    "xgmc3sixthree1",
    "3eight2twojqsvbtftp",
    "six7sixtwos1mhzfpzmhfcslrmfive",
    "bmxmxzldtngrgbt538jzqvjlrrc4",
    "sevenxqzcrgzvfiveggxlxf4fiveppvrxjkdk9",
    "one8six",
    "fourdlhgvx1onesix",
    "onelpbxfnjm28gjjs5",
    "pdb69six6cdxmxxbfour5five",
    "eightjndqhjzv43five631",
    "9fourldr92eight",
    "three1sevensrxzlnxrnine7four",
    "eightfive4bldzgtpvslgkrmlmkftpone",
    "22357fourone6",
    "sixrzhgvzsjsix9dbldsevenfivedtnbkjjxfc",
    "mcgfpfh1three",
    "ninetwo1",
    "sqgtvmcvbfsslsdnine19three1two",
    "f5nine7six",
    "1sbggj",
    "5eight56342h",
    "3onezdfsvngvjg4fqeight",
    "sixncfrkbqthreeqsbpvspjt4",
    "fjseventwo4k",
    "five8five",
    "4oneone14",
    "prpnzmnsjsfivetdrqpt54",
    "2threefour2fourrkkndqzq",
    "lreightfourfour12sfjkjmbntkgfjv",
    "sixfour93",
    "eightfivetwo1one",
    "three5eightjk5twothreeseven",
    "tz62twofivetclnxfp8dhsxzgpxhsfhx",
    "fivefivecrjhmbrk6three",
    "58fiveseven3five",
    "nine4six6hqmqqqbktkfvmb",
    "7five8k",
    "5kbfjmqppvrbjdkc",
    "hkpchj2gknjhvc",
    "7twosix",
    "2kltwo",
    "six6vlmhdmvtdsix",
    "xqtpnglkktvpktfive1",
    "9one91",
    "vbrcfmjeight4qmtzmpqhsninejdmvzpdtpq2",
    "3eightzdcrvqeightl7nsbpdrczdrnine",
    "nine6hkfeight9",
    "73pqqqsixone7bvl",
    "1threeeight9six",
    "46one9smxbqzrppr56six",
    "njoneight27fourthreevtxf51",
    "fivekbdfkfjk2",
    "two1lxdpqtq2jcl4q",
    "foursevenbtenzeightfivesixpsxn3",
    "fournine5twofour2",
    "txztpbmvb1sevenqtwo",
    "tq7qtwoninevbfmj",
    "stepicwebonem1five",
    "8five1k",
    "45qppqtl4cczdfour5",
    "1three8fourkbcbnbmxmtjkxvtbdcvwzvgqg",
    "twopxwqtwocbqcnl59vvhcxgzzv5clvqv6",
    "7onelrgw1pgkmghnmlldfvbsvtnsqzljm9",
]

list_numbers = (
    "0123456789"  # Digits from 1 - 9 in string format to compare within the loop
)
total = 0  # Initializes inital total

for calibration_string in calibration_strings:  # Checks each string provided
    calibration_value = ""  # Initalizes empty string to be appended
    for char in calibration_string:  # Checks each individual string character
        if char in list_numbers:
            calibration_value = (
                calibration_value + char
            )  # Concatenates the current character if it is present in the list_numbers variable
        else:
            continue
    if (
        int(calibration_value) > 2
    ):  # Takes only the first and last digits with value is larger than 2 digits
        first_char = calibration_value[0]
        last_char = calibration_value[-1]
        calibration_value = ""
        calibration_value = first_char + last_char
    print(f"Calibration value is: {calibration_value}")
    total += int(calibration_value)
print(f"Sum of all calibration values is {total}")

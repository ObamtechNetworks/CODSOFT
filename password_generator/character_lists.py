#!/usr/bin/python3
"""This module serves as a database that holds the list"""


# list of characters
letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
        'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

# list of numbers
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# list of symbols
symbols = [
        '!', '#', '$', '%', '&', '(', ')', '*',
        '+', '@', '^' '-', '+', '=', '_', ']', '['
        ]

# password logo
logo = """
d8888b.  .d8b.  .d8888. .d8888. db   d8b   db  .d88b.  d8888b. d8888b.
88  `8D d8' `8b 88'  YP 88'  YP 88   I8I   88 .8P  Y8. 88  `8D 88  `8D
88oodD' 88ooo88 `8bo.   `8bo.   88   I8I   88 88    88 88oobY' 88   88
88~~~   88~~~88   `Y8b.   `Y8b. Y8   I8I   88 88    88 88`8b   88   88
88      88   88 db   8D db   8D `8b d8'8b d8' `8b  d8' 88 `88. 88  .8D
88      YP   YP `8888Y' `8888Y'  `8b8' `8d8'   `Y88P'  88   YD Y8888D'


 d888b  d88888b d8b   db d88888b d8888b.  .d8b.  d888888b  .d88b.  d8888b.
88' Y8b 88'     888o  88 88'     88  `8D d8' `8b `~~88~~' .8P  Y8. 88  `8D
88      88ooooo 88V8o 88 88ooooo 88oobY' 88ooo88    88    88    88 88oobY'
88  ooo 88~~~~~ 88 V8o88 88~~~~~ 88`8b   88~~~88    88    88    88 88`8b
88. ~8~ 88.     88  V888 88.     88 `88. 88   88    88    `8b  d8' 88 `88.
 Y888P  Y88888P VP   V8P Y88888P 88   YD YP   YP    YP     `Y88P'  88   YD
"""

welcome_message = """
      Hello and welcome to this PASSWORD GENERATOR APP
      This is a simple yet robust and highly secured
      PASSWORD GENERATOR. HOW TO USE?
      You will be prompted to:

      --> input your desired number of letters for your password
      --> input desired number of symbols
      --> input desired number of digits

      Then your password is computed with THE TIME it was generated
      You have the options to:
      --> REVEAL PASSWORD or NOT
      --> Password is automatically saved to a TXT file for later use
      --> Timestamps of when it was generated is also appended together
      with the password

      ENJOY and GIVE FEEDBACK ABOUT THIS APP
      Programmed by: Bamidele Michael Ipadeola
      """

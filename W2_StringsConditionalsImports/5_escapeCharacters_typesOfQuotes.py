
# ********** Lec 5 [ Escape Characters and Types of Quotes ]

print ( 'Hey What\'s Up?')
print ( 'Hey everyone\nThis is me')
print ( f"This is amazon's app" )
print ( r"This \nis amazon's app" )  #? \n wont work here
#? Escape sequences like \n, \t, \\ are taken literally, not interpreted.
#? rule: raw strings cannot end with a single backslash \.


#? Use '''    ''' to store a multiline string/comments
#? Use """    """ to store a multiline string/comments
#? Note: if we use a \ in multiline comment, Python will treat it as string

x = '''first line
second line
third line
''' 


'''
This looks like a multiline comment
But actually it's just a multiline string
that is not assigned to any variable.
'''



# Escape Sequence                 Meaning
# -------------------------------- ------------------------------
# \newline                        Backslash and newline ignored
# \\                              Backslash (\)
# \'                              Single quote (')
# \"                              Double quote (")
# \a                              ASCII Bell (BEL)
# \b                              ASCII Backspace (BS)
# \f                              ASCII Formfeed (FF)
# \n                              ASCII Linefeed (LF)
# \r                              ASCII Carriage Return (CR)
# \t                              ASCII Horizontal Tab (TAB)
# \v                              ASCII Vertical Tab (VT)
# \ooo                            Character with octal value ooo
# \xhh                            Character with hex value hh

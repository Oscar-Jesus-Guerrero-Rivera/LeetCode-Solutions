"""
3280_convert_date_to_binary

You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.
date can be written in its binary representation obtained by converting year, month, and day to 
their binary representations without any leading zeroes and writing them down in year-month-day 
format.

Return the binary representation of date.

Example:

Input: date = "2080-02-29"
Output: "100000100000-10-11101"
"""

def convertDateToBinary( date):
    """
    :type date: str
    :rtype: str
    """
    return '-'.join(bin(int(part))[2:] for part in date.split("-"))

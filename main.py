"""Bitmap Message
displays a text message according to the provided bitmap image
"""

import sys

# https://inventwithpython.com/bitmapworld.txt
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Bitmap Massage')
print("Enter the message to display with the bitmap")

message = input("> ")
if message == "":
    sys.exit()

# loop iver each line in the bitmap
for line in bitmap.splitlines():
    # loop over each char in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # print an empty space since theres a space in the bitmap
            print(' ', end='')
        else:
            # print a char form the mess
            print(message[i % len(message)], end='')
    print() # prints a newline

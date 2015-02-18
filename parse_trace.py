#!/usr/bin/python3.4
# The MIT License (MIT)
#
# Copyright (c) 2015 Todor Mitev
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import getopt
import sys
# CUSTOM IMPORTS
import parsetrace
import parsetrace.cli.messages as messenger


def main():
    global verbose
    file = ''

    try:
        options, args = getopt.getopt(sys.argv[1:], "f:hv", ["file=", "help="])
    except getopt.GetoptError as err:
        # print help information and exit:
        messenger.print_exception(err)
        messenger.print_help()
        sys.exit(2)

    for option, value in options:
        if option == "-v":
            verbose = True
        elif option in ("-h", "--help"):
            messenger.print_help()
            sys.exit()
        elif option in ("-f", "--file"):
            file = value

    print(file)

if __name__ == "__main__":
    main()

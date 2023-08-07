#!/usr/bin/env python

import sys
from xpycommon import ValNameDesc, ValNameDescs
from xpycommon.common import upgrade
from xpycommon.at_cmd import AtCode, AtCodes
from xpycommon.log import Logger, DEBUG
from xpycommon.ui import red

logger = Logger(__name__, DEBUG, filename='./log')


# class Codes(ValNameDescs):
#     a = Code(1)
#     b = Code(2)
#     c = Code('sadf')

class ExtAtCodes(AtCodes):
    t = AtCode('123')
    


def main():
    """"""
    print(isinstance(ExtAtCodes.t, AtCode))
    print(isinstance(ExtAtCodes.t, str))
    print(ExtAtCodes.ss)
    # print(AtCodes.mro())
    # print(AtCodes.OK)
    # print(type(AtCodes.OK))
    # print(AtCodes.OK.result_code_types)
    # print(AtCodes.OK.name)
    # print(AtCodes.OK.desc)
    # print(AtCodes.OK + 'asdf')
    # print(AtCodes['OK'])
    # print(AtCodes['OK'].name)
    # print(AtCodes.OK.encode())



if __name__ == '__main__':
    main()

#!/usr/bin/evn python3


import logging
import amodule

logging.basicConfig(level=logging.NOTSET)

amodule.main()

# Note if we import apackage before calling basicConfig or setting up
# a handler then we won't see the debug message
import apackage

apackage.main()

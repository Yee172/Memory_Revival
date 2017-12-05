#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2017/12/03'


import sys
PATH = sys.path[0][:-4]
sys.path.append(PATH)
from src.Func import *


win = MainWin()
sys.exit(app.exec_())

#!/usr/bin/env python3
from bugfinder.apps.monitor import fire_monitor
from bugfinder.asrsummary import save_record, calculate_summary
from typing import Dict, List, Optional, Set, Tuple

import sys
import os
from bugfinder.utils import is_in_china
import codefast as cf


def dbinstall():
    """install database"""
    is_cn = is_in_china()
    pypi = "https://pypi.douban.com/simple" if is_cn else "https://pypi.org/simple"
    cmd = 'python3 -m pip install {} -i {}'.format(' '.join(sys.argv[1:]), pypi)
    os.system(cmd)


def transferfile():
    files = " ".join(sys.argv[1:])
    cmd = f"curl -s -o /tmp/transfer.pl https://host.ddot.cc/transfer.pl && perl /tmp/transfer.pl {files} && rm /tmp/transfer.pl"
    try:
        resp = os.system(cmd)
    except Exception as e:
        print(e)


def syncfile():
    file = sys.argv[1]
    try:
        # still file.ddot
        cmd = f"curl -s https://file.ddot.cc/gofil|bash -s '{file}'"
        resp = os.system(cmd)
        print(resp)
    except FileNotFoundError as e:
        print(e)


def esyncfile():
    """sync file with encryption"""
    file = sys.argv[1]
    try:
        cmd = f"curl -s https://host.ddot.cc/gofile|bash -s '{file}'"
        resp = os.system(cmd)
        print(resp)
    except FileNotFoundError as e:
        print(e)


def osssync():
    """sync file with encryption"""
    file = sys.argv[1]
    try:
        cmd = f"curl -s https://host.ddot.cc/oss|bash -s {file}"
        resp = os.system(cmd)
        print(resp)
    except FileNotFoundError as e:
        print(e)


def justdemo():
    print("just demo")


def qgrep():
    cf.shell('grep {} /log/serving/serving.log'.format(' '.join(sys.argv[1:])))


exported = ['fire_monitor', 'transferfile', 'dbinstall', 'syncfile', 'esyncfile', 'osssync', 'save_record', 'calculate_summary', 'qgrep']

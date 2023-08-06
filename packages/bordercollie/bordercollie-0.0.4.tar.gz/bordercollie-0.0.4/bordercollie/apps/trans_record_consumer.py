#!/usr/bin/env python3
import json
import os
import random
import re
import sqlite3
import sys
from collections import defaultdict
from functools import reduce
from typing import Callable, Dict, List, Optional, Set, Tuple, Union

import codefast as cf
import joblib
import nsq
import numpy as np
import pandas as pd
from rich import print

from bordercollie.auth import auth

db = sqlite3.connect('/home/x03/Dropbox/datasets/sqlite/transcription_records.db')
db.execute(
    'create table if not exists trans_records (md5 text primary key, msg text)'
)


def persist_data(message):
    msg = json.loads(message.body)
    md5 = cf.md5sum(str(msg))
    db.execute(
        'insert into trans_records (md5, msg) values (?, ?) on conflict (md5) do nothing',
        (md5, str(msg)))
    db.commit()
    cf.info('data {} was persisted'.format(str(msg)))
    return True


if __name__ == '__main__':
    r = nsq.Reader(message_handler=persist_data,
                   lookupd_http_addresses=[auth.nsqlookupd],
                   topic='transcript_record',
                   channel='persist',
                   lookupd_poll_interval=3,
                   max_in_flight=10)
    nsq.run()

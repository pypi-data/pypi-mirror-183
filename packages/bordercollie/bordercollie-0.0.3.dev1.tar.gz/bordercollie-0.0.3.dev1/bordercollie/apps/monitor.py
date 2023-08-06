#!/usr/bin/env python3
from typing import Callable, Dict, List, Optional, Set, Tuple, Union

import codefast as cf
import fire

from bordercollie.utils import post_to_lark
import pandas as pd

def nsqtopic(webhook: str, max_depth: int = 100):
    """nsq topic monitor"""
    js = cf.net.get('http://localhost:4151/stats?format=json').json()
    messages = []

    for j in js['topics']:
        channel_list = j['channels']
        for chan in channel_list:
            depth = int(chan['depth'])
            name = chan['channel_name']
            if depth > max_depth:
                messages.append('NSQ channel {} 当前队列长度为 {}，请留意系统状态。'.format(name, depth))
    if messages:
        cur_time = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
        messages = [cur_time] + messages
        msg = '\n'.join(messages)
        post_to_lark(webhook, msg)

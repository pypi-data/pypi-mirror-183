#!/usr/bin/env python3
import fire
import re
from typing import Callable, Dict, List, Optional, Set, Tuple, Union
import time
import codefast as cf
from codefast.patterns.pipeline import Component, Pipeline
import redis
from codefast.io.osdb import osdb
db = osdb('/tmp/logtracker')


def post_to_telegram(msg: str):
    try:
        from ojbk.auth import auth 
        cf.net.post(auth.telegram_api, json={'channel': 'cowbark', 'message': msg})
    except Exception as e:
        print(e)


class NewErrorCollector(Component):
    def __init__(self) -> None:
        super().__init__()
        self.print_log = False

    def process(self, log_path: str) -> List[str]:
        lns = []
        with open(log_path, 'r') as f:
            pre = ''
            for line in f:
                if 'ERROR' in line:
                    start_mark = True
                if 'INFO' in line:
                    start_mark = False

                if start_mark:
                    pre += line

                if not start_mark:
                    if pre and (pre not in lns):
                        pre = re.sub(r'\[\d+m', '', pre)
                        if not db.exists(cf.md5sum(pre)):
                            lns.append(pre)
                    pre = ''
        return lns


class Post(Component):
    def __init__(self) -> None:
        super().__init__()
        self.print_log = False

    def process(self, errors: List[str]) -> List[str]:
        for e in errors:
            ex = cf.shell('hostname') + ' ' + e
            post_to_telegram(ex)
        return errors


class MarkPosted(Component):
    def __init__(self) -> None:
        super().__init__()
        self.print_log = False

    def process(self, errors: List[str]) -> List[str]:
        for e in errors:
            db.set(cf.md5sum(e), e)
        return errors


def logtrack(log_path: str = '/tmp/cf.log'):
    pass

def looplogtrack(log_path: str = '/tmp/cf.log', interval: int = 60):
    p = Pipeline([NewErrorCollector(), Post(), MarkPosted()])
    while True:
        p.process(log_path)
        time.sleep(interval)


if __name__ == '__main__':
    fire.Fire(looplogtrack)

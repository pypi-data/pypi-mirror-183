import datetime
import time
from threading import Thread

import objgraph


class Handlers:
    MEMORY_TYPE_NUM = 'MEMORY_TYPE_NUM'
    MEMORY_TYPE_NUM_GROWTH = 'MEMORY_TYPE_NUM_GROWTH'
    MEMORY_STACK = 'MEMORY_STACK'
    MEMORY_TOP_GRAPH = 'MEMORY_TOP_GRAPH'


class MemoryLogger(Thread):

    def __init__(self, log_file_name, duration: int = 5):
        super().__init__()
        self.daemon = True

        # 日志文件
        if not log_file_name:
            self.log_file_name = f'log/memory.log'
        else:
            self.log_file_name = f'log/{log_file_name}_debug.log'
        self.log_file = open(self.log_file_name, 'a')

        # 间隔时间
        if not isinstance(duration, int):
            raise Exception('duration must be type int!')
        if not duration:
            self.duration = 5
        else:
            self.duration = duration

        self.targets = []
        self.handlers = []

    def add_target(self, target):
        if target not in [Handlers.MEMORY_TYPE_NUM, Handlers.MEMORY_TYPE_NUM_GROWTH, Handlers.MEMORY_STACK, Handlers.MEMORY_TOP_GRAPH]:
            raise Exception('指标类型不存在!')
        self.targets.append(target)
        if target == Handlers.MEMORY_TYPE_NUM:
            self.handlers.append(MemoryNumHandler(self.log_file))
        if target == Handlers.MEMORY_TYPE_NUM_GROWTH:
            self.handlers.append(MemoryNumGrowthHandler(self.log_file))
        if target == Handlers.MEMORY_STACK:
            self.handlers.append(MemoryHeapHandler(self.log_file))
        if target == Handlers.MEMORY_TOP_GRAPH:
            self.handlers.append(MemoryTopGraphHandler(self.log_file))


    def run(self):
        if not self.handlers:
            raise Exception('Error: no handler exists!')
        while True:
            for handler in self.handlers:
                handler.handle()
            time.sleep(self.duration)


class MemoryNumHandler(object):

    def __init__(self, log_file):
        self.log_file = log_file

    def handle(self):
        self.log_file.write(f'=== types: {datetime.datetime.now()} === \t\n')
        objgraph.show_most_common_types(file=self.log_file)
        self.log_file.flush()


class MemoryNumGrowthHandler(object):

    def __init__(self, log_file):
        self.log_file = log_file

    def handle(self):
        self.log_file.write(f'=== increments: {datetime.datetime.now()} === \t\n')
        objgraph.show_growth(file=self.log_file)
        self.log_file.flush()


class MemoryHeapHandler(object):

    def __init__(self, log_file):
        from guppy import hpy
        self.log_file = log_file
        self.hpy = hpy()

    def handle(self):
        self.log_file.write(f'=== heap: {datetime.datetime.now()} === \t\n')
        heap = self.hpy.heap()
        self.log_file.write(f'{heap.__str__()} \t\n')
        self.log_file.flush()


class MemoryTopGraphHandler(object):

    def __init__(self, log_file):
        from guppy import hpy
        self.log_file = log_file
        self.hpy = hpy()

    def handle(self):
        gth = objgraph.growth(limit=20)
        for gt in gth:
            objgraph.show_backrefs(objgraph.by_type(gt[0])[0], max_depth=10, too_many=5,
                                   filename="log/dots/%s_backrefs.dot" % gt[0])
            objgraph.show_refs(objgraph.by_type(gt[0])[0], max_depth=10, too_many=5,
                               filename="log/dots/%s_refs.dot" % gt[0])
            objgraph.show_chain(
                objgraph.find_backref_chain(objgraph.by_type(gt[0])[0], objgraph.is_proper_module),
                filename="log/dots/%s_chain.dot" % gt[0]
            )

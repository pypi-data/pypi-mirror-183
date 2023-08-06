import time

import debug_util


class Int:

    def __init__(self, value):
        self.value = value


def new_int(i1, rs1):
    a = Int(i1)
    rs1.append(a)


if __name__ == '__main__':
    ml = debug_util.memory_logger(log_file_name='test', duration=2)
    ml.add_target(debug_util.handlers.MEMORY_TYPE_NUM)
    ml.add_target(debug_util.handlers.MEMORY_TYPE_NUM_GROWTH)
    ml.add_target(debug_util.handlers.MEMORY_STACK)
    ml.start()
    rs = []
    i = 0
    while True:
        if i % 1000000 == 0:
            time.sleep(2)
        if i == 10000000:
            break
        new_int(i, rs)
        i += 1

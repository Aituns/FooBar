from json.encoder import INFINITY
from os import major
from tempfile import tempdir


def solution(l):

    print(lambda l:[int(i) for i in l.split('.')])

    return sorted(l, key=lambda l:[int(i) for i in l.split('.')])      

print()
print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
print()

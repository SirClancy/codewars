#! /usr/bin/python
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

print maskify("34234234234234")


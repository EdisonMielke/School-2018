import re
date_pat = re.compile("""
# European style
(?P<yr>[0-9][0-9][0-9][0-9])-
(?P<mo>
    (0?[1-9])     # 01..09, 1..9
    | (1[0-2])# 10..12
)-
(?P<da>    (3[01])# 30, 31
    |     ([12][0-9])  # 10-19, 20-29
    |     ([0]?[1-9])  # 01-09, 1-9
)
""", re.VERBOSE)

sample = "On 2018-06-12, we will have an exam."
match = date_pat.search(sample)
if match:
    parts = match.groupdict()
    print("{}/{}/{}".format(parts["mo"], parts["da"], parts["yr"]))
else:
    print("Didn't find a date")
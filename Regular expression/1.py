from re import *


x = "[^abc]"


matcher = finditer(x, "a7b@k9z")
for match in matcher:
    print(match.start(), "......", match.group())

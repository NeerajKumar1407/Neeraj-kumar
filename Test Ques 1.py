"""Given a string, compute recursively a new string where all appearances
of "pi" have been replaced by "3.14". (Input: xpix)"""


x = input()
split_str = x.split("pi")
join_str = ("3.14").join(split_str)
print(join_str)


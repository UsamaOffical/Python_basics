text = "Hey my name is usama jameel. I'm  a student of GIAIC!"

# part = string[0:20:2]

# print(part)

# print(text[::-1])# ye puri string ko reverse kar dae ga

# ------------------ reapeat

num = "10"
# print(num * 10) # print ten time in one line


# --------------- membership
nam = "Usama"
# print("U" in num)

swap = "uSmAma sSjJ".swapcase()
# print(swap)

# ------------- replace method

language = "Python programming"

chg_lang = language.replace("Python","Javascript")

# print(language,chg_lang)

split_method = "a-b-c"
s = split_method.split("-")
# print(s)

# -------------- join

result = ", ".join(s)
# print(result)

# --------------- startwith & endswith

start_end = "python"

print(start_end.startswith("p"))# true / false

print(start_end.endswith("n"))# true / false

print(start_end.isalpha()) # true / false 

print(start_end.isdigit()) # true / false

print(start_end.isalnum()) # true / false




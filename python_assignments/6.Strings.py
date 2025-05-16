# 1. Different ways creating a string
print("\n1. String Creation")
s1 = "Hello"
s2 = str('World')
s3 = '''Multiline
String'''
print(s1, s2, s3)

# 2. Concatenating two strings using + operator
print("\n2. String Concatenation")
s = s1 + " " + s2
print(s)

# 3. Finding the length of the string
print("\n3. String Length")
count = 0
for _ in s:
    count += 1
print("Length:", count)

# 4. Extract a string using Substring
print("\n4. Substring Extraction")
sub = ""
for i in range(0, 5):
    sub += s[i]
print(sub)

# 5. Searching in strings using index()
print("\n5. Searching with index()")
ch = 'W'
idx = -1
for i in range(count):
    if s[i] == ch:
        idx = i
        break
print(f"Index of '{ch}':", idx)

# 6. Matching with regex using match()
print("\n6. Regex Match")
import re
pattern = r"boy"
print("Match found:" if re.match(pattern, s) else "No match")

# 7. Comparing strings
print("\n7. String Comparison")
a, b = "abc", "abc"
print("Equal" if a == b else "Not Equal")

# 8. startsWith(), endsWith(), compareTo()
print("\n8. startswith(), endswith(), comparison")
print("Starts with Hello:", s.startswith("Hello"))
print("Ends with World:", s.endswith("World"))
# compareTo equivalent
print("Compare result:", (a > b) - (a < b))  # 0 if equal

# 9. Trimming strings with strip()
print("\n9. Trimming")
raw = "  hello  "
trimmed = ""
i, j = 0, len(raw) - 1
while i <= j and raw[i] == ' ':
    i += 1
while j >= i and raw[j] == ' ':
    j -= 1
for k in range(i, j+1):
    trimmed += raw[k]
print("Trimmed:", trimmed)

# 10. Replacing characters in strings with replace()
print("\n10. Replace")
orig = "apple"
repl = ""
for ch in orig:
    if ch == 'p':
        repl += 'b'
    else:
        repl += ch
print("Replaced:", repl)

# 11. Splitting strings with split()
print("\n11. Split")
text = "one,two,three"
parts = []
temp = ""
for ch in text:
    if ch == ',':
        parts.append(temp)
        temp = ""
    else:
        temp += ch
parts.append(temp)
print("Split:", parts)

# 12. Converting integer objects to Strings
print("\n12. Int to String")
num = 123
num_str = ""
for digit in str(num):  # Manual form
    num_str += digit
print(num_str)

# 13. Upper and lower case
print("\n13. Case Conversion")
sample = "HeLLo"
upper, lower = "", ""
for ch in sample:
    if 'a' <= ch <= 'z':
        upper += chr(ord(ch) - 32)
    else:
        upper += ch
for ch in sample:
    if 'A' <= ch <= 'Z':
        lower += chr(ord(ch) + 32)
    else:
        lower += ch
print("Upper:", upper)
print("Lower:", lower)

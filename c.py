
def log_plagiat_check(func):
    def wrapper(*args):
        original_result = func(*args)
        print(f"Check '{args[0]}' vs '{args[1]}' -> {original_result}")
        return original_result
    return wrapper

@log_plagiat_check
def is_plagiat(word1: str, word2: str):
  s1 = set(word1.lower())
  s2 = set(word2.lower())
  l = len(s2.difference(s1))
  res = (l == 1 or l == 0)
  return res

source_file = open('words.txt', 'r')
for line in source_file:
    words = line.strip().split()
    if len(words) == 0:
        break
    is_plagiat(words[0], words[1])

source_file.close()
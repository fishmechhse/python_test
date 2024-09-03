source_file = open('input2.txt', 'r')
word1 = source_file.readline()
word2 = source_file.readline()
def is_plagiat(word1: str, word2: str):
  s1 = set(word1.lower())
  s2 = set(word2.lower())
  l = len(s2.difference(s1))
  res = (l == 1 or l == 0)
  return res
print(is_plagiat(word1, word2))
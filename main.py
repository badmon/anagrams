from collections import defaultdict

wordstore = defaultdict(list)

def sort_word(word):
	#sanitize string
	word = sanitize(word)
	return ''.join(sorted(word))

def sanitize(s):
	return s.strip()

def main():
	with open('words.txt', 'r') as f, open('anagrams.txt', 'w') as out:
		for w in f:
			wordstore[sort_word(w)].append(sanitize(w))
		for k,v in wordstore.items():
			if len(v) > 1:
				# print(v)
				out.write(' '.join(v) + '\n')

if __name__ == '__main__':
	main()

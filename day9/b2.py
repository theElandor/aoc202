# cleaner solution for part 2
import sys
filename = sys.argv[1]
nums = [int(x) for x in list(open(filename).read().strip())]
spaces = []
files = []
pos = 0
ide = 0
mem = []
for i,n in enumerate(nums):
	if i % 2 != 0:
		if n != 0:
			spaces.append([pos,n])
			mem += ["." for _ in range(n)]
	else:
		if n != 0:
			mem += [ide for _ in range(n)]
			files.append((pos,n,ide))
		ide += 1
	pos += n

final = ["."]*len(mem)
print(files)
print(spaces)
for file_start, file_len, ide in files[::-1]: # for each file from the end
	for i in range(len(spaces)): # for each space from beg
		space_start, space_len = spaces[i]
		if space_start >= file_start:
			continue
		if space_len >= file_len:
			# insert
			final[space_start:space_start+file_len] = [ide]*file_len
			# update that space
			if space_len == file_len:
				spaces.pop(i)
			else:
				spaces[i][0] = space_start + file_len
				spaces[i][1] = space_len - file_len
			break
	else:
		final[file_start:file_start+file_len] = [ide]*file_len

ans = sum([i *int(n) for i, n in enumerate(final) if n != "."])

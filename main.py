import os
import time


commit_count = -1

with open('commit_count.txt', 'r') as f:
	commit_count = int(f.read())

if commit_count == -1:
	raise ValueError("Check the commit_count.txt")

for i in range(commit_count):
	os.system(f'echo "Commit {str(i + 1)}" > main.txt')
	os.system(f'git add .')
	os.system(f'git commit -m "Auto-commit {str(i + 1)} at {time.strftime("%Y-%m-%d %H:%M:%S")}"')
	time.sleep(0.3)

commit_count += 1

with open('commit_count.txt', 'w') as f:
	f.write(str(commit_count))

os.system(f'git add .')
os.system(f'git commit -m "Auto-commit to update commit_count.txt at {time.strftime("%Y-%m-%d %H:%M:%S")}"')
time.sleep(0.5)

os.system("git push")
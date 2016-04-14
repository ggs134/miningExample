import random
import string
import hashlib

example_challenge = '1a9s9d9f9b99df91234kjdifh'


def generation(challenge=example_challenge, size=25):
    answer = ''.join(random.choice(string.ascii_lowercase +
                                   string.ascii_uppercase + 
                                   string.digits) for x in range(size))
    attemp = challenge + answer

    return attemp, answer

def testAttempt():
	shaHash = hashlib.sha256()
	test, attempt = generation()
	shaHash.update(attempt)
	solution = shaHash.hexdigest()
	return solution, attempt


if __name__ == "__main__":
	found = False
	while found == False:
		sol, answer = testAttempt()
		if sol.startswith('0000'):
			found = True
			print sol

	print answer
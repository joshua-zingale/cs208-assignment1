import random
import hashlib
def main():
    nouns = ["men", "women", "dogs", "cats", "mysteries"]
    verbs = ["chase", "fear", "love", "want"]

    with open("./server/mydata.txt", "w") as f:

        for _ in range(30):
            subject = nouns[random.randrange(len(nouns))].capitalize()
            verb = verbs[random.randrange(len(verbs))]
            object = nouns[random.randrange(len(nouns))]
            f.write(f"{subject} {verb} {object}. ")

    with open("mydata.txt", "rb") as f:
        print(hashlib.md5(f.read()).hexdigest())

if __name__ == "__main__":
    main()
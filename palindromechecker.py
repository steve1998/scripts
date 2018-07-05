# checks if a word is a palindrome

# palindrome function
def palindrome(str):
    i = 0
    j = len(str) - 1

    # comparison of each word
    while j > i:
        if str[i] != str[j]:
            return False
        i = i + 1
        j = j - 1

    return True

def main():
    filename = input("Enter list of words to check for palindrome: ")
    counter = 0 # final value goes here

    # reads each line in the list of files
    with open(filename) as f:
        content = f.readlines()

    # removes whitespace
    content = [x.strip() for x in content]

    # iterates over every word in the txt file
    for word in content:
        num = palindrome(word)

        if num == True:
            counter += 1

    print("There are", counter, "palindromes in this list of words")

    # old version
    # str = input("Enter the word to check: ")
    # pal = palindrome(str)
        #if pal == True:
            #print("Word is a palindrome")
        #else:
            #print("Word is not a palindrome")

if __name__ == "__main__":
    main()

def count_word_occurrences(file_name, word):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            occurrences = content.lower().count(word.lower())
            return occurrences
    except FileNotFoundError:
        print("File not found.")
        return -1

def main():
    file_name = input("Enter the file name: ")
    word = input("Enter the word to search: ")
    
    occurrences = count_word_occurrences(file_name, word)
    if occurrences >= 0:
        print(f"The word '{word}' occurs {occurrences} time(s) in the file '{file_name}'.")
    else:
        print("Word count cannot be determined.")

if __name__ == "__main__":
    main()
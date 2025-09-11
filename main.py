import sys
# Imports sys module to handle command line arguments

# Check if the number of command line arguments is 2
if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1) # Exit the program if the number of arguments is not 2
else:    
    path_to_book = sys.argv[1]
# Gets the path to the book from command line arguments

from stats import count_words
# Imports count_words from stats.py

from stats import count_characters
# Imports count_characters from stats.py 

from stats import sorting_characters
# Imports sorting_characters from stats.py   

def main():
    
    #Header Starts
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path_to_book}...")
    print ("----------- Word Count ----------")
    #Header Ends

    #Word count starts
    text = get_book_text(path_to_book)
    print (f"Found {count_words(text)} total words")
    #Word count ends

    #Character count starts (sorted)
    print ("--------- Character Count -------")
    characters = count_characters(text)
    sorted_characters = sorting_characters(characters)
    for item in sorted_characters:
        char_to_check = item["char"] # Get the character from the dictionary to check if its an alphabet latter.
        num = item["num"] # Get the count of the character from the dictionary. No need to check if its an alphabet latter.But will help if f-string.
        print (f"{char_to_check}: {num}") # Print the character and its count.
    
    #Character count ends (sorted)
    
    # Footer Starts
    print ("============= END ===============")
    # Footer Ends

    # End of main()
     
def get_book_text(path_to_book):
    with open(path_to_book, 'r', encoding='utf-8') as file:
        return file.read()
# Converts path_to_book to text

main()
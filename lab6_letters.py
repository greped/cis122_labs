# lab6.py
# This is Josh Guertler's submission for Lab 6

def main():
    # description and text input space are added

    textInput = input("\nDesign and develop a program to report the number of times\na certain letter appears in a sentence. Prompt the user for\nthe sentence, then the letter to search for and display the\nnumber of times that letter appears. Your result must include\nboth uppercase and lowercase occurrences of the letter.\nEnter the input sentence: ")

    # user is prompted to input their desired letter

    inputLetter = input("Enter input letter: ")

    # this line first capitalizes the text input and then counts the number of times the capitalized version of the input letter can be found. Capitalization avoid case sensitivity issues.

    print("Number of occurrence of the letter", inputLetter, ":", textInput.upper().count(inputLetter.upper()))
main()

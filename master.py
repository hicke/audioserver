#!/usr/bin/python

def main():
    text_file = open("Output.txt", "w")
    for i in range(1, 32):
        print i
    text_file.close()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
# text_file.close()

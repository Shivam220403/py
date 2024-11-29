def palindrome(string):
        for i in range(len(string) // 2):
                if string[i] != string[len(string) - i - 1]:
                        print("It is Not a palindrome.")
                        return
        print("It is a palindrome.")


s = str(input("Enter a string: ")).lower()
palindrome(s)
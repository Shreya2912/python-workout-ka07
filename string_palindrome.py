class String_Ops:
    @staticmethod
    def reverse_string(str):
        return str[::-1]

    @staticmethod
    def isPalindrome(input_str):
        return input_str==input_str[::-1]

class String_Ops_Runner:
    print(String_Ops.reverse_string("shreya"))
    print(String_Ops.isPalindrome("madam"))

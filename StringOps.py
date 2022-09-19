class String_Ops:
    @staticmethod
    def reverse_string(str):
        return str[::-1]

    @staticmethod
    def isPalindrome(input_str):
        return input_str==input_str[::-1]

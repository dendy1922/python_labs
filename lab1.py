from functools import reduce


class MyClass:

    def __init__(self):
        print("Con")

    def check_unique_words(self, l_str):
        """
        function checking unique words in str
        """
        words = l_str.lower().split()
        print(l_str)
        return len(set(words)) == len(words)

    def change_word(self, l_str, word_before, word_after):
        """
        change word without recurcive
        """
        return l_str.replace(word_before, word_after)

    def change_word_rec(self, l_str, word_before, word_after):
        #function string.split(separator, maxsplit)
        s_list = l_str.split(" ",1)
        # after split we get list that contain first word and remaining string
        # checking if first word on replace
        if s_list[0] == word_before:
            s_list[0] = word_after

        #recursive case
        if len(s_list) == 1:
            return s_list[0]

        #base case
        #concatenation first words of returning functions
        return s_list[0] + " " + self.change_word_rec(s_list[1], word_before, word_after)

    def compose(self, *fns):
        """
        composing two functions check_unique_words and change_word
        """
        return reduce(lambda second, first: lambda *args: second(first(*args)), fns)

    def script_intger(self):
        """
        Script for inputting and finding square 1/3
        """
        try:
            int_srp = int(input("Input integer: "))
            result = int_srp**(1/3)
            print(result)
        except ValueError:
            print("Wrong number")


if __name__ == "__main__":

    #inputing data 
    STR_L = input("input string: ")
    word_before = input("input what replace substring: ")
    word_after = input("input by what replace substring: ")
    #for automate filling(uncomment down)
    #STR_L, word_before, word_after = "The factories in the2 Banana above use a number of different providers to match  type  data  model would contain", "code", "Banana"
    #creating instance
    z = MyClass()
    #print result of checking unique words
    print(z.check_unique_words(STR_L))
    print()
    #recursive changing words
    print(z.change_word_rec(STR_L, "code", "Banana"))
    print()
    #realizing composing functions
    mul = z.compose(z.check_unique_words, z.change_word)
    print(mul(STR_L, word_before, word_after))
    print()
    #execution script of integer
    z.script_intger()
    
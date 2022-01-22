
class Choice():
    # Choices are represented as 0, 1, ... n-1 number of choices
    # Last column of choices data is which choice they decided on

    def __init__(self, choice_row,num_options=4):
        self.NUM_OPTIONS = num_options
        #XXX add which choice it was column
        self.choice = choice_row[0]
        self.choice_number = choice_row[-1]
        # self.choice = self.encode()
        self.checkrep()


    # def encode(self):
    #     self.letter = self.letter.strip()
    #     if self.letter == "a":
    #         choice = [1, 0, 0, 0]
    #     elif self.letter == "b":
    #         choice = [0, 1, 0, 0]
    #     elif self.letter == "b":
    #         choice = [0, 0, 1, 0]
    #     elif self.letter == "d":
    #         choice = [0, 0, 0, 1]
    #     else:
    #         raise ValueError("letter is not a supported Choice")
    #     return choice


    def checkrep(self):
        # assert(len(self.choice) == self.NUM_OPTIONS)
        assert(self.choice < self.NUM_OPTIONS)


    def __str__(self):
        return str(self.choice)
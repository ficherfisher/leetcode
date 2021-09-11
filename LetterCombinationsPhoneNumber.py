
def letterCombinations(digits):
    information = [["abc"], ["def"],["ghi"],["jkl"],
                   ["mno"],["pqrs"],["tuv"],["wxyz"]]
    result = []
    temp = []
    for i in digits:
        temp.append(information[i])
        

    pass


if __name__ == "__main__":
    digits = ""
    letterCombinations(digits)



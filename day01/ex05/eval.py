class Evaluator:

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        sum = 0
        for i, word in enumerate(words):
            sum += (coefs[i] * len(word))
        return print(sum)

    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return print(-1)
        sum = 0
        for word, coef in zip(words, coefs):
            sum += coef * len(word)
        return print(sum)


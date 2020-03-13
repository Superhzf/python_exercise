class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        B = 0
        secret_list = dict()
        B_candidate = []

        for index,secret_char in enumerate(secret):

            if secret_char in secret_list.keys():
                secret_list[secret_char]+=1
            else:
                secret_list[secret_char] = 1

        for index,secret_char in enumerate(secret):
            if secret_char == guess[index]:
                A += 1
                secret_list[secret_char] -=1
            else:
                B_candidate.append(guess[index])


        for guess_char in B_candidate:
            if guess_char in secret_list.keys() and secret_list[guess_char] > 0:
                B+=1
                secret_list[guess_char]-=1

        return "{}A{}B".format(A,B)

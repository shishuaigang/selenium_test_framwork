import random


def createRandomPhoneNumber():
    phoneNumberFront = ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '150', '151', '152',
                        '153', '158', '159', '177', '180', '181', '182', '183', '186', '188', '189']
    phoneNumberBack = []
    for i in range(8):
        phoneNumberBack.append(str(random.randint(0, 9)))
    return random.choice(phoneNumberFront) + ''.join(phoneNumberBack)


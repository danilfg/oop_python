class BasePage:
    pass


class LoginPage(BasePage):
    pass

"""
LoginPage -> BasePage -> object
"""
# print(issubclass(LoginPage, BasePage))
# print(issubclass(BasePage, LoginPage))

lp = LoginPage()

# print(isinstance(lp, LoginPage))
# print(isinstance(lp, BasePage))
# print(isinstance(lp, object))

# print(issubclass(int, object))
# print(issubclass(list, object))
# print(issubclass(str, object))

class Str(str):
    def __str__(self):
        return "Это строка: " + self

s1 = str("ываукцпку")
print(s1)
s2 = Str("ываукцпку")
print(s2)


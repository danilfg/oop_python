"""
assert условие, 'комментарий'
"""

# def avg(lst: list):
#     assert len(lst) > 0, (
#         "Список не имеет элементов,\n"
#         "для вычесления среднего значения\n"
#         f"Переданный список: {lst}"
#     )
#
#     return round(sum(lst)/len(lst), 2)
#
# lst_1 = [12, 34, 556]
# lst_2 = []
# print(avg(lst_2))
resp = {'balance': 200, 'word': 'sfjfuiqehieh23iurhdfiu23h'}

def check_token(response):
    assert 'token' in response, "Токен отсутствует в ответе от сервера"

check_token(resp)
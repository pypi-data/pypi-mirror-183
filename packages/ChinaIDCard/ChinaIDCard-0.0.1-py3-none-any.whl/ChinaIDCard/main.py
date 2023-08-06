import random
import time


def check_ID_Card(idcard):
    if len(idcard) == 18:
        a = idcard
        check_digit_mapping = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
        weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        s = sum(int(a[i]) * w for i, w in enumerate(weights))
        expected_check_digit = check_digit_mapping[s % 11]
        return a[17] == expected_check_digit
    else:
        return "Length of ID card does not match"


def calculation_17ID_Card_code18(idcard_17):
    if len(idcard_17) == 17:
        a = idcard_17
        weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_digit_mapping = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
        weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        s = sum(int(a[i]) * w for i, w in enumerate(weights))
        expected_check_digit = check_digit_mapping[s % 11]
        return idcard_17 + expected_check_digit
    else:
        return "I need the first 17 of my ID cards"


def generate_ID_Card():
    # 生成前17位
    idcard = ''.join(str(random.randint(0, 9)) for _ in range(17))
    # 计算校验位
    check_digit_mapping = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    s = sum(int(idcard[i]) * w for i, w in enumerate(weights))
    check_digit = check_digit_mapping[s % 11]
    # 生成完整的身份证号码
    idcard += check_digit
    return idcard



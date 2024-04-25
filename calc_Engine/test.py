import unittest
from Postfix_Evaluation import Post_Evaluation
t=unittest.TestCase()
pe=Post_Evaluation()
infix_expressions = {
    "5 + 3 * 2":11,
    "10 - 2 + 4":12,
    "8 * (3 + 2)":40,
    "15 / 3 - 2":3,
    "(7 - 2) * 4":20,
    "12 + 6 / 2":15,
    "2 * 3 + 7":13,
    "4 - 2 * (5 - 2)":-2,
    "6 / (2 + 1)":2,
    "(4 + 3) * (6 - 4)":14,
    "9 - 3 * 2":3,
    "5 + 2 * 3":11,
    "8 / 2 + 1":5,
    "2 * (6 + 3)":18,
    "(12 - 4) / 2":4,
    "7 - 3 + 5":9,
    "10 * 2 / 4":5,
    "(8 + 2) * 3":30,
    "4 / (2 - 1)":4,
    "9 - 6 / 2":6,
    "5 + 4 * 2 - 1":12,
    "2 * (5 - 1) + 3":11,
    "(10 - 2) / 4":2,
    "6 + 4 / 2":8,
    "7 * (3 + 1)":28,
    "12 / 2 - 3":3,
    "4 - 2 + (6 - 3)":5,
    "9 / (3 * 1)":3,
    "2 + 3 * (8 - 4)":14,
    "(6 - 2) * 3 + 1":13,
    #"sin(0.5)":0.0087265354983,
    "sin(33)":0.544639035015027,
    "cos(33)":0.838670567945424
}


for infix_expr, expected_result in infix_expressions.items():
    actual_result = pe.Post_Evaluation(infix_expr)
    if isinstance(expected_result, float):
        t.assertAlmostEqual(actual_result, expected_result, delta=0.000000000000001)
    else:
        t.assertEqual(actual_result, expected_result)
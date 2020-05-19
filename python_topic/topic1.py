from itertools import product, combinations, combinations_with_replacement
"""
武老师在纸上写了4个数字后，便收了起来，接着他对同学们说：“这张纸上有4个数字，这4个数字是1至8中的任意4个，
现在请各位同学们猜一猜是哪4个数字。”听完之后，有四位同学（甲、乙、丙、丁）分别作出了如下回答。

甲：就凭借我对武老师的了解，我觉得这4个数字很可能是2、3、4、5。
乙：我凭感觉猜测，应该是1、3、4、8。
丙：那我就猜1、2、7、8。
丁：我没有什么依据，就猜是1、4、6、7吧。

武老师在听完四位同学的回答后说到：“很不错，甲和丙两位同学猜对了2个数字，而乙和丁同学只猜对了1个数字。
”那么，同学们，听了我的话后，你们谁能够推理出这4个数字到底是什么吗？
"""

class MathTest():

    def base(self):
        a = [2, 3, 4, 5]
        b = [1, 3, 4, 8]
        c = [1, 2, 7, 8]
        d = [1, 4, 6, 7]
        guess_all_list = [(a, 2), (b, 1), (c, 2), (d, 1)]
        base_number = [1, 2, 3, 4, 5, 6, 7, 8]
        # real_list = list(product(base_number, repeat=4))
        real_list = list(combinations_with_replacement(base_number, 4))
        print(real_list)
        # real_list = list(combinations(base_number, 4))
        answer = list()
        answer_remove = list()
        for real_number in real_list:
            assert_list = list()
            for guess in guess_all_list:
                guess_list = guess[0]
                guess_num = guess[1]
                list_together = [x for x in guess_list if x in real_number]
                assert_list.append(self.get_assert_count(real_number, list_together, guess_num))
            if assert_list.count(False) == 0:
                answer.append(real_number)
        print(answer)
        answer = [sorted(x) for x in answer]
        [answer_remove.append(y) for y in answer if y not in answer_remove]
        print(answer_remove)

    @staticmethod
    def get_assert_count(real_number, count_list, number):
        count_num = 0
        for i in count_list:
            count_num += real_number.count(i)
        if count_num == number:
            return True
        else:
            return False


if __name__ == '__main__':
    MathTest().base()

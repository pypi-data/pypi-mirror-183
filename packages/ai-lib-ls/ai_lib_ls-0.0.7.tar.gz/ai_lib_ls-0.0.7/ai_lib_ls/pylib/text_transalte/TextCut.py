# -*- coding: utf-8 -*-
import re
import numpy as np


class TextShort():
    def __init__(self, min_len=2000, step=10, stop_list=None):
        self.min_len = min_len  # 自定义最短长度
        self.step = step  # 自定义划窗步长
        if stop_list and isinstance(stop_list, list):
            self.stop_list = stop_list  # 自定义分割标点符
        else:
            self.stop_list = ['.', '!', '|', '。', '！', '；', ';', '?', '？', ',']
        self.split_patten = '[' + ''.join(self.stop_list) + ']'

    def find_now_index(self, now_point, sum_len_list):
        for i in range(len(sum_len_list) - 1):
            if now_point >= sum_len_list[i] and now_point < sum_len_list[i + 1]:
                return i + 1
        else:
            return 0

    def cut_text(self, text):
        if not isinstance(text, str):
            raise TypeError
        spilt_text = re.split(self.split_patten, text)
        len_list = np.array([len(x) for x in spilt_text])
        sum_len_list = np.cumsum(len_list)
        result_list = []
        end_point = 0
        pre_index = 0
        while end_point <= sum_len_list[-1]:
            end_point += self.step
            now_index = self.find_now_index(end_point, sum_len_list)
            if np.sum(len_list[pre_index:now_index]) >= self.min_len:
                result_list.append(''.join(spilt_text[pre_index:now_index]))
                pre_index = now_index
        return result_list

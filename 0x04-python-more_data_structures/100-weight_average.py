#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is not None:

        sum_of_weight = 0
        sum_score_weight = 0

        for score, weight in my_list:
            sum_of_weight += weight
            sum_score_weight += score * weight

        return sum_score_weight / sum_of_weight
    else:
        return 0

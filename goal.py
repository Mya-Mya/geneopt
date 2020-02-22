#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy


# In[ ]:


class Goal():
    '''
    最適化の目標を示す抽象クラス。
    '''
    def __init__(self):
        pass
    def get_ranking(self,y_list):
        '''
        最適化の試行結果を目標に近いもの順に並べ替える。
        
        Parameters
        ----------
        y_list : list
            試行結果の数値(リスト形式)
        
        Returns
        -------
        rank_index : list
            目標に近いもの順に並べ替えられたy_listの添字配列(リスト形式)
        '''
        pass


# In[ ]:


class Maximize(Goal):
    '''
    スカラー値の最大化を目標とする。
    '''
    def __init__(self):
        pass
    def get_ranking(self,y_list):
        '''
        最適化の試行結果(スカラー値)を大きいもの順に並べ替える。
        
        Parameters
        ----------
        y_list : list
            試行結果のスカラー値(リスト形式)
        
        Returns
        -------
        rank_index : list
            大きいもの順に並べ替えられたy_listの添字配列(リスト形式)
        '''
        return list(numpy.argsort(y_list)[::-1])
    def __str__(self):
        return 'スカラー値の最大化を目標とする。'


# In[ ]:


class Minimize(Goal):
    '''
    スカラー値の最小化を目標とする。
    '''
    def __init__(self):
        pass
    def get_ranking(self,y_list):
        '''
        最適化の試行結果(スカラー値)while小さいもの順に並べ替える。
        
        Parameters
        ----------
        y_list : list
            試行結果のスカラー値(リスト形式)
        
        Returns
        -------
        rank_index : list
            小さいもの順に並べ替えられたy_listの添字配列(リスト形式)
        '''
        return list(numpy.argsort(y_list))
    def __str__(self):
        return 'スカラー値の最小化を目標とする。'


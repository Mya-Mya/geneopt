#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[3]:


class InheritWay:
    '''
    遺伝方法を表し、遺伝を行う抽象クラス。
    '''
    def inherit(self,val_range,g1,g2):
        '''
        遺伝を行う。
        Parameters
        ----------
        val_range : (min:float,max:float)
            変数の値域
        g1 : float
            親1の遺伝情報
        g2 : float
            親2の遺伝情報
        Returns
        -------
        gc : float
            子の遺伝情報
        '''
        pass


# In[4]:


class Meaning(InheritWay):
    '''
    親の遺伝情報のほぼ中間を子の遺伝情報とする。
    '''
    def __init__(self,α):
        '''
        Parameters
        ----------
        α : float
            突然変異の割合
            2つの親の遺伝情報の差 * α 標準偏差とした
            正規分布の乱数を突然変異とし、子の遺伝情報に加算する。
        '''
        self.α=α
    def inherit(self,val_range,g1,g2):
        '''
        遺伝を行う。
        Parameters
        ----------
        val_range : (min:float,max:float)
            変数の値域
        g1 : float
            親1の遺伝情報
        g2 : float
            親2の遺伝情報
        Returns
        -------
        gc : float
            子の遺伝情報
        '''
        gc=random.gauss((g1+g2)*0.5,(g1-g2)*self.α)
        if gc<val_range[0]:gc=val_range[0]
        elif val_range[1]<gc:gc=val_range[1]
        return gc
    def __str__(self):
        return '親の遺伝情報のほぼ中間を子の遺伝情報とする。α={}'.format(self.α)


# In[5]:


class SheerNew(InheritWay):
    '''
    親の遺伝情報に関わらず全く新しい遺伝情報の子を生成する。
    '''
    def inherit(self,val_range,g1,g2):
        '''
        遺伝を行う。
        Parameters
        ----------
        val_range : (min:float,max:float)
            変数の値域
        g1 : float
            親1の遺伝情報
        g2 : float
            親2の遺伝情報
        Returns
        -------
        gc : float
            子の遺伝情報
        '''
        return random.uniform(val_range[0],val_range[1])
    def __str__(self):
        return '親の遺伝情報に関わらず全く新しい遺伝情報の子を生成する。'


# In[66]:


class GeneticOptimizer:
    '''
    遺伝アルゴリズムを提供する。
    '''
    def __init__(self,M,f,val_ranges,goal,N,num_parent,num_generation,inherit_ways):
        '''
        Parameters
        ----------
        M : int
            最適化の対象となる関数が受け入れる変数の数
        f : function
            最適化の対象となる関数
        val_ranges : list
            各変数の値域
            (min:float,max:float)のリスト形式
        goal : Goal
            最適化の目標
        N : int
            1世代あたりの個体数
        num_parent : int
            次の世代を作るために使われる親の個体数
        num_generation : int
            全世代数
        inherit_ways : dict
            遺伝方法とその実行割合をdict形式でまとめたもの
            key : InheritWay value : float
        '''
        self.set_M(M)
        self.set_f(f)
        self.set_val_ranges(val_ranges)
        self.set_goal(goal)
        self.set_N(N)
        self.set_num_parent(num_parent)
        self.set_num_generation(num_generation)
        self.set_inherit_ways(inherit_ways)
        self.debug=False
    def execute(self):
        '''
        適化を実行する
        Returns
        -------
        final_generation_variable_list : list
            最後の世代の親となる予定だった個体達の変数値
        log : list
            各世代の親もしくは親となる予定だった個体達の変数値
        '''
        log=[]
        indv_list=[]
        #初世代の個体
        for i in range(self.N):#各個体に対し
            gene_list=[]
            for j in range(self.M):
                val_range=self.val_ranges[j]
                gene_list.append(
                    random.uniform(val_range[0],val_range[1])
                )
            indv_list.append(gene_list)
        
        #最適化
        now_generation=1
        while(now_generation<=self.num_generation):
            if(self.debug):print('generation{}'.format(now_generation))
            if(self.debug):print('indv_list={}'.format(indv_list))
            
            #評価値の収集
            y_list=[]
            for i in range(self.N):
                val=indv_list[i]
                y_list.append(self.f(val))
            if(self.debug):print('y_list={}'.format(y_list))
            
            #ランク付けと親決め
            rank_index=self.goal.get_ranking(y_list)
            if(self.debug):print('rank_index={}'.format(rank_index))
            parents=[indv_list[i]for i in rank_index[0:self.num_parent]]
            log.append(parents)
            
            if(now_generation==self.num_generation):break
            #遺伝して次の世代をつくる
            if(self.debug):print('parents={}'.format(parents))
            next_indv_list=[]
            for i in range(self.N):#各個体に対し
                if(self.debug):print('next_indv{}'.format(i))
                parent1=random.choice(parents)
                parent2=random.choice(parents)
                inherit_way=self.__get_inherit_way__()
                if(self.debug):print(' inherit_way={}'.format(inherit_way))
                
                gene_list=[]
                for j in range(self.M):
                    if(self.debug):print(' gene{}'.format(j))
                    val_range=self.val_ranges[j]
                    g1=parent1[j]
                    g2=parent2[j]
                    gc=inherit_way.inherit(val_range,g1,g2)
                    if(self.debug):print(' g1={} g2={} gc={}'.format(g1,g2,gc))
                    gene_list.append(gc)
                next_indv_list.append(gene_list)
            
            indv_list=next_indv_list
            now_generation+=1
        
        return parents,log
    def __get_inherit_way__(self):
        R=random.random()
        I=0
        for i in range(len(self.inherit_ways_values)):
            if i==0:
                if R<=self.inherit_ways_values[0]:
                    I=0
                    break
            elif self.inherit_ways_values[i-1]<R and R<self.inherit_ways_values[i]:
                I=i
                break
        return self.inherit_ways_keys[I]
    def set_M(self,M):
        self.M=M
    def set_f(self,f):
        self.f=f
    def set_val_ranges(self,val_ranges):
        self.val_ranges=val_ranges
    def set_goal(self,goal):
        self.goal=goal
    def set_N(self,N):
        self.N=N
    def set_num_parent(self,num_parent):
        self.num_parent=num_parent
    def set_num_generation(self,num_generation):
        self.num_generation=num_generation
    def set_inherit_ways(self,inherit_ways):
        s=sum(inherit_ways.values())
        accr=0
        for k,v in inherit_ways.items():
            v/=s
            accr+=v
            inherit_ways[k]=accr
        self.inherit_ways_keys=list(inherit_ways.keys())
        self.inherit_ways_values=list(inherit_ways.values())
        self.inherit_ways=inherit_ways
    def enable_debug(self):
        self.debug=True


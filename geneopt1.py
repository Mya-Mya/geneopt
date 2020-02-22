#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
import random


# In[ ]:


class Expression:
    '''
    遺伝情報から変数値を発現する方法を記述する。
    '''
    def __init__(self,min_value,max_value,num_gene_bit):
        '''
        Parameters
        ----------
        min_value : number
            変数値の最小値
        max_value : number
            数値値の最大値
        num_gene_bit : int
            遺伝子ビット数
        '''
        self.min_value=min_value
        self.max_value=max_value
        self.num_gene_bit=num_gene_bit
        self.__update_D__()
        
    def express(self,gene):
        '''
        遺伝子に従い変数値を発現する。
        Parameters
        ----------
        gene : int
            ビットで表現された遺伝子情報
        '''
        return self.min_value+self.D*gene
    def get_num_gene_bit(self):
        return self.num_gene_bit
    def set_num_gene_bit(self,num_gene_bit):
        '''
        遺伝子ビット数を指定する。
        Parameters
        ----------
        num_gene_bit : int
            遺伝子ビット数
        '''
        self.num_gene_bit=num_gene_bit
        __update_D__(self)
    def set_max_value(self,max_value):
        '''
        数値の最大値を指定する。
        Parameters
        ----------
        max_value : number
            変数値の最大値
        '''
        self.max_value=max_value
        __update_D__(self)
    def set_min_value(self,min_value):
        '''
        数値の最小値を指定する。
        Parameters
        ----------
        min_value : number
            変数値の最小値
        '''
        self.min_value=min_value
        __update_D__(self)
    def __update_D__(self):
        self.D=(self.max_value-self.min_value)/(2**self.num_gene_bit-1)
    def __str__(self):
        return 'Expression min_value={} max_value={} num_gene_bit={} D={}'.format(
            self.min_value,self.max_value,self.num_gene_bit,self.D
        )


# In[ ]:


class InheritWay():
    '''
    遺伝子の遺伝方法を表し、遺伝を行う抽象クラス。
    '''
    def __init__(self):
        pass
    def inherit(self,num_gene_bit,g1,g2):
        '''
        遺伝を行う。
        Parameters
        ----------
        num_gene_bit : int
            遺伝子ビット数
        g1 : int
            親1のビットで表現された遺伝子情報
        g2 : int
            親2のビットで表現された遺伝子情報
        Returns
        -------
        gc : int
            生成された新しい個体のビットで表現された遺伝子情報
        '''
        pass


# In[ ]:


class EitherClone(InheritWay):
    '''
    どちらかを選びクローンとする。
    '''
    def __init__(self):
        pass
    def inherit(self,num_gene_bit,g1,g2):
        '''
        遺伝を行う。
        Parameters
        ----------
        num_gene_bit : int
            遺伝子ビット数
        g1 : int
            親1のビットで表現された遺伝子情報
        g2 : int
            親2のビットで表現された遺伝子情報
        Returns
        -------
        gc : int
            生成された新しい個体のビットで表現された遺伝子情報
        '''
        if random.getrandbits(1):
            return g1
        return g2
    def __str__(self):
        return 'どちらかを選びクローンとする。'


# In[ ]:


class SheerMutation(InheritWay):
    '''
    突然変異を起こし全く新しい個体を生成する。
    '''
    def __init__(self):
        pass
    def inherit(self,num_gene_bit,g1,g2):
        '''
        遺伝を行う。
        Parameters
        ----------
        num_gene_bit : int
            遺伝子ビット数
        g1 : int
            親1のビットで表現された遺伝子情報
        g2 : int
            親2のビットで表現された遺伝子情報
        Returns
        -------
        gc : int
            生成された新しい個体のビットで表現された遺伝子情報
        '''
        print('called random...')
        return random.getrandbits(num_gene_bit)
    def __str__(self):
        return '突然変異を起こし全く新しい個体を生成する。'


# In[ ]:


class GeneticCrossing(InheritWay):
    '''
    遺伝子交叉を行ったり、一定確率で突然変異を起こしたりする。
    2つの親の遺伝子ビットの各桁を比較した際、
    A : 遺伝子情報が同じ -> ratioの確率でその桁を反転させる(突然変異)。
    B : 遺伝子情報が異なる -> 遺伝子交叉を行う。
    '''
    def __init__(self,ratio):
        '''
        Parameters
        ----------
        ratio : float
            突然変異を起こす確率
        '''
        self.ratio=ratio
    def inherit(self,num_gene_bit,g1,g2):
        '''
        遺伝を行う。
        Parameters
        ----------
        num_gene_bit : int
            遺伝子ビット数
        g1 : int
            親1のビットで表現された遺伝子情報
        g2 : int
            親2のビットで表現された遺伝子情報
        Returns
        -------
        gc : int
            生成された新しい個体のビットで表現された遺伝子情報
        '''
        for d in range(num_gene_bit):
            if ((g1>>d)&1) ^ ((g2>>d)&1):#g1とg2の遺伝子ビットが異なる桁に対して(B)
                if random.getrandbits(1):#半分の確率で
                    g1^=(1<<d)#g1のその遺伝子ビットの桁を反転する
            else:#g1とg2の遺伝子ビットが同じ桁に対して(A)
                if random.random()<=self.ratio:#ratioの確率で
                    g1^=(1<<d)#g1のその遺伝子ビットの桁を反転する
        return g1
    def __str__(self):
        return '遺伝子交叉を行ったり、一定確率で突然変異を起こしたりする。ratio={}'.format(self.ratio)


# In[ ]:


class GeneticOptimizer:
    '''
    遺伝アルゴリズムを提供する。
    '''
    def __init__(self
                 ,M,target_func,expression_list,goal
                 ,N,num_parent,num_generation,inherit_ways):
        '''
        Parameters
        ----------
        M : int
            最適化の対象となる関数が受け入れる変数の数
        target_func : function
            最適化の対象となる関数
        expression_list : list
            各変数の発現方法Expressionをlist形式でまとめたもの
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
        self.set_expression_list(expression_list)
        self.set_goal(goal)
        self.set_inherit_ways(inherit_ways)
        self.set_N(N)
        self.set_M(M)
        self.set_num_generation(num_generation)
        self.set_num_parent(num_parent)
        self.set_target_func(target_func)
        self.disable_debug()
    def disable_debug(self):
        self.debug=False
    def enable_debug(self):
        self.debug=True
    def execute(self):
        '''
        最適化を実行する
        Returns
        -------
        final_generation_variable_list : list
            最後の世代の変数値
        '''
        indv_list=[]
        #ランダムに1世代目の各個体を生成する。
        for i in range(self.N):#各個体に対し
            gene_list=[]
            for j in range(self.M):#各遺伝子に対し
                num_gene_bit=self.expression_list[j].get_num_gene_bit()
                gene_list.append(random.getrandbits(num_gene_bit))
            indv_list.append(gene_list)
        
        #最適化作業
        now_generation=1
        while(now_generation<=self.num_generation):
            if(self.debug):print('generation{}'.format(now_generation))
            
            y_list=[]
            for i in range(self.N):#各個体に対し
                gene_list=indv_list[i]
                
                if(self.debug):print('indv{}: gene_list={}'.format(i,gene_list))
                
                variable_list=[]#標的関数に与える変数リスト
                for j in range(self.M):#各遺伝子に対し
                    variable_list.append(
                        self.expression_list[j].express(gene_list[j])
                    )
                
                if(self.debug):print('indv{}: variable_list={}'.format(i,variable_list))
                
                y_list.append(self.target_func(variable_list))#標的関数から評価値をもらう
            
            if(self.debug):print('y_list={}'.format(y_list))
            
            rank_index=self.goal.get_ranking(y_list)
            
            if(self.debug):print('rank_index={}'.format(rank_index))
            
            parents=[indv_list[i]for i in rank_index[0:self.num_parent]]#目標に近い親を選出
            
            if(self.debug):print('parents={}'.format(parents))
            
            next_indv_list=[]
            for i in range(self.N):#各個体に対し
                
                if(self.debug):print('next_indv{}'.format(i))
                
                gene_list=[]
                inherit_way=self.__get_inherit_way__()
                parent_indv_1=random.choice(parents)
                parent_indv_2=random.choice(parents)
                
                if(self.debug):print('inherit_way={}'.format(inherit_way))
                
                for j in range(self.M):#各遺伝子に対し
                    num_gene_bit=self.expression_list[j].get_num_gene_bit()
                    g1=parent_indv_1[j]
                    g2=parent_indv_2[j]
                    gc=inherit_way.inherit(num_gene_bit,g1,g2)
                    
                    if(self.debug):print(' gene{}: g1={} g2={} gc={}'.format(j,bin(g1),bin(g2),bin(gc)))
                    
                    gene_list.append(gc)
                
                next_indv_list.append(gene_list)
            indv_list=next_indv_list
            now_generation+=1
        
        #最終世代の変数値
        final_generation_variable_list=[]
        for i in range(self.N):#各個体に対し
            gene_list=indv_list[i]
            variable_list=[]
            for j in range(self.M):#各遺伝子に対し
                expression=self.expression_list[j]
                variable_list.append(expression.express(gene_list[j]))
            final_generation_variable_list.append(variable_list)
        return final_generation_variable_list
            
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
    def set_expression_list(self,expression_list):
        '''
        各変数の発現方法を指定する。
        Parameters
        ----------
        expression_list : list
            各変数の発現方法Expressionをlist形式でまとめたもの
        '''
        self.expression_list=expression_list
    def set_goal(self,goal):
        '''
        最適化の目標を指定する。
        Parameters
        ----------
        goal : Goal
            最適化の目標
        '''
        self.goal=goal
    def set_inherit_ways(self,inherit_ways):
        '''
        遺伝方法とその実行割合を指定する。
        Parameters
        ----------
        inherit_ways : dict
            遺伝方法とその実行割合をdict形式でまとめたもの
            key : InheritWay value : float
        '''
        s=sum(inherit_ways.values())#valuesを(0,1]の累積割合に変換する
        rr=0
        for k,v in inherit_ways.items():
            v/=s
            rr+=v
            inherit_ways[k]=rr
        self.inherit_ways_keys=list(inherit_ways.keys())
        self.inherit_ways_values=list(inherit_ways.values())
        self.inherit_ways=inherit_ways
    def set_N(self,N):
        '''
        1世代あたりの個体数を指定する。
        Parameters
        ----------
        N : int
            1世代あたりの個体数
        '''
        self.N=N
    def set_M(self,M):
        '''
        最適化の対象となる関数が受け入れる変数の数を指定する。
        Parameters
        ----------
        M : int
            最適化の対象となる関数が受け入れる変数の数
        '''
        self.M=M
    def set_num_generation(self,num_generation):
        '''
        全世代数を指定する。
        Parameters
        ----------
        num_generation : int
            全世代数
        '''
        self.num_generation=num_generation
    def set_num_parent(self,num_parent):
        '''
        次の世代を作るために使われる親の個体数を指定する。
        Parameters
        ----------
        num_parent : int
            次の世代を作るために使われる親の個体数
        '''
        self.num_parent=num_parent
    def set_target_func(self,target_func):
        '''
        最適化の対象となる関数を指定する。
        Parameters
        ----------
        target_func : function
            最適化の対象となる関数
        '''
        self.target_func=target_func
    def __str__(self):
        return 'M={} target_func={} expression_list={} goal={} N={} num_parent={} num_generation={} inherit_ways={}'.format(
            self.M,self.target_func,self.expression_list,self.goal,self.N,self.num_parent,self.num_generation,self.inherit_ways
        )


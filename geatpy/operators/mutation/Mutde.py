# -*- coding: utf-8 -*-
from operators.mutation.Mutation import Mutation
from mutde import mutde

class Mutde(Mutation):
    """
    Mutde - class : 一个用于调用内核中的变异函数mutde(差分变异)的变异算子类，
                    该类的各成员属性与内核中的对应函数的同名参数含义一致，
                    可利用help(mutde)查看各参数的详细含义及用法。
    """
    def __init__(self, F = 0.5, DN = 1, Loop = False):
        self.F = F # 差分变异缩放因子
        self.DN = DN # 表示有多少组差分向量
        self.Loop = Loop # 表示是否采用循环的方式处理超出边界的变异结果
    
    def do(self, Encoding, OldChrom, FieldDR, *args): # 执行变异
        if len(args) != 1:
            raise RuntimeError('error in Mutde: Parameter error. (传入参数错误。)')
        r0_or_Xr0 = args[0]
        return mutde(Encoding, OldChrom, FieldDR, r0_or_Xr0, self.F, self.DN, self.Loop)
    
    def getHelp(self): # 查看内核中的变异算子的API文档
        help(mutde)
    
# -*- coding: utf-8 -*-
def A(y,n):
    s=1
    for key in n:
        s=s*(1+y)
    return s
    
def B(y,n):
    m1=1-s(y,n)
    return m1/y

def C(y,n,c,m):
    return m*A+c*B


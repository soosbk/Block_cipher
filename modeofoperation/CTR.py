# soosbk 나중에 개인 포트폴리오로 활용될 자료입니다. 무단복제 하지마세요
#CTR
#No padding

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:02:29 2020

@author: soosbk
"""
import random

def xor_fun(pt,ct):
    #print(type(pt))
    new_state=[]
    for i in range(len(pt)):
        new_state+=[pt[i]^ct[i]]
        
    return new_state

  
 def get_counter(nonce):
    nonce[15] = (nonce[15]+ 1) % 256
    for i in range(15,0,-1) :
        if (nonce[i] == 0):
            c=1
            nonce[i-1] = (nonce[i-1] + c) % 256
            #print("a\n")
        else :
            c=0
            return nonce
    return nonce
   


def get_nonce(): # Nonce 생성 하는 함수
    nonce = [0 for i in range(16)]
    for i in range(16):
        nonce[i] = random.randint(0, 255)
    return nonce    
                
def CTR(pt,key): #padding x
    ct=[]
    #nonce=get_nonce() #초기 한 번
    nonce=[0xf0,0xf1,0xf2,0xf3,0xf4,0xf5,0xf6,0xf7,\
           0xf8,0xf9,0xfa,0xfb,0xfc,0xfd,0xfe,0xfe]   #test

    block_num=(len(pt)+16-1)//16
    
    for i in range(block_num-1):
        nonce=get_counter(nonce)
        i_th_state=pt[16*i : 16*i+16]
        state=Toycipher_Enc(nonce,key)
        ct+=xor_fun(state,i_th_state)        
    
    #마지막 블록 처리
    nonce=get_counter(nonce)
    
    state=Toycipher_Enc(nonce,key)

    
    #처리 시작
    for i in range((len(pt)-16*(block_num-1))&31):
        ct+= [state[i]^pt[16*(block_num-1)+i]]
    
    return ct
    

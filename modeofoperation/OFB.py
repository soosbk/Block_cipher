#soosbk 나중에 개인 포트폴리오로 활용될 자료입니다. 무단복제 하지마세요
#OFB

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:02:29 2020

@author: soosbk
"""


   
    
import random

def get_nonce(): # Nonce 생성 하는 함수
    nonce = [0 for i in range(16)]
    for i in range(16):
        nonce[i] = random.randint(0, 255)
    return nonce    
    

    
def OFB(pt,key):
    ct=[]
    IV=get_nonce();
    '''
    IV=[0xf0,0xf1,0xf2,0xf3,0xf4,0xf5,0xf6,0xf7,\
           0xf8,0xf9,0xfa,0xfb,0xfc,0xfd,0xfe,0xfe]   #test'''
    
    new_state=[]    
    block_num=(len(pt)+16-1)//16
    nonce=IV
    for i in range(block_num-1):
        new_state=Toycipher_Enc(nonce,key) #Toycipher의 output이 next input이 됨
        i_th_state=pt[16*i : 16*i+16]
        ct+=xor_fun(new_state,i_th_state) 
        nonce=new_state
        
    
    #마지막 블록 처리
    state=Toycipher_Enc(nonce,key)
    
    
    #처리 시작
    for j in range((len(pt)-16*(block_num-1))&31):
        ct+=[ pt[16*(block_num-1)+j]^state[j]]
    
    return ct



    

# soosbk 나중에 개인 포트폴리오로 활용될 자료입니다. 무단복제 하지마세요
#CBC
#padding: one-zero


# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:02:29 2020

@author: soosbk
"""
import random

def padding(pt):
    pad_pt=[]
    pad_pt=pt
    pad_pt.append(0x10)
    while(1):
        if(len(pad_pt)%16==0): break
        else: pad_pt.append(0x00)
        
    return pad_pt

def get_nonce(): # Nonce 생성 하는 함수
    nonce = [0 for i in range(16)]
    for i in range(16):
        nonce[i] = random.randint(0, 255)
    return nonce    
    
def CBC_Enc(pt,key):
    ct=[]  
    #padding
    aft_pt=padding(pt)
    #IV=get_nonce();
    IV=[0xf0,0xf1,0xf2,0xf3,0xf4,0xf5,0xf6,0xf7,\
           0xf8,0xf9,0xfa,0xfb,0xfc,0xfd,0xfe,0xfe]   #test
    
    block_num=len(aft_pt)//16
    nonce=IV
    for i in range(block_num):
        i_th_state=aft_pt[16*i : 16*i+16]
        new_state=xor_fun(i_th_state,nonce)
        nonce=Toycipher_Enc(new_state,key)
        ct+=nonce
    
    return ct
    
def CBC_Dnc(ct,key):
    pt=[]
    #IV=get_nonce();
    IV=[0xf0,0xf1,0xf2,0xf3,0xf4,0xf5,0xf6,0xf7,\
           0xf8,0xf9,0xfa,0xfb,0xfc,0xfd,0xfe,0xfe]   #test
    
    block_num=len(ct)//16
    nonce=IV
    for i in range(block_num):
            i_th_state=ct[16*i : 16*i+16]
            new_state=Toycipher_Dnc(i_th_state,key)
            pt+=xor_fun(new_state,nonce)
            nonce=i_th_state
        
    
# padding 삭제  
    while(1):
        num=len(pt)-1
        if(pt[num]==0x10):
            del(pt[num])
            break
        del(pt[num])
       
    return pt
        

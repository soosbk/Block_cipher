# soosbk 나중에 개인 포트폴리오로 활용될 자료입니다. 무단복제 하지마세요
#ECB
#padding: one-zero

def padding(pt):
    pad_pt=[]
    pad_pt=pt
    pad_pt.append(0x10)
    while(1):
        if(len(pad_pt)%16==0): break
        else: pad_pt.append(0x00)
        
    return pad_pt
    
    
    
    
def ECB_Enc(pt,key):
   ct=[]
   #padding
   aft_pt=padding(pt)
   block_num=len(aft_pt)//16
   for i in range(block_num):
       i_th_state=aft_pt[16*i : 16*i+16]
       new_state=Toycipher_Enc(i_th_state, key)
       ct+=new_state
   #toycipher를 이용해 enc
   
   return ct
        

def ECB_Dnc(ct,key):
    pt=[]
    block_num=len(ct)//16
    for i in range(block_num):
        i_th_state=ct[16*i : 16*i+16]
        new_state=Toycipher_Dnc(i_th_state,key)
        pt+=new_state
        
  # padding 삭제 
    while(1):
        num=len(pt)-1
        if(pt[num]==0x10):
            del(pt[num])
            break
        del(pt[num])

       
    return pt
    

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:11:01 2019

@author: achoud3
"""

        
usr_inp=int(input("Enter your 4 digit PIN :"))
raw=usr_inp
riv=0
r2=raw

while(r2!=0):
    div=r2%10
    riv=riv*10+div
    r2=r2//10






rev=0
for i  in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                div=usr_inp%10
                if(l==div):
                    rev=rev*10+div
                  
                    if(rev==riv):
                       print("The PIN is : "+str(raw))
                       break
                                        
                    
                   
                    
                
                   
            
            usr_inp=usr_inp//10
            div=usr_inp%10
            if(k==div):
                rev=rev*10+div
                if(rev==riv):
                  # print(" hiiii" )
                    exit
              # print(" the rev is 2 " +str(rev))
                break
        usr_inp=usr_inp//10
        div=usr_inp%10
        if(j==div):
            rev=rev*10+div
            if(rev==riv):
               #print(" hiiii" )
                exit
           #print(" the rev is 3 " +str(rev))
            break
    usr_inp=usr_inp//10
    div=usr_inp%10
    if(i==div):
        rev=rev*10+div
        if(rev==riv):
          # print(" hiiii" )
            exit
      # print(" the rev is 4" +str(rev))
        break
    usr_inp=usr_inp//10
    if(rev==riv):
       #print(" hiiii" )
        exit
    break
    break





                
   

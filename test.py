#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:38:57 2020

@author: louis
"""
#1-a

s=['louiswei']
s_s=[]
for i in s[0]:

    s_s.append(i)
#s_copy=s.copy()
s_copy=['']
for i in range(0,len(s[0])):
    s_copy[0]+=s_s[len(s[0])-i-1]
print(s_copy)
#1-b
text=['hi how are you']
text_s=['']
count_word=0
for i in text[0]:
    if i == ' ':
        count_word+=1
        text_s.append('')
count=0
for i in text[0]:
    if i == ' ':
        count+=1
        continue
    text_s[count]+=i
ans=['']

contrary=[]
for i in text_s:
    s=[i]
    s_s=[]
    for j in s[0]:

        s_s.append(j)
        #s_copy=s.copy()
        s_text_copy=['']
    for k in range(0,len(s[0])):
        s_text_copy[0]+=s_s[len(s[0])-k-1]    
    contrary.append(s_text_copy)
for i in contrary:
    ans[0]+=i[0]
print(ans)
 
#2.
num=[]
n=int(input('input:'))
for i in range(1,n+1):
    if  i%15==0:
        num.append(i)
    elif i % 5 !=0 and i % 3 != 0:
        num.append(i)
        
        
print('output: %s' % (len(num)))
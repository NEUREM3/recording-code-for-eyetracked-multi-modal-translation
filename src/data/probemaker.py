#!/usr/bin/env python3
"""
Probemaker
"""
import os
import random
from shutil import rmtree
import numpy as np

data_ambig = os.path.join("experiment_pics","dry_run_probe_ambig")
data_nonambig = os.path.join("experiment_pics","dry_run_probe_nonambig")


f_ambig = open(data_ambig,"r")
cap_a = f_ambig.read().split("\n")
ambig_sent_id = np.arange(start=0, stop=100) 
np.random.shuffle(ambig_sent_id)
ambig_sent = np.concatenate((ambig_sent_id,ambig_sent_id,ambig_sent_id), axis=None) #accounting for all permutations of the ambiguous stimulus

#ambig_captions = []
#for ind in ambig_sent:
#    ambig_captions.append(cap_a[ind])


f_nonambig = open(data_nonambig,"r")
cap_na = f_nonambig.read().split("\n")
nonambig_sent_id = np.arange(start=0, stop=100) 
np.random.shuffle(nonambig_sent_id)
nonambig_sent = np.concatenate((nonambig_sent_id,nonambig_sent_id,nonambig_sent_id), axis=None)

#nonambig_captions = []
#for ind in nonambig_sent:
#    nonambig_captions.append(cap_na[ind])

    

try:
    os.mkdir("probes")
except FileExistsError:
    rmtree(os.path.join(os.getcwd(),"probes"))
    os.mkdir("probes")    

def amb_rand(n):
    r = random.randint(0,100)
    if r==n:
        amb_rand(n)
    return r


def namb_rand(n):
    r = random.randint(0,100)
    if r==n:
        namb_rand(n)
    return r

def construct_probe():
    probe_name = 0
    s_no = 0
    for probe in range(0,300,15):
        probe_name += 1
        p_name = "probes/probe"+str(probe_name)
        print(probe_name)
        f = open(p_name,"a")
        for sent in range(5):
            for case in range(3):
                if case==0:
                    img_amb = ambig_sent[s_no]
                    img_namb = nonambig_sent[s_no]
                elif case==1:
                    img_amb = amb_rand(s_no) 
                    img_namb = namb_rand(s_no)
                elif case==2:
                    img_amb ='control'
                    img_namb = 'control'
                tup_amb = 'amb'+ '\t' + str(case) + '\t' + str(ambig_sent[s_no]) + '\t' + cap_a[ambig_sent[s_no]] + '\t' + str(img_amb)+".jpg"+"\n"
                tup_namb = 'namb'+ '\t' + str(case) + '\t' + str(nonambig_sent[s_no]) + '\t' + cap_na[nonambig_sent[s_no]] + '\t' + str(img_namb)+".jpg"+"\n"
                f.write(tup_amb)
                f.write(tup_namb)
                s_no += 1
            amb_contrastive = "A person in a blue ski suit is racing two girls on skis."
            namb_contrastive = "A person in her blue ski suit is racing two girls on skis."
        tup_amb = 'amb'+ '\t' + '3' + '\t' + 'contrastive_amb' + '\t' + amb_contrastive + '\t' + "contrastive.jpg"+"\n"
        tup_namb = 'namb'+ '\t' + '3' + '\t' + 'contrastive_namb' + '\t' + namb_contrastive + '\t' + "contrastive.jpg"+"\n"
        f.write(tup_amb)
        f.write(tup_namb)
        f.close()
construct_probe()

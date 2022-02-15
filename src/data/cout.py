import os
import numpy as np
m = 0
w = 0
mi_m = 100000
mi_w = 100000
for file in os.listdir(os.path.join(os.getcwd(),"probes")):
    f_ = open(os.path.join(os.getcwd(),os.path.join("probes",file)),"r").read().split("\n")
    if len(f_)==33:
        for line in f_:
            try:
                sent = line.split("\t")[3]
                words = sent.split()
                if m<=len(sent):
                    m=len(sent)
                if mi_m>=len(sent):
                    mi_m=len(sent)
                if w<=len(words):
                    w=len(words)
                if mi_w>=len(words):
                    mi_w=len(words)
            except:
                pass
print(m)
print(w)
print(mi_m)
print(mi_w)
        

import os

  #####   ####     #   #   ####
    #      #  #    #   #  #       TRUS: Triple Relation Using Syntaxnet.
    #      ###     #   #  #       
    #      #  #    #   #   ####  
    #      #  #     ###        #
                               #
  #############################             

def info():
  print "\nDeveloped by: Mr.Ravin Kumar.  Email id: mr.ravin_kumar@hotmail.com"
  print "Linkedin: https://www.linkedin.com/in/ravinkumar21/"

# Python code to parse the syntax net
# lst: list of wrds, 
# dat_lst: list in order of word in sentence, 
# rel: list in order of tree, and sub tree.

def parse_read(filename):
    dat=open(filename)
    dat_read=dat.readlines()
    #print dat_read
    val=[]
    lst_val=[]
    for i in range(len(dat_read)):
        if i>=2:
            val.append(dat_read[i][:-1])
            continue
        if i==0:
            lst_val.append(dat_read[i][7:-1])
            continue
        else:
            continue
    tmp_lst=act_parse(val)
    label_list=[]
    for j in val:
          #print j
          cnt=0
          while j[cnt]==' 'or j[cnt:cnt+3]=='+--' or j[cnt]=='|':
              #print "printing"
              #print j[cnt]
              cnt=cnt+1
          if j[cnt-1:cnt+3]=='+-- ':
              label_list.append(j[cnt+3:])
          else:
              label_list.append(j[cnt:])
    ##################################################

    tmp_parent=[]
    for i in range(len(tmp_lst)):
        cnt=0
        if i>0:
          for j in range(i+1):
              if tmp_lst[j]<tmp_lst[i]:
               cnt=j
          tmp_parent.append(cnt)
        else:
            tmp_parent.append(-1)

    fin_label_list=[] 
    for i in label_list:
      fin_label_list.append(i.split(" "))
    return (fin_label_list,tmp_parent)

def act_parse(val):
    tpl=[]
    for i in val:
        cnt=0
        if i[0]!=' ':
            tpl.append(0)
        else:
          while i[cnt]!='+':
              cnt=cnt+1
          tpl.append(cnt)
    return tpl
info()
print "\nenter sentence :"
strng=raw_input()
os.system("echo "+"\""+strng+"\""+" | syntaxnet/demo.sh > tree.txt")
t=parse_read('tree.txt')
fin_label=t[0]
fin_dep=t[1]

fin_strng=strng.split(' ')


lst=[]
cnt=0
for i in range(len(fin_dep)):
  lst.append([fin_dep[i],cnt,fin_label[i],[],0])
  cnt=cnt+1

for i in range(len(lst)):
  if lst[i][0]!= -1:  
    lst[lst[i][0]][3].append(i)

list_concat_nn_vb_subj_obj=[]
for i in lst:
  if i[2][1][0:2] =="VB" or i[2][1][0:2] =="VB" or i[2][2][1:5] =="subj" or i[2][2][1:4] =="obj":
    list_concat_nn_vb_subj_obj.append(i)

dat_lst=[]
for i in fin_strng:
  cnt=0
  for j in lst:
    if cnt==0:
      if i==j[2][0]:
        dat_lst.append([i,j])
        cnt=cnt+1

subjects=[]
objects=[]
tmp=[]
for i in dat_lst:
  if i[1][2][2][1:5]=="subj":
      subjects.append(i)
  elif i[1][2][2][1:4]=="obj":
    if len(i[1][3])==0:
      objects.append(i)
  else: 
    tmp.append(i)

tmp=[]
cnt=0
rel=[]
ty=0
while ty<len(lst):
  ty=ty+1
  if lst[cnt][4]!=1:
    val=lst[cnt]
    lst[cnt][4]=1
    tmp.append(val)
    for i in val[3]:
     if len(lst[i][3])==0:
       lst[i][4]=1
     tmp.append(lst[i])
    rel.append(tmp)
    tmp=[]
  cnt=cnt+1

####### Triple Relationship Retrival Method ###############
###########################################################

# Python code to generate triple relations from the above receive information
# res contains the triple relations

def check(fin_subj,fin_root,fin_obj,nn,vb):  ### check if subject, root/verb , object are present or not...and then handle accordingly.
  tmp=""
  if len(fin_subj)==0 and len(fin_obj)==0:
    if len(nn)!=0:
      tmp=tmp+" "+nn
    if len(vb)!=0:
      tmp=tmp+" "+vb
    return ["",fin_root,tmp,0]   
  return [fin_subj,fin_root,fin_obj,1]  
  
last_rel=[]
fin_subjz=""
fin_rootz=""
fin_objz=""

def frstfn(main_node,prev_subj,prev_root,prev_obj):  ### triple relations generation function
  cnt=-1
  child=[]
  subj=""
  obj=""
  root=""
  nn=""
  vb=""
  for i in main_node:
    cnt=cnt+1
    if cnt==0:          ## conditions for parent 
          if i[2][2][1:5]=="subj":
            if main_node[1][2][1][:2]=="NN" and len(main_node[1][3])==0:
              subj=main_node[1][2][0]+" "+i[2][0]
              main_node[1][4]=main_node[1][4]+1
            else:
              subj=i[2][0]
      
          elif i[2][2][1:4]=="obj" or i[2][2][1:4]=="mod":
            if main_node[1][2][1][:2]=="NN" and len(main_node[1][3])==0:
              obj=main_node[1][2][0]+" "+i[2][0]
              main_node[1][4]=main_node[1][4]+1
            else:
              obj=i[2][0]
          else:
            root=i[2][0]
          i[4]=i[4]+1

    else:               ## conditions for child
      if len(i[3])==0:
          if i[2][2][1:5]=="subj":
              subj=i[2][0]+" "+subj
          elif i[2][2][1:4]=="obj" or i[2][2][1:4]=="mod" or i[2][2][0:3]=="num":
              obj=i[2][0]+" "+obj
          elif i[2][1]=="RB":
              root=i[2][0]+" "+root
          elif i[2][1][:2]=="VB":
              vb=i[2][0]
          elif i[2][1][:2]=="NN":
              nn=i[2][0]
          i[4]=i[4]+1
      else:  
          child.append(i)   ## child which further have childs.

  fin_subj=""
  fin_obj="" 
  fin_root=""  
  subj=subj.strip()
  obj=obj.strip()
  root=root.strip()
  
  if len(subj)!=0:
    fin_subj=subj
  if len(obj)!=0:
    fin_obj=obj
  if len(subj.strip())==0 and len(prev_subj.strip())!=0:
    fin_subj=fin_subj+" "+prev_subj
  if len(obj.strip())==0 and len(prev_obj.strip())!=0:
    fin_obj=fin_obj+" "+prev_obj



  fin_root=fin_root+" "+prev_root
  fin_root=fin_root+" "+root
  fin_root=fin_root.strip()
  
  n=check(fin_subj,fin_root,fin_obj,nn,vb)
  
  send=n[:-1]
  
  fin_subjz=send[0].strip()
  fin_rootz=send[1].strip()
  fin_objz=send[2].strip()
  
  for ch in child:
    for ij in range(len(rel)):
      if rel[ij][0]==ch:
          #print "details=",fin_subjz
          frstfn(rel[ij],fin_subjz,fin_rootz,fin_objz)
  last_rel.append([fin_subjz,fin_rootz,fin_objz,n[-1]])       
   
frstfn(rel[0],"","","") ### running, Starting from the root of the synatxnet's tree
maxmm=last_rel[0][3]
doer=""
doer_rel=""
final_prnt=[]

for ie in last_rel:
  if ie[3]==maxmm:
    if ie[0]=="" and ie[1].split(" ")[0]==doer_rel:
      ie[0]=doer
      if ie[0]=="" and ie[2]=="":
        final_prnt.append(ie[1].split(" "))  
        #print ie[1].split(" ")
      else:
        final_prnt.append(ie)
        #print ie 
    else:
      doer=ie[0]
      doer_rel=ie[1].split(" ")[0]
      final_prnt.append(ie)  
      
res=[]
#### The conditions below are applied to remove repeated or incomplete triple relations.
for i in range(len(final_prnt)):
  tmp=0
  for j in range(len(final_prnt)):
   if i!=j:
      i_alen=len(final_prnt[i][0])
      i_blen=len(final_prnt[i][1])
      i_clen=len(final_prnt[i][2])
      j_alen=len(final_prnt[j][0])
      j_blen=len(final_prnt[j][1])
      j_clen=len(final_prnt[j][2])
      alen=min(i_alen,j_alen)
      blen=min(i_blen,j_blen)
      clen=min(i_clen,j_clen)
      
      if final_prnt[i][0]=="" and final_prnt[i][1][:blen]==final_prnt[j][1][:blen] and final_prnt[i][2][:clen]==final_prnt[j][2][:clen] and blen>0 and clen>0:
        tmp=tmp+1
        continue
      if final_prnt[i][1]=="" and final_prnt[i][0][:alen]==final_prnt[j][0][:alen] and final_prnt[i][2][:clen]==final_prnt[j][2][:clen] and alen>0 and clen>0:
        tmp=tmp+1
        continue
      if final_prnt[i][2]=="" and final_prnt[i][1][:blen]==final_prnt[j][1][:blen] and final_prnt[i][0][:alen]==final_prnt[j][0][:alen] and alen>0 and blen>0:
        tmp=tmp+1
        continue
      if final_prnt[i][0]=="" and final_prnt[i][1]=="" and final_prnt[i][2][:clen]==final_prnt[j][2][:clen] and clen>0:
        tmp=tmp+1
        continue
      if final_prnt[i][1]=="" and final_prnt[i][0][:alen]==final_prnt[j][0][:alen] and final_prnt[i][2]=="" and alen>0:
        tmp=tmp+1
        continue
      if final_prnt[i][2]=="" and final_prnt[i][0]=="" and final_prnt[i][1][:blen]==final_prnt[j][1][:blen] and blen>0:
        tmp=tmp+1
        continue
      
      if final_prnt[i][1][:blen]==final_prnt[j][1][:blen] and final_prnt[i][0][:alen]==final_prnt[j][0][:alen] and final_prnt[i][2][:clen]==final_prnt[j][2][:clen] and alen>0 and blen>0 and clen>0:
        tmp=tmp+1
        continue
  if tmp==0:
    res.append(final_prnt[i])

#### res contains the triple relation.
for iet in res:   
  print iet

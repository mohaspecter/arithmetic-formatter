def arithmetic_arranger(problems,show_result=True):
  separator="    "
  tiret="-"
  espace=" "
  ligne1=""
  ligne2=""
  ligne3=""
  ligne4=""
  
  def affichage():
   print(ligne1+"\n"+ligne2+"\n"+ligne3+"\n"+ligne4)
  def affichage_sansres():
   print(ligne1+"\n"+ligne2+"\n"+ligne3)
    
  op1list = []
  op2list = []
  reslist = []
  
  for i in range(0, len(problems)):
   nb_space = 0
   op1_lgt=len(problems[i].split()[0])
   op2_lgt=len(problems[i].split()[2])
   nb_space = op1_lgt-op2_lgt
   operand1 = int(problems[i].split()[0])
   operand2 = int(problems[i].split()[2])
   plusminus = problems[i].split()[1]
  
   if plusminus=='+':
    res=operand1+operand2
   if plusminus=='-':
    res=operand1-operand2
   res_lgt = len(str(res))
   ligne1 = ligne1 + espace + espace
   ligne2 = ligne2 + problems[i].split()[1] + espace
  
   while nb_space>0:
    ligne2 = ligne2 + espace
    nb_space = nb_space - 1
   
   while nb_space<0:
    ligne1 = ligne1 + espace
    nb_space = nb_space + 1 
  
   
   ligne1 = ligne1 + str(operand1)
   ligne2 = ligne2 + str(operand2)
   
   while len(ligne2)>len(ligne3):
     ligne3 = ligne3 + tiret
   while len(ligne4)<len(ligne2)-len(str(res)):
     ligne4 = ligne4 + espace
             
   ligne4 = ligne4 + str(res)
  
   #on fait la séparation
   ligne1 = ligne1 + espace + espace + espace + espace
   ligne2 = ligne2 + espace + espace + espace + espace
   ligne3 = ligne3 + espace + espace + espace + espace
   ligne4 = ligne4 + espace + espace + espace + espace

  if show_result is True:
    affichage()
  if show_result is False:
    affichage_sansres()  
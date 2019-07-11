e = int(input(" Para IMC digite 1. Para RQC digite 2. Para análise da medida da cintura digite 3: "))
if (e==1):
  p  = float (input( "Digite seu peso: "))
  a  = float (input ("Digite sua altura: "))
  i  = int (input ("Digite sua idade: "))
  imc= p/(a*a)
  if (i<65):
    if ((imc>1) and (imc < 16)):
      print ("Seu IMC é %.2f e você está com magreza grau 3"%imc)
    elif ((imc> 16) and (imc<16.9)):
      print ("Seu IMC é %.2f e você está com magreza grau 2"%imc)
    elif ((imc> 17) and (imc<18.4)):
      print ( "Seu IMC é %.2f e você está com magreza grau 1"%imc)
    elif ((imc> 18.5) and (imc<24.9)):
      print ( "Seu IMC é %.2f e você está eutrófico" %imc)
    elif ((imc>25) and (imc<29.9)):
      print ("Seu IMC é %.2f e você está com sobrepeso" %imc)
    elif ((imc>30) and (imc<34.9)):
      print ("Seu IMC é %.2f e você está com obesidade grau 1" %imc)
    elif ((imc>35) and (imc<39.9)):
      print ("Seu IMC é %.2f e você está com obesidade grau 2"%imc)
    elif ((imc>40) and (imc<60)):
      print ("Seu IMC é %.2f e você está com obesidade grau 3"%imc)
    else:
      print ("Alguma informação está incorreta. Tente novamente!")
  if (i>65):
    if ((imc>1) and (imc < 22)):
      print ("Seu IMC é %.2f e você está com magreza"%imc)
    elif ((imc> 22) and (imc<27)):
      print ( "Seu IMC é %.2f e você está eutrófico" %imc)
    elif ((imc>27) and (imc<50)):
      print ("Seu IMC é %.2f e você está com excesso de peso"%imc)
    else:
      print ("Alguma informação está incorreta. Tente novamente!")
elif (e==2):
  c = float (input( "Digite a medida da sua cintura: "))
  q = float (input( "Digite a medida do seu quadril: "))
  s = int (input(" Para sexo masculino digite 4. Para sexo feminino digite 5: "))
  rqc= c/q
  
  if (s==4):
    if  (rqc < 0.87):
     print ("Seu RQC é %.2f e você está normal" %rqc)
    elif ((rqc> 0.88) and (rqc<0.95)):
      print ("Seu RQC é %.2f e você possui um risco médio" %rqc)
    elif ((rqc>0.96) and (rqc<1)):
      print ("Seu RQC é %.2f e você possui um risco alto" %rqc)
    elif ((rqc>1) and (rqc<5)):
     print ("Seu RQC é %.2f e você possui um risco muito alto" %rqc)
    else:
     print ("Alguma informação está incorreta. Tente novamente!")
    
  elif (s==5):
    if  (rqc < 0.72):
      print ("Seu RQC é %.2f e você está normal" %rqc)
    elif ((rqc> 0.73) and (rqc<0.79)):
      print ("Seu RQC é %.2f e você possui um risco médio"% rqc)
    elif ((rqc>0.80) and (rqc<0.87)):
      print ("Seu RQC é %.2f e você possui um risco alto" %rqc)
    elif ((rqc>0.87) and (rqc<4)):
     print ("Seu RQC é %.2f e você possui um risco muito alto" %rqc)
    else:
     print ("Alguma informação está incorreta. Tente novamente!")
     
elif (e==3):
  ci = float (input( "Digite a medida da sua cintura: "))
  se = int (input(" Para sexo masculino digite 6. Para sexo feminino digite 7: "))
   
  if (se==6):
    
      if (ci<94):
       print ("Medida Ideal")
      if ((ci>94) and (ci<102)):
       print ("Medida com Risco Moderado")
      if(ci>102):
       print ("Medida com Risco Elevado")
      
  elif (se==7):  
      if (ci<80):
       print ("Medida Ideal")
      if ((ci>80) and (ci<88)):
       print ("Medida com Risco Moderado")
      if (ci>88):
       print ("Medida com Risco Elevado")
   
   
   
   
   
   
   
###################Projeto###################
## Autor: Uriel Gonçalves Paiva da conceição
## Turma: FEAU-3UNA
## Matricula: 02010287
## versão: 2.0v
## Link: https://youtu.be/NCAVdhhkrJA    #Video de 5 min com explicação da Ultima versão do programa
## Link_bonus: https://youtu.be/jXx8d9jYcf4    #video 20min com explicações mais detalhadas da terceira versão do programa
#############################################
import requests; import numpy as np; import matplotlib.pyplot as plt; from datetime import datetime
LTOTAL=[];L0=[];LC=[];IC=[];LCP=[]
i=0;t=0;g=1;u=0;x=0
######BAIXANDO_ARQUIVO#################################################################################################
def Baixar_arquivo(url, endereco):
    resposta= requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arq:
            novo_arq.write(resposta.content)
        print("Download Completo. Salvo como: {}".format(endereco))
    else:
        resposta.raise_for_status()
if __name__ == "__main__":
    Baixar_arquivo('https://covid.ourworldindata.org/data/owid-covid-data.csv','owid-covid-data.csv')
########LEITURA_DE_ARQUIVO#######################################################################################################
arq=open("owid-covid-data.csv","r")
for linha in arq:
    L=linha[:-1].split(',')
    if i > 0:
        data=datetime.strptime((L[3]),'%Y-%m-%d').date()
        L0.append(data)
        LTOTAL.append(L)
    else:
        LTOTAL.append(L)
        i=i+1
arq.close()
while u<len(LTOTAL):
    if LTOTAL[u][1]=="North America" or LTOTAL[u][1]=="South America":
        LC.append(LTOTAL[u])
    u=u+1
while x<len(LC):
    if LC[x][0] not in IC:
        IC.append(LC[x][0])
    if LC[x][2] not in LCP:
        LCP.append(LC[x][2])
    x=x+1
######PROCESSAMENTO_DE_DADOS#############################################################################################
while t<1:
    RLTF=[];LD=[];LM=[];LP=[];MD=[];LR=[];N=[];LMF=[];LPF=[];LRF=[];MDS=[];NS=[];L1=[];LDS=[]
    RLTF2=[];LM2=[];LP2=[];MD2=[];LR2=[];N2=[];LMF2=[];LPF2=[];LRF2=[];MDS2=[];NS2=[]
    RLTF3=[];LM3=[];LP3=[];MD3=[];LR3=[];N3=[];LMF3=[];LPF3=[];LRF3=[];MDS3=[];NS3=[]
    RLTF4=[];LM4=[];LP4=[];MD4=[];LR4=[];N4=[];LMF4=[];LPF4=[];LRF4=[];MDS4=[];NS4=[]
    RLTF5=[];LM5=[];LP5=[];MD5=[];LR5=[];N5=[];LMF5=[];LPF5=[];LRF5=[];MDS5=[];NS5=[]
    w=0;z=0;x=0;v=0;n=0;f=0;k=0;h=0;f2=0;f3=0;f4=0;f5=0;z2=0;z3=0;z4=0;z5=0;s=0;o=0;e=0
    print("digite a seguir os isos codes dos paises que deseja comparar com o Brasil, sendo:")
    while s<len(LCP):
        print(IC[s],":",LCP[s])
        s=s+1
    print("os iso codes disponiveis")
    cod=input("digite o primeiro iso code do país que deseja:\n")
    cod2=input("digite o segundo iso code do país que deseja:\n")
    cod3=input("digite o terceiro iso code do país que deseja:\n")
    cod4=input("digite o quarto iso code do país que deseja:\n")
    p=int(input("1 para colocar grade no grafico e 0 para tirar a grade:\n"))
    a=int(input("1 para colocar legenda no grafico e 0 para tirar a legenda:\n"))
    print("Data limite Minima:",min(L0),"\nData limite Maxima:",max(L0))
    data1=input("digite a data inicial, no formato Y-m-d\n")
    data2=input("digite a data final, no formato Y-m-d\n")
    data1=datetime.strptime(data1,'%Y-%m-%d').date()
    data2=datetime.strptime(data2,'%Y-%m-%d').date()
    if p==1:
        q=True
    else:
        q=False
    while h<1:
        if data1<min(L0) or data2>max(L0):
            data1=input("digite a data inicial novamente, no formato Y-m-d\n")
            data2=input("digite a data final novamente, no formato Y-m-d\n")
            data1=datetime.strptime(data1,'%Y-%m-%d').date()
            data2=datetime.strptime(data2,'%Y-%m-%d').date()
        else:
            h=h+1
    while w<1:
        RLT=[];RLT2=[];RLT3=[];RLT4=[];RLT5=[];c=0
        while c<len(LC):
            if LC[c][0]=="BRA":
                RLT.append(LC[c])
            elif LC[c][0]==cod:
                RLT2.append(LC[c])
            elif LC[c][0]==cod2:
                RLT3.append(LC[c])
            elif LC[c][0]==cod3:
                RLT4.append(LC[c])
            elif LC[c][0]==cod4:
                RLT5.append(LC[c])
            c=c+1
        if len(RLT2)==0:
            cod=input("ISO code invalido. Digite o primeiro iso code do país que deseja novamente:\n")
            w=0
        elif len(RLT3)==0:
            cod2=input("ISO code invalido. Digite o segundo iso code do país que deseja novamente:\n")
            w=0
        elif len(RLT4)==0:
            cod3=input("ISO code invalido. Digite o terceiro iso code do país que deseja novamente:\n")
            w=0
        elif len(RLT5)==0:
            cod4=input("ISO code invalido. Digite o quarto iso code do país que deseja novamente:\n")
            w=0
        else:
            w=1
    while z<len(RLT):
        j=datetime.strptime((RLT[z][3]),'%Y-%m-%d').date()
        if data1<=j<=data2:
            RLTF.append(RLT[z])
            #LD.append(j)
        z=z+1
    while z2<len(RLT2):    
        j2=datetime.strptime((RLT2[z2][3]),'%Y-%m-%d').date()
        if data1<=j2<=data2:
            RLTF2.append(RLT2[z2])
        z2=z2+1
    while z3<len(RLT3):
        j3=datetime.strptime((RLT3[z3][3]),'%Y-%m-%d').date()
        if data1<=j3<=data2:
            RLTF3.append(RLT3[z3])
        z3=z3+1
    while z4<len(RLT4):
        j4=datetime.strptime((RLT4[z4][3]),'%Y-%m-%d').date()
        if data1<=j4<=data2:
            RLTF4.append(RLT4[z4])
        z4=z4+1
    while z5<len(RLT5):
        j5=datetime.strptime((RLT5[z5][3]),'%Y-%m-%d').date()
        if data1<=j5<=data2:
            RLTF5.append(RLT5[z5])
        z5=z5+1
    #####################################################
    while o<len(LC):
        if data1<=L0[o]<=data2 and L0[o] not in L1:
            L1.append(L0[o])
        o=o+1
    LD=L1
    while e<len(L1):
        if len(L1)>len(RLTF):
            RLTF.append(RLTF[-1])
        elif len(L1)>len(RLTF2):
            RLTF2.append(RLTF2[-1])
        elif len(L1)>len(RLTF3):
            RLTF3.append(RLTF3[-1])
        elif len(L1)>len(RLTF4):
            RLTF4.append(RLTF4[-1])
        elif len(L1)>len(RLTF5):
            RLTF5.append(RLTF5[-1])
        e=e+1
    while x<len(RLTF):
        LDS.append(RLTF[x][3])
        if RLTF[x][7]=='':
            LM.append("0")
        else:
            LM.append(str(RLTF[x][7]))
        if RLTF[x][44]=='':
            LP.append("0")
        else:
            LP.append(str(RLTF[x][44]))
        if RLTF[x][16]=='':
            LR.append("0")
        else:
            LR.append(str(RLTF[x][16]))
    ############################################
        if RLTF2[x][7]=='':
            LM2.append("0")
        else:
            LM2.append(str(RLTF2[x][7]))
        if RLTF2[x][44]=='':
            LP2.append("0")
        else:
            LP2.append(str(RLTF2[x][44]))
        if RLTF2[x][16]=='':
            LR2.append("0")
        else:
            LR2.append(str(RLTF2[x][16]))
    ############################################
        if RLTF3[x][7]=='':
            LM3.append("0")
        else:
            LM3.append(str(RLTF3[x][7]))
        if RLTF3[x][44]=='':
            LP3.append("0")
        else:
            LP3.append(str(RLTF3[x][44]))
        if RLTF3[x][16]=='':
            LR3.append("0")
        else:
            LR3.append(str(RLTF3[x][16]))
    #############################################
        if RLTF4[x][7]=='':
            LM4.append("0")
        else:
            LM4.append(str(RLTF4[x][7]))
        if RLTF4[x][44]=='':
            LP4.append("0")
        else:
            LP4.append(str(RLTF4[x][44]))
        if RLTF4[x][16]=='':
            LR4.append("0")
        else:
            LR4.append(str(RLTF4[x][16]))
    ##########################################
        if RLTF5[x][7]=='':
            LM5.append("0")
        else:
            LM5.append(str(RLTF5[x][7]))
        if RLTF5[x][44]=='':
            LP5.append("0")
        else:
            LP5.append(str(RLTF5[x][44]))
        if RLTF5[x][16]=='':
            LR5.append("0")
        else:
            LR5.append(str(RLTF5[x][16]))
        x=x+1
    while k<len(LP):
        LMF.append(float(LM[k]))
        LPF.append(float(LP[k]))
        LRF.append(float(LR[k]))
        ############################
        LMF2.append(float(LM2[k]))
        LPF2.append(float(LP2[k]))
        LRF2.append(float(LR2[k]))
        #############################
        LMF3.append(float(LM3[k]))
        LPF3.append(float(LP3[k]))
        LRF3.append(float(LR3[k]))
        ##############################
        LMF4.append(float(LM4[k]))
        LPF4.append(float(LP4[k]))
        LRF4.append(float(LR4[k]))
        #############################
        LMF5.append(float(LM5[k]))
        LPF5.append(float(LP5[k]))
        LRF5.append(float(LR5[k]))
        k=k+1
    while v<len(LP):
        MT=(LMF[v]/LPF[v])*100
        MD.append(MT)
        MDS.append(str(MT))
        ########################
        MT2=(LMF2[v]/LPF2[v])*100
        MD2.append(MT2)
        MDS2.append(str(MT2))
        #####################
        MT3=(LMF3[v]/LPF3[v])*100
        MD3.append(MT3)
        MDS3.append(str(MT3))
        ########################
        MT4=(LMF4[v]/LPF4[v])*100
        MD4.append(MT4)
        MDS4.append(str(MT4))
        #########################
        MT5=(LMF5[v]/LPF5[v])*100
        MD5.append(MT5)
        MDS5.append(str(MT5))
        v=v+1
    while n<len(MD):
        if MD[n] != 0:
            MM=(LRF[n]/MD[n]) #taxa de reprodução diario em relação a população diaraia
            N.append(MM)
            NS.append(str(MM))
        else:
            N.append(0)
            NS.append(str(0))
        ####################
        if MD2[n] != 0:
            MM2=(LRF2[n]/MD2[n])
            N2.append(MM2)
            NS2.append(str(MM2))
        else:
            N2.append(0)
            NS2.append(str(0))
        #####################
        if MD3[n] != 0:
            MM3=(LRF3[n]/MD3[n])
            N3.append(MM3)
            NS3.append(str(MM3))
        else:
            N3.append(0)
            NS3.append(str(0))
        ###########################
        if MD4[n] != 0:
            MM4=(LRF4[n]/MD4[n])
            N4.append(MM4)
            NS4.append(str(MM4))
        else:
            N4.append(0)
            NS4.append(str(0))
        ##########################
        if MD5[n] != 0:
            MM5=(LRF5[n]/MD5[n])
            N5.append(MM5)
            NS5.append(str(MM5))
        else:
            N5.append(0)
            NS5.append(str(0))
        n=n+1
#########ESCREVENDO_NOVO_ARQUIVO_COM_OS_DADOS_ANALISADOS#####################################################################################################################
    arq=open("3UNA_Uriel_Goncalves_ex1_{}.txt".format(g),"w")
    arq.write(str("Autor: Uriel Gonçalves Paiva da conceição\nTurma: FEAU-3UNA\nMatricula: 02010287\nversão:2.0v\nlink: https://youtu.be/NCAVdhhkrJA \n"))
    arq.write(str("iso_code\tData\tTotal_de_Mortos\tPopulação\tTaxa_de_Reprodução\t%_de_Mortes_diarias_em_relação_a_população\tTaxa_de_reprodução_diario_em_relação_a_população_diaraia\n"))
    while f<len(LP):
        arq.write(str("BRA"+"\t"+LDS[f]+"\t"+LM[f]+"\t"+LP[f]+"\t"+LR[f]+"\t"+MDS[f]+"\t"+NS[f]+"\n"))
        f=f+1
    while f2<len(LP2):
        arq.write(str(cod+"\t"+LDS[f2]+"\t"+LM2[f2]+"\t"+LP2[f2]+"\t"+LR2[f2]+"\t"+MDS2[f2]+"\t"+NS2[f2]+"\n"))
        f2=f2+1
    while f3<len(LP3):
        arq.write(str(cod2+"\t"+LDS[f3]+"\t"+LM3[f3]+"\t"+LP3[f3]+"\t"+LR3[f3]+"\t"+MDS3[f3]+"\t"+NS3[f3]+"\n"))
        f3=f3+1
    while f4<len(LP4):
        arq.write(str(cod3+"\t"+LDS[f4]+"\t"+LM4[f4]+"\t"+LP4[f4]+"\t"+LR4[f4]+"\t"+MDS4[f4]+"\t"+NS4[f4]+"\n"))
        f4=f4+1
    while f5<len(LP5):
        arq.write(str(cod4+"\t"+LDS[f5]+"\t"+LM5[f5]+"\t"+LP5[f5]+"\t"+LR5[f5]+"\t"+MDS5[f5]+"\t"+NS5[f5]+"\n"))
        f5=f5+1
    arq.close()
#########GERANDO_GRAFICO#####################################################################################################################    
    w=60
    LD=np.array(LD, dtype='object')
    LMF=np.array(LMF, dtype='object');MD=np.array(MD, dtype='object');N=np.array(N, dtype='object')
    ##################################
    LMF2=np.array(LMF2, dtype='object');MD2=np.array(MD2, dtype='object');N2=np.array(N2, dtype='object')
    LMF3=np.array(LMF3, dtype='object');MD3=np.array(MD3, dtype='object');N3=np.array(N3, dtype='object')
    LMF4=np.array(LMF4, dtype='object');MD4=np.array(MD4, dtype='object');N4=np.array(N4, dtype='object')
    LMF5=np.array(LMF5, dtype='object');MD5=np.array(MD5, dtype='object');N5=np.array(N5, dtype='object')
###########################################
    plt.figure(figsize=(16, 8))
    plt.subplot(2,2,1)
    plt.plot(LD,MD,'-b',label="Brasil")
    plt.plot(LD,MD2,'-r',label="Primeiro País selecionado")
    plt.plot(LD,MD3,'-g',label="Segundo País selecionado")
    plt.plot(LD,MD4,'-y',label="Terceiro País selecionado")
    plt.plot(LD,MD5,'-p',label="Quarto País selecionado")
    plt.xticks(rotation=w);plt.title("relação diaria do total de mortos com o total da população do país")
    plt.xlabel("(Data)")
    plt.ylabel("(%_de_(mortos/população))")
    if a==1:
        plt.legend(fontsize=10)
    plt.grid(q)
    plt.subplot(2,2,2)
    plt.plot(LD,LMF,'-b',label="Brasil")
    plt.plot(LD,LMF2,'-r',label="Primeiro País selecionado")
    plt.plot(LD,LMF3,'-g',label="Segundo País selecionado")
    plt.plot(LD,LMF4,'-y',label="Terceiro País selecionado")
    plt.plot(LD,LMF5,'-p',label="Quarto País selecionado")
    plt.xticks(rotation=w);plt.title("total de mortos do País")
    plt.xlabel("(Data)")
    plt.ylabel("(Total de mortos)")
    if a==1:
        plt.legend(fontsize=10)
    plt.grid(q)
    plt.subplot(2,2,3)
    plt.plot(LD,N,'-b',label="Brasil")
    plt.plot(LD,N2,'-r',label="Primeiro País selecionado")
    plt.plot(LD,N3,'-g',label="Segundo País selecionado")
    plt.plot(LD,N4,'-y',label="Terceiro País selecionado")
    plt.plot(LD,N5,'-p',label="Quarto País selecionado")
    plt.xticks(rotation=w);plt.title("taxa de reprodução diario em relação ao total de mortes País")
    plt.xlabel("(Data)")
    plt.ylabel("(%de reprodução/%de mortes)")
    if a==1:
        plt.legend(fontsize=10)
    plt.grid(q)
    plt.tight_layout()
    plt.savefig('3UNA_Uriel_Goncalves_ex1_{}.png'.format(g))
    plt.show()
    t=int(input("digite 0 para fazer outra analise ou 1 para parar\n"))
    g=g+1

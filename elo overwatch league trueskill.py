import trueskill as ts
import json
import matplotlib.pyplot as plt

"graphe en semaine"

def afficherelo():
    print("------elo final -----")
    print("valliant : "+str(vaillant))
    print("gladiator : "+str(gladiator))
    print("fusion : "+str(fusion))
    print("excelsior : "+str(excelsior))
    print("spitfire : "+str(spitfire))
    print("uprising : "+str(uprising))
    print("mahyem : "+str(mahyem))
    print("dragon : " + str(dragon))
    print("shock : " + str(choc)  )
    print("dynastie : "+str(dynastie))
    print("fuel : "+str(fuel))
    print("outlaw : "+str(outlaw))

def ajouterlist(tour ):
    if i%12 == 0 :
        listedeselo = [vaillant,gladiator,fusion,excelsior,spitfire,uprising,mahyem,dragon,choc,dynastie,fuel,outlaw]
        listelo.append([i/12,listedeselo])

with open('match.json', 'r') as m:
    fichier = json.load(m)
    match = fichier["content"]
nbMatch = fichier["numberOfElements"]

listelo = []

afficher = True
elo_de_depart = 1000
vaillant =ts.Rating() #4405
gladiator =ts.Rating() #4406
fusion =ts.Rating() #4524
excelsior =ts.Rating() #4403
spitfire = ts.Rating() #4410
uprising =ts.Rating() #4402
mahyem = ts.Rating() # 4407
dragon =ts.Rating() #4408
choc = ts.Rating()#4404
dynastie = ts.Rating() #4409
fuel =ts.Rating() #4523
outlaw = ts.Rating() #4525


for i  in range( nbMatch ):
    #if afficher == True :
       #print(i)
    if i == 205 or i==208 or i ==276 or i== 289 :
        if afficher == True :
            print("match non chargé")
    else :
        donnematch= match[i]["competitors"]
        equipe1 = donnematch[0]["id"]
        equipe2 = donnematch[1]["id"]
    
            #on cherche le winer 
        if equipe1 == 4405 : #valliantwin 
            elo1 = vaillant
        if equipe1 == 4406 : #valliantwin 
            elo1 = gladiator
        if equipe1 == 4524 : #valliantwin 
            elo1 =fusion
        if equipe1 == 4403 : #valliantwin 
            elo1 = excelsior
        if equipe1 == 4410 : #valliantwin 
            elo1 = spitfire
        if equipe1 == 4402 : #valliantwin 
            elo1 = uprising
        if equipe1 == 4407 : #valliantwin 
            elo1 = mahyem
        if equipe1 == 4408 : #valliantwin 
            elo1 = dragon
        if equipe1 == 4404 : #valliantwin 
            elo1 = choc
        if equipe1 == 4409 : #valliantwin 
            elo1 = dynastie
        if equipe1 == 4523 : #valliantwin 
            elo1 = fuel
        if equipe1 == 4525 : #valliantwin 
            elo1 = outlaw
            #------------------------------------------------------    
        if equipe2 == 4405 : #valliantwin 
            elo2 = vaillant
        if equipe2 == 4406 : #valliantwin 
            elo2 = gladiator
        if equipe2 == 4524 : #valliantwin 
            elo2 = fusion
        if equipe2 == 4403 : #valliantwin 
            elo2 = excelsior
        if equipe2 == 4410 : #valliantwin 
            elo2 = spitfire
        if equipe2 == 4402 : #valliantwin 
            elo2 = uprising
        if equipe2 == 4407 : #valliantwin 
            elo2 = mahyem
        if equipe2 == 4408 : #valliantwin 
            elo2 = dragon
        if equipe2 == 4404 : #valliantwin 
            elo2 = choc
        if equipe2 == 4409 : #valliantwin 
            elo2 = dynastie
        if equipe2 == 4523 : #valliantwin 
            elo2 = fuel
        if equipe2 == 4525 : #valliantwin 
            elo2 = outlaw
            
            #on calcule le nouvelle elo 
        if afficher ==True:
            print("-------------------------------------------------")
            print("Match équilibré :  "+str(ts.quality_1vs1(elo1,elo2)))
            
        if equipe1 == match[i]["winner"]["id"]:
            nvelo = ts.rate_1vs1(elo1,elo2)
            elo1 = nvelo[0]
            elo2 = nvelo[1]
            
        else :
            nvelo = ts.rate_1vs1(elo2,elo1)
            elo1 = nvelo[1]
            elo2 = nvelo[0]
           
        if afficher == True :
           print(donnematch[0]["name"] + " " +str(match[i]["scores"][0]["value"] )+"-" + str(match[i]["scores"][1]["value"] )+" " + donnematch[1]["name"])
            
            #on attribut le elo à la team associe
            
        if equipe1 == 4405 : #valliantwin 
            vaillant = elo1
        if equipe1 == 4406 : #valliantwin 
            gladiator= elo1
        if equipe1 == 4524 : #valliantwin 
            fusion= elo1
        if equipe1 == 4403 : #valliantwin 
            excelsior= elo1
        if equipe1 == 4410 : #valliantwin 
            spitfire= elo1
        if equipe1 == 4402 : #valliantwin 
            uprising= elo1
        if equipe1 == 4407 : #valliantwin 
            mahyem= elo1
        if equipe1 == 4408 : #valliantwin 
            dragon= elo1
        if equipe1 == 4404 : #valliantwin 
            choc= elo1
        if equipe1 == 4409 : #valliantwin 
            dynastie= elo1
        if equipe1 == 4523 : #valliantwin 
            fuel= elo1
        if equipe1 == 4525 : #valliantwin 
            outlaw= elo1
                
        if equipe2 == 4405 : #valliantwin 
            vaillant =elo2
        if equipe2 == 4406 : #valliantwin 
            gladiator =elo2
        if equipe2 == 4524 : #valliantwin 
            fusion =elo2
        if equipe2 == 4403 : #valliantwin 
            excelsior =elo2
        if equipe2 == 4410 : #valliantwin 
            spitfire =elo2
        if equipe2 == 4402 : #valliantwin 
            uprising =elo2
        if equipe2 == 4407 : #valliantwin 
            mahyem =elo2
        if equipe2 == 4408 : #valliantwin 
            dragon =elo2
        if equipe2 == 4404 : #valliantwin 
            choc =elo2
        if equipe2 == 4409 : #valliantwin 
            dynastie =elo2
        if equipe2 == 4523 : #valliantwin 
            fuel =elo2
        if equipe2 == 4525 : #valliantwin 
            outlaw =elo2
        ajouterlist(i )
afficherelo()

axe_x = []
axe_y = []
for e in listelo:
    axe_x.append(e[0])
    axe_y.append(e[1])



plt.plot(axe_x,axe_y)
plt.legend(["val","gla","fus","exe","spit","upr","meh","dra","dyn","fue","out"],loc ="lower left")
plt.show()
     
        
    
        
        


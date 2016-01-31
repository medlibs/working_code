from __future__ import division
import random
import math

level_1_type = ['acidosis', 'alkalosis']
level_2_type = ['metabolic', 'respiratory']
level_3_type = ['compensated', 'uncompensated']
level_3a_type = ['acute', 'chronic']
level_4_type = ['gap', 'normal gap']
#level_5_type = ['mixed', 'unmixed']

level_1 = random.sample(level_1_type, 1)[0]
level_2 = random.sample(level_2_type, 1)[0]
level_3 = random.sample(level_3_type, 1)[0]
level_3a = random.sample(level_3a_type, 1)[0]
level_4 = random.sample(level_4_type, 1)[0]

print "level_1", level_1
print "level_2", level_2
if level_2 == 'respiratory' and level_3 == 'compensated': print level_3a
print "level_3", level_3
if level_1 == 'acidosis' and level_2 == 'metabolic': print level_4

def HH(HCO3, pCO2):
    pH = round(6.1+math.log(HCO3/(.03*pCO2),10),2)
    return pH

if level_1 == 'acidosis':
    pH = round(random.uniform(6.8, 7.34),2)
    RR = random.randint(12,18)
    if level_2 == 'metabolic':
        pCO2 = random.uniform(35,45)
        HCO3 = round(.03*pCO2*(10**(pH-6.1)),0)
        if level_3 == 'compensated':
            pCO2 = 1.5*HCO3+8+random.randint(-2,2)
            pH = HH(HCO3, pCO2)
            RR = random.randint(20,30)
        if level_4 == 'gap':
            Na = 0
            Cl = 0
            while Na-Cl < 17+bicarb:                
                Na = random.randint(135,145)
                Cl = random.randint(95, 105)
            gap = Na-HCO3-Cl
            mix_metric = (gap-12)/(24-HCO3)
            if mix_metric < 1 and mix_metrix > 0.4:
                level_5 = 'mixed'
            elif mix_metric > 1 and mix_metric < 2:
                level_5 = 'not'
        else:
            Na = random.randint(135,145)
            gap = 12+random.randint(-4,4)
            Cl = Na-HCO3-gap
            
    else:
        HCO3 = random.randint(22,28)
        pCO2 = round(HCO3/(.03*(10**(pH-6.1))),0)
        if level_3 == 'compensated':

            if level_3a == 'acute':
                multiplier = 1
            else:
                multiplier = 4                
            HCO3 = round(24+multiplier*(pCO2-40)/10,0)
            pH = HH(HCO3, pCO2)
else:
    pH = round(random.uniform(7.36,7.8),2)
    RR = random.randint(12,18)
    if level_2 == 'metabolic':
        pCO2 = random.uniform(35,45)
        HCO3 = round(.03*pCO2*(10**(pH-6.1)),0)
        if level_3 == 'compensated':
            pCO2 = 0.7*HCO3+20+random.randint(-5,5)
            pH = HH(HCO3, pCO2)
            RR = random.randint(6,11) #?
    else:
        HCO3 = random.randint(22,28)
        pCO2 = round(HCO3/(.03*(10**(pH-6.1))), 0)
        if level_3 == 'compensated':
            first_run = 1
            if level_3a == 'acute':
                while first_run == 1 or HCO3 < 18:
                    first_run = 0
                    multiplier = random.uniform(1,2)
                    
            else:
                while first_run == 1 or HCO3 < 12:
                    first_run = 0
                    multiplier = random.uniform(4,5)
                    HCO3 = round(24-multiplier*(40-pCO2/10),1)
            pH = HH(HCO3, pCO2)

print 'pH: ', str(pH)
print 'HCO3: ', str(HCO3)
print 'pCO2: ', str(pCO2)
print 'RR: ', str(RR)
if level_1 == 'acidosis' and level_2 == 'metabolic':
    print 'gap: ', gap
    print 'Na: ', Na
    print 'Cl: ', Cl
    

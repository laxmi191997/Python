d1={'Python':3,'Java':6,'Perl':2}
d2={'C++':5,'AngularJS':3,'Python':5}
d={}
d['Python']=d1['Python']+d2['Python']
#print(d)
d1.update(d)
#print(d1)
for each in d1:
    if each not in d2:
        d2.update(d1)
print(d2)






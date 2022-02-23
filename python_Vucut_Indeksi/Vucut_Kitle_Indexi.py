print("INDEKS HESAPLAMA")
boy = float(input("Boy ():"))
kilo = int(input("Kilo (kg):"))

if boy<4:
      
    endeks  = kilo/(boy*boy)
    altnk = (18.5)*((boy)*(boy))
    ustnk = (24.99)*((boy)*(boy))
    if endeks <18:
        print("\n zayıf VKİ:{}".format(endeks))
        print("\n {} - {} kilolari arasinda olmalisiniz".format(altnk,ustnk))
    elif endeks >= 18 and endeks <25:
        print("\n normal VKİ:{}".format(endeks))
    elif endeks >= 25 and endeks <30:
        print("\n kilolu VKİ:{}".format(endeks))
        print("\n {} - {} kilolari arasinda olmalisiniz".format(altnk,ustnk))
    else:
        print("\n obez VKİ:{}".format(endeks))
        print("\n {} - {} kilolari arasinda olmalisiniz".format(altnk,ustnk))
    
else:
    
    endeks  = kilo/((boy/100)*(boy/100))
    altnk = (18.5)*((boy/100)*(boy/100))
    ustnk = (24.99)*((boy/100)*(boy/100))
    if endeks <18:
        print("\n zayıf VKİ:{}".format(endeks))
        print("\n {} - {} kilolari arasinda olmalisiniz".format(altnk,ustnk))
        
    elif endeks >= 18 and endeks <25:
        print("\n normal VKİ:{}".format(endeks))
    elif endeks >= 25 and endeks <30:
        print("\n kilolu VKİ:{}".format(endeks))
        print("\n {} - {} kilolari arasinda olmalisiniz".format(altnk,ustnk))
    else:
        print("\n obez VKİ:{}".format(endeks))
        print("\n {} - {} kilolari arasinda olmalisiniz".format(altnk,ustnk))
    

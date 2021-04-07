

obje_ori = 'Extrude018'
lttr = 'G'

obje = App.ActiveDocument.getObject(obje_ori)

for c in range(1, 12):
    obje_cp = App.ActiveDocument.copyObject(obje, True)
    obje_cp.Label = 'Extrusion {}{:02d}'.format(lttr, c+1)
    obje_cp.Placement = App.Placement(App.Vector(9,0,0), App.Rotation(0,0,0), App.Vector(0,0,0)).multiply(obje_cp.Placement)
    nameSubElement = obje_cp.OutList[0].Name
    chaine = '{}{:02d}'.format(lttr, c+1)
    lab = '{} string'.format(chaine)
    App.ActiveDocument.getObject(nameSubElement).String = chaine
    App.ActiveDocument.getObject(nameSubElement).Label = chaine
    obje = obje_cp


App.activeDocument().recompute()




#############################################
#############################################


for obje in App.ActiveDocument.Objects:
    if obje.Label.startswith('Extrusion'):
        subElement = obje.OutList[0]
        txt = subElement.String
        if re.search('.0.', txt):
        	subElement.String = '{}{}'.format(txt[0], txt[2])
        obje.Placement = App.Placement(App.Vector(0, 1, 0), App.Rotation(0, 0, 0), App.Vector(0, 0, 0)).multiply(obje.Placement)





#############################################
#############################################


for obje in App.ActiveDocument.Objects:
    if obje.Label.startswith('Extrusion'):
        subElement = obje.OutList[0]
        subElement.Size = '2 mm'

App.activeDocument().recompute()


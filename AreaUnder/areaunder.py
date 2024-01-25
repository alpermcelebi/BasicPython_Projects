v = eval(input())
nv = [(v[0][0], abs(v[0][1])), (v[1][0], abs(v[1][1])), (v[2][0], abs(v[2][1])), (v[3][0], abs(v[3][1]))]
nl = sorted(nv)
nnl = [(nl[0]), (nl[1]), (nl[3]), (nl[2])] if nl[3][0] == nl[2][0] else nl

directlylinked = abs(nv.index(nl[0]) - nv.index(nl[3])) == 1 or abs(nv.index(nl[0]) - nv.index(nl[3])) == 3
directlylinked2 = abs(nv.index(nnl[0]) - nv.index(nnl[3])) == 1 or abs(nv.index(nnl[0]) - nv.index(nnl[3])) == 3
dlslope = (nnl[3][1] - nnl[0][1]) / (nnl[3][0] - nnl[0][0])
dlc = nnl[0][1] - (dlslope * nnl[0][0])

beneaththeline = (nnl[1][1] > ((dlslope * nnl[1][0]) + (dlc))) or (nnl[2][1] > ((dlslope * nnl[2][0]) + (dlc)))
undertheline =(nnl[1][1] < ((dlslope * nnl[1][0]) + (dlc))) or (nnl[2][1] < ((dlslope * nnl[2][0]) + (dlc)))
lineisbetween = (nnl[1][1] > ((dlslope * nnl[1][0]) + (dlc))) and (nnl[2][1] < ((dlslope * nnl[2][0]) + (dlc))) or (nnl[1][1] < ((dlslope * nnl[1][0]) + (dlc))) and (nnl[2][1] > ((dlslope * nnl[2][0]) + (dlc)))

isslope = (nl[2][1] - nl[0][1]) / (nl[2][0] - nl[0][0]) 
isc = nl[2][1] - (isslope * nl[2][0])
isline = (nl[1][1] > ((isslope * nl[1][0]) + (isc)))

kslope = (nl[3][1] - nl[1][1]) / (nl[3][0] - nl[1][0]) 
kc = nl[3][1] - (kslope * nl[3][0])
kline = (nl[2][1] > ((kslope * nl[2][0]) + (kc)))

sbu = 0.5*(abs((nl[0][0]*nl[1][1] + nl[1][0]*nl[3][1] + nl[3][0]*nl[0][1]) - (nl[1][0]*nl[0][1] + nl[3][0]*nl[1][1] + nl[0][0]*nl[3][1])))
biu = 0.5*(abs((nl[1][0]*nl[2][1] + nl[2][0]*nl[3][1] + nl[3][0]*nl[1][1]) - (nl[2][0]*nl[1][1] + nl[3][0]*nl[2][1] + nl[1][0]*nl[3][1])))
sbi = 0.5*(abs((nl[0][0]*nl[1][1] + nl[1][0]*nl[2][1] + nl[2][0]*nl[0][1]) - (nl[1][0]*nl[0][1] + nl[2][0]*nl[1][1] + nl[0][0]*nl[2][1])))
siu = 0.5*(abs((nl[0][0]*nl[2][1] + nl[2][0]*nl[3][1] + nl[3][0]*nl[0][1]) - (nl[2][0]*nl[0][1] + nl[3][0]*nl[2][1] + nl[0][0]*nl[3][1])))
case1 = (nnl[2][0] == nnl[3][0]) and (abs(nv.index(nnl[3])-nv.index(nnl[1])) == 1 or abs(nv.index(nnl[3])-nv.index(nnl[1])) == 3) and (abs(nv.index(nnl[2])-nv.index(nnl[1])) != 1 and abs(nv.index(nnl[2])-nv.index(nnl[1])) != 3)
case2 = isline and (abs(nv.index(nnl[3])-nv.index(nnl[1])) == 1 or abs(nv.index(nnl[3])-nv.index(nnl[1])) == 3) and (nnl[3][0] != nnl[2][0])
case3 = nnl[2][0] == nnl[1][0] and (abs(nv.index(nnl[0])-nv.index(nnl[2])) == 1 or abs(nv.index(nnl[0])-nv.index(nnl[2])) == 3)
case3_2 = nnl[2][0] == nnl[1][0] and (abs(nv.index(nnl[0])-nv.index(nnl[1])) == 1 or abs(nv.index(nnl[0])-nv.index(nnl[1])) == 3)
case4 = kline and (abs(nv.index(nnl[0])-nv.index(nnl[1])) != 1 and abs(nv.index(nnl[0])-nv.index(nnl[1])) != 3)
casecheck = not ( case1 or case2 or case3 or case3_2 or case4)

if directlylinked or directlylinked2:

	if beneaththeline:

		if not case1:
			area = (nnl[0][1] + nnl[3][1]) * (0.5) * (abs(nnl[3][0] - nnl[0][0]))
			print("%.2f" % (area))
		elif case1:
			area_1 = 0.5*(nnl[0][1]+nnl[1][1])*(abs(nnl[0][0]-nnl[1][0])) + 0.5*(nnl[1][1]+nnl[3][1])*(abs(nnl[1][0]-nnl[3][0]))
			print("%.2f" % (area_1))

	elif undertheline:

		if case2:
			var1 = 0.5*(nl[3][1]+nl[0][1])*(abs(nl[3][0]-nl[0][0]))
			var2 = var1 - sbi - sbu
			print("%.2f" % (var2))
		elif case3:
			var3  = 0.5*(nl[3][1]+nl[0][1])*(abs(nl[3][0]-nl[0][0]))
			var4 = var3 - siu - biu
			print("%.2f" % (var4))
		elif case3_2:
			var5 = 0.5*(nl[3][1]+nl[0][1])*(abs(nl[3][0]-nl[0][0]))
			var6 = var5 - sbi - siu
			print("%.2f" % (var6))
		elif case4:
			var7 = 0.5*(nl[3][1]+nl[0][1])*(abs(nl[3][0]-nl[0][0]))
			var8 = var7 - biu - siu
			print("%.2f" % (var8))
		elif casecheck and isline: 
			var9 = 0.5*(nl[3][1]+nl[0][1])*(abs(nl[3][0]-nl[0][0]))
			var10 = var9 - sbu - biu
			print("%.2f" % (var10))
		elif casecheck and not (isline):
			var11 = 0.5*(nl[3][1]+nl[0][1])*(abs(nl[3][0]-nl[0][0]))
			var12 = var11 - sbi - siu
			print("%.2f" % (var12))

elif lineisbetween :

	if nnl[2][1]>nnl[1][1]:
		aarea = 0.5*(nnl[0][1]+nnl[1][1])*(abs(nnl[0][0]-nnl[1][0])) + 0.5*(nnl[1][1]+nnl[3][1])*(abs(nnl[1][0]-nnl[3][0]))
		print("%.2f" % (aarea))
	elif nnl[1][1]>nnl[2][1]:
		barea = 0.5*(nnl[0][1]+nnl[2][1])*(abs(nnl[0][0]-nnl[2][0])) + 0.5*(nnl[2][1]+nnl[3][1])*(abs(nnl[2][0]-nnl[3][0]))
		print("%.2f" % (barea))

elif not(lineisbetween or directlylinked2 or directlylinked):

	if nnl[2][1]>nnl[1][1]:
		carea = 0.5*(nnl[0][1]+nnl[1][1])*(abs(nnl[0][0]-nnl[1][0])) + 0.5*(nnl[1][1]+nnl[3][1])*(abs(nnl[1][0]-nnl[3][0]))
		print("%.2f" % (carea))
	elif nnl[1][1]>nnl[2][1]:
		darea = 0.5*(nnl[0][1]+nnl[2][1])*(abs(nnl[0][0]-nnl[2][0])) + 0.5*(nnl[2][1]+nnl[3][1])*(abs(nnl[2][0]-nnl[3][0]))
		print("%.2f" % (darea))
	else:
		farea = 0.5*(nnl[0][1]+nnl[2][1])*(abs(nnl[0][0]-nnl[2][0])) + 0.5*(nnl[2][1]+nnl[3][1])*(abs(nnl[2][0]-nnl[3][0]))
		print("%.2f" % (farea))
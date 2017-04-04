def export(acc_t,doc_t,npp,arr2, dat):
	arr = []
	for ind in arr2:
		bf = (ind[0],ind[1], str(round(float(ind[2]),2)).replace('.',','))
		arr.append(bf)
	from xml.dom import minidom
	doc = minidom.Document()
	dcmt = doc.createElement('DOCUMENT')
	doc.appendChild(dcmt)

	filial = doc.createElement('FILIAL')
	text = doc.createTextNode('2')
	filial.appendChild(text)
	dcmt.appendChild(filial)

	acc_type = doc.createElement('ACC_TYPE')
	text = doc.createTextNode(acc_t)
	acc_type.appendChild(text)
	dcmt.appendChild(acc_type)

	doc_type = doc.createElement('DOC_TYPE')
	text = doc.createTextNode(doc_t) 
	doc_type.appendChild(text)
	dcmt.appendChild(doc_type)

	date_period = doc.createElement('DATE_PERIOD')
	text = doc.createTextNode(dat[:4]+'-'+dat[4:]+'-01')
	date_period.appendChild(text)
	dcmt.appendChild(date_period)
	contragent = []
	code_mo = []
	partition = []
	id = []
	part_type = []
	sum_pos = []
	mo_buf = ''
	h = -1
	for idx, val in enumerate(arr):
		if mo_buf != val[0]:
			contragent.append(doc.createElement('CONTRAGENT'))
			h+=1
			print (idx,mo_buf,val[0])
			code_mo.append(doc.createElement('CODE_MO'))
			text = doc.createTextNode(val[0])
			code_mo[len(code_mo)-1].appendChild(text)
			contragent[h].appendChild(code_mo[len(code_mo)-1])
			mo_buf = val[0]
		partition.append(doc.createElement('PARTITION'))
		id.append(doc.createElement('ID'))
		text = doc.createTextNode(str(idx))
		id[len(id)-1].appendChild(text)
		partition[len(partition)-1].appendChild(id[len(id)-1])
		
		part_type.append(doc.createElement('PART_TYPE'))
		text = doc.createTextNode(str(val[1]))
		part_type[len(part_type)-1].appendChild(text)
		partition[len(partition)-1].appendChild(part_type[len(part_type)-1])	

		sum_pos.append(doc.createElement('SUM_POS'))
		text = doc.createTextNode(str(val[2]))
		sum_pos[len(sum_pos)-1].appendChild(text)
		partition[len(partition)-1].appendChild(sum_pos[len(sum_pos)-1])	
		contragent[h].appendChild(partition[len(partition)-1])
		if idx < len(arr)-1:
			if arr[idx+1][0] != arr[idx][0]:
				print(contragent[h])
				dcmt.appendChild(contragent[h])
		if idx == len(arr)-1:		
			dcmt.appendChild(contragent[h])
	xml_str = doc.toprettyxml(indent = "	", newl = "\n", encoding = "WINDOWS-1251")
	#xml_str = doc.toprettyxml(indent = "	")
	strok = "d:\\2_"+dat+"_"+str(acc_t)+"_"+str(doc_t)+"_"+str(npp)+".xml"
	with open(strok,"wb") as f:
		f.write(xml_str)


#оригинал
'''from xml.dom import minidom
doc = minidom.Document()
dcmt = doc.createElement('document')
doc.appendChild(dcmt)

filial = doc.createElement('filial')
text = doc.createTextNode('32')
filial.appendChild(text)
dcmt.appendChild(filial)

acc_type = doc.createElement('acc_type')
text = doc.createTextNode('1')
acc_type.appendChild(text)
dcmt.appendChild(acc_type)

doc_type = doc.createElement('doc_type')
text = doc.createTextNode('1')
doc_type.appendChild(text)
dcmt.appendChild(doc_type)

date_period = doc.createElement('date_period')
text = doc.createTextNode('2016-01-01')
date_period.appendChild(text)
dcmt.appendChild(date_period)
arr = [('020158', 6, 0), ('020158', 5, 328310.7), ('020159', 6, 186405), ('020159', 5, 0), ('020160', 5, 346534.2), ('020160', 6, 0)]
contragent = []
code_mo = []
partition = []
id = []
part_type = []
sum_pos = []
mo_buf = ''

h = -1
for idx, val in enumerate(arr):
	if mo_buf != val[0]:
		contragent.append(doc.createElement('contragent'))
		h+=1
		print (idx,mo_buf,val[0])
		code_mo.append(doc.createElement('code_mo'))
		text = doc.createTextNode(val[0])
		code_mo[len(code_mo)-1].appendChild(text)
		contragent[h].appendChild(code_mo[len(code_mo)-1])
		mo_buf = val[0]

	partition.append(doc.createElement('partition'))
	
	id.append(doc.createElement('id'))
	text = doc.createTextNode(str(idx))
	id[len(id)-1].appendChild(text)
	partition[len(partition)-1].appendChild(id[len(id)-1])
	
	part_type.append(doc.createElement('part_type'))
	text = doc.createTextNode(str(val[1]))
	part_type[len(part_type)-1].appendChild(text)
	partition[len(partition)-1].appendChild(part_type[len(part_type)-1])	

	sum_pos.append(doc.createElement('sum_pos'))
	text = doc.createTextNode(str(val[2]))
	sum_pos[len(sum_pos)-1].appendChild(text)
	partition[len(partition)-1].appendChild(sum_pos[len(sum_pos)-1])	
	contragent[h].appendChild(partition[len(partition)-1])
	if idx < len(arr)-1:
		if arr[idx+1][0] != arr[idx][0]:
			print(contragent[h])
			dcmt.appendChild(contragent[h])
			
	if idx == len(arr)-1:		
		dcmt.appendChild(contragent[h])

xml_str = doc.toprettyxml(indent = " ")
with open("d:\\text_xml.xml","w") as f:
	f.write(xml_str)'''

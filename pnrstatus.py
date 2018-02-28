import pnrapi

'''

@author ssaxena36

'''

p = pnrapi.PnrApi("8729696880")  # 10-digit PNR Number
if p.request() == True:
    print(p.get_json())
else:
	print(p.error)

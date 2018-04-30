import requests
import json
from variant_challenge import abbreviated_list

# Our abbreviated list has CHROM POS ID REF ALT QUAL TYPE DP AO AO/DP, and we need to get it in the correct format for the api
# So, we need the CHROM POS REF ALT separated by a "-"
format_api = []

for item in abbreviated_list:
	format_api += [str(item[0])+ "-" + str(item[1]) + "-" + str(item[3]) + "-" + str(item[4])]

api_freq_data = []

# Here, we loop through all of the different variants in the correct format for the api
for item in format_api:
	url = 'http://exac.hms.harvard.edu/rest/variant/variant/%s' % item
	response = requests.get(url)
	data_from_url = response.json()
	if 'allele_freq' in data_from_url:
		api_freq_data += [[item, data_from_url['allele_freq'], data_from_url['rsid']]]

#print(api_freq_data)
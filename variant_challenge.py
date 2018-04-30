from __future__ import division

with open("Challenge_data.vcf") as f:
	data_lines = f.readlines()

data_lines = [line.strip("\n") for line in data_lines] 
data_lines = [line.split("\t") for line in data_lines]

# This accounts for the format notes in the begining and removes them
without_formatting_info_lines = []

for item in data_lines:
	if "#CHROM" not in item:
		if len(item) == 11:
			without_formatting_info_lines += [item]


# Now, without the formatting notes in the begining, we are able to parse through the info which is located at index 7
for item in without_formatting_info_lines:
	item[7] = item[7].split(";")

# After we have all the info split up, we can look at what specific annotations we are interested in
for item in without_formatting_info_lines:
	for value in item[7]:
		if "TYPE=" in value:
			item.append(value)
		if "DP=" in value:
			item.append(value)
		# Note that when searching just "AO" you also get the "PAO", but I account for this later
		if "AO=" in value:
			item.append(value)

# Now we can get rid of the extra info and format for the purposes of this assignment:
abbreviated_list = []

for item in without_formatting_info_lines:
	# We put it into a list that will look like: CHROM POS ID REF ALT QUAL TYPE DP AO
	abbreviated_list += [[item[0], item[1], item[2], item[3], item[4], item[5], item[14], item[12], item[11]]]

# Next, I go through and get rid of the annotation abbreviations (TYPE, DP, AO) so that I only have the value in the new columns
for item in abbreviated_list:
	# This is to get the TYPE alone
	item[6] = item[6].split("=")
	item[6] = item[6][1]
	# Now that we have the TYPE alone, since we are only looking at the most deleterious value, we account for that here
	item[6] = item[6].split(",")
	item[6] = item[6][0]
	# This is to get the DP alone
	item[7] = item[7].split("=")
	item[7] = item[7][1]
	# This is to get the AO alone
	item[8] = item[8].split("=")
	item[8] = item[8][1]
	# Now that we have the AO alone, since we are only looking at the most deleterious value, we account for that here
	item[8] = item[8].split(",")
	item[8] = item[8][0]




# Now, to get the percentage of reads supporting the variant, we do: AO/DP, and add that to our list

for item in abbreviated_list:
	reads_supporting_variant = int(item[8]) / int(item[7])
	# For simplification, I only went out to 3 decimal points for the percentage
	item.append("%.3f" % reads_supporting_variant)

#print len(abbreviated_list)

# Now, from our file where we searched the api for frequencies, we look at that table which is currently in the format: [CHROM-POS-REF-ALT, FREQ]
from api_freq_data import api_freq_data

# Note that from our initial search of the api we only got 3376 freq for the 6977, so we will add those to our final table here
for value in api_freq_data:
	for item in abbreviated_list:
		if (str(item[0])+ "-" + str(item[1]) + "-" + str(item[3]) + "-" + str(item[4])) == value[0]:
			# Again, I only go to 3 decimal points for simplicity
			item.append("%.3f" % value[1])
			item[2] = value[2]

# Here, I just add a null value if we weren't able to find the frequency using the api
for item in abbreviated_list:
	if len(item) != 11:
		item.append(".")

# Finally, we have an abbreviated list that has the following format:
#	CHROM POS ID REF ALT QUAL TYPE DP AO (AO/DP) EXAC_FREQ
# And we print this out in a tab-deliminated table while also adding a title line:
print("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tTYPE\tDP\tAO\t(AO/DP)\tEXAC_FREQ")

for i in abbreviated_list:
	print(*i, sep="\t")







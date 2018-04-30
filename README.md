# tempus-challenge

Hello! I have heavily notated the code attached, I will briefly outline the files I have attached here:

1. variant_code.py 
  This is the main coding for this challenge, which addresses points 1-3 on the Tempus Challenge sheet
  
2. Challenge_data.vcf
  This is the given vcf file
  
3. exac_api_code.py
  This is where I use the ExAC api code to address point 4 on the Tempus Challenge, I choose to do this separately because the run time was taking a while and I didn't want to have to run through all of my previous code as well.
  
4. api_freq_data.py
  As mentioned for (2), since I didn't want to keep running the api, I put my tailored results into a list that I manipulated back in the main code (1)
  
5. variant_challenge_table.txt
  This is the final output from the code, which has the following tables:
    #CHROM  POS ID  REF ALT QUAL  TYPE  DP  AO  AO/DP EXAC_FREQ

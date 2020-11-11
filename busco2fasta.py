import sys
import argparse
import os
import shutil

def get_list_of_busco_dirs(results_dir):
	# get list of busco_dirs
	busco_dir_list = []
	for busco_dir in os.listdir(results_dir):
		busco_dir_list.append(busco_dir)
	# print output
	print("[STATUS] Found " + str(len(busco_dir_list)) + " BUSCO runs in input directory ('" + results_dir.replace("/","") + "'):")
	for busco_dir in busco_dir_list:
		print("[STATUS] \t- " + busco_dir)
	# return list
	return busco_dir_list

def count_single_copy_buscos(results_dir, busco_dir_list, suffix):
	scb_count_dict = {}
	for busco_dir in busco_dir_list:
		for item in os.listdir(results_dir + busco_dir):
			if item.startswith("run_"):
				scb_file_list = os.listdir(results_dir + busco_dir + "/" + item + "/busco_sequences/single_copy_busco_sequences/")
				for scb_file in scb_file_list:
					if scb_file.endswith(suffix):
						scbID = scb_file.replace(suffix, "")
						try:
							scb_count_dict[scbID] += 1
						except KeyError:
							scb_count_dict[scbID] = 1
	return scb_count_dict

def get_usable_buscos(scb_count_dict, proportion, busco_dir_list):
	n_taxa = len(busco_dir_list)
	min_taxon_count = int(round(n_taxa * proportion, 0))
	usable_scb_list = []
	print("[STATUS] Selecting BUSCOs present in ≥ " + str(min_taxon_count) + " taxa...")
	for scbID, count in scb_count_dict.items():
		if count >= min_taxon_count:
			usable_scb_list.append(scbID)
	return usable_scb_list

def parse_fasta(fasta_file):
	with open(fasta_file) as fasta:
		fasta_dict = {}
		for line in fasta:
			if line.startswith(">"):
				header = line.rstrip("\n")
				fasta_dict[header] = ''
			else:
				fasta_dict[header] += line.rstrip("\n")
	return fasta_dict

def create_output_fastas(results_dir, busco_dir_list, usable_scb_list, suffix, outdir):
	print("[STATUS] Writing " + str(len(usable_scb_list)) + " " + seqtype + " FASTA files to output directory ('" + (outdir) + "')...") 
	for busco_dir in busco_dir_list:
			for item in os.listdir(results_dir + busco_dir):
				if item.startswith("run_"):
					scb_file_list = os.listdir(results_dir + busco_dir + "/" + item + "/busco_sequences/single_copy_busco_sequences/")
					for scb_file in scb_file_list:
						full_path_to_scb_file = results_dir + busco_dir + "/" + item + "/busco_sequences/single_copy_busco_sequences/" + scb_file
						scbID = scb_file.split(".")[0]
						if scbID in usable_scb_list and scb_file.endswith(suffix):
							fasta_dict = parse_fasta(full_path_to_scb_file)
							with open(outdir + "/" + scbID + suffix, 'a') as outfile:
								for header, sequence in fasta_dict.items():
		 							outfile.write(">" + busco_dir +  "." + header.replace(">", "").split(" ")[0] + "\n")
	 								outfile.write(sequence + "\n")	

if __name__ == "__main__":
	SCRIPT = "busco2fasta.py"
	### argument set up 
	# set up
	parser = argparse.ArgumentParser()
	parser.add_argument("-b", "--busco_dir", type=str, help = "directory containing a set BUSCO results directories (e.g. one per taxon)", required=True)
	parser.add_argument("-o", "--outdir", type=str, help = "output directory for FASTAs (default: b2f_output)", default="b2f_output")
	parser.add_argument("-s", "--seqtype", type=str, help = "your chosen sequence type (defaut: protein)", choices={"protein", "nucleotide"}, default="protein")
	parser.add_argument("-p", "--proportion", type=float, help = "proportion of taxa required for a given BUSCO to be output as FASTA (default: 1.0)", default=1.0)
	args = parser.parse_args()
	results_dir = args.busco_dir
	seqtype = args.seqtype
	proportion = args.proportion
	outdir = args.outdir
	# add slash to results dir if necessary
	if not results_dir.endswith("/"):
		results_dir = results_dir + "/"
	# get suffix based on seqtype	
	if seqtype == 'protein':
		suffix = ".faa"
	else:
		suffix = ".fna"
	# proportion
	print("busco2fasta.py parameters:")
	print("\tinput_dir: " + results_dir)
	print("\toutput_dir: " + outdir)
	print("\tseqtype: " + seqtype)
	print("\tproportion: " + str(proportion))
	print("")
	if os.path.exists(outdir):
		print("[WARING] Removing existing output directory ('" + outdir + "') and its contents...")
		shutil.rmtree(outdir)
	os.mkdir(outdir)
	### run functions	
	busco_dir_list = get_list_of_busco_dirs(results_dir)
	scb_count_dict = count_single_copy_buscos(results_dir, busco_dir_list, suffix)
	usable_scb_list = get_usable_buscos(scb_count_dict, proportion, busco_dir_list)
	create_output_fastas(results_dir, busco_dir_list, usable_scb_list, suffix, outdir)
	print("[STATUS] Successfuly wrote " + str(len(usable_scb_list)) + " " + seqtype + " FASTA files. Run complete.")
					






# busco2fasta

A script to turn a set of BUSCO results into a directory of multisequence FASTA files

Note: this script currently doesn't work on BUSCO runs created using the `-m transcriptome` option because the output lacks a `single_copy_busco_sequences` directory. If you want to use it on a transcriptome assembly, you should extract protein sequences (e.g. using TransDecoder) and run BUSCO using the `-m proteins` mode. 

```
usage: busco2fasta.py [-h] -b BUSCO_DIR [-o OUTDIR] [-s {protein,nucleotide}]
                      [-p PROPORTION]

optional arguments:

  -h, --help            show this help message and exit
  
  -b BUSCO_DIR, --busco_dir BUSCO_DIR
  
                        directory containing a set BUSCO results directories (e.g. one per taxon)
                        
  -o OUTDIR, --outdir OUTDIR
                        output directory for FASTAs (default: b2f_output)
                        
  -s {protein,nucleotide}, --seqtype {protein,nucleotide}
                        your chosen sequence type (default: protein)
                        
  -p PROPORTION, --proportion PROPORTION
                        proportion of taxa required for a given BUSCO to be output as FASTA (default: 1.0)
```                        

# busco2fasta

A script to turn a set of BUSCO results into a directory of multisequence FASTA files

```
usage: busco2fasta.py [-h] -b BUSCO_DIR [-o OUTDIR] [-s {protein,nucleotide}]
                      [-p PROPORTION]

optional arguments:

  -h, --help            show this help message and exit
  
  -b BUSCO_DIR, --busco_dir BUSCO_DIR
  
                        directory containing a set of BUSCO results directories (e.g. one per taxon)
                        
  -o OUTDIR, --outdir OUTDIR
                        output directory for FASTAs (default: b2f_output)
                        
  -s {protein,nucleotide}, --seqtype {protein,nucleotide}
                        your chosen sequence type (default: protein)
                        
  -p PROPORTION, --proportion PROPORTION
                        proportion of taxa required for a given BUSCO to be output as FASTA (default: 1.0)
```

Note that BUSCO_DIR should contain a set of BUSCO results directories only (e.g. no log files or other directories). Here is an example BUSCO_DIR `busco_results` the BUSCO results for three nematode species: 

```
busco_results/
├── ancylostoma_caninum/
│   ├── logs/
│   ├── run_nematoda_odb10/
│   └── short_summary.specific..ancylostoma_caninum.PRJNA72585.WBPS17.genomic.fa_busco_nematoda.txt
├── ancylostoma_ceylanicum/
│   ├── logs/
│   ├── run_nematoda_odb10/
│   └── short_summary.specific..ancylostoma_ceylanicum.PRJNA231479.WBPS17.genomic.fa_busco_nematoda.txt
├── ancylostoma_duodenale/
│   ├── logs/
│   ├── run_nematoda_odb10/
│   └── short_summary.specific..ancylostoma_duodenale.PRJNA72581.WBPS17.genomic.fa_busco_nematoda.txt
```

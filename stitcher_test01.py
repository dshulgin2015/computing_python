#!/usr/bin/env python
import argparse
import pysam
import string
import vcf
import os
import pandas as pd


# IMPORTANT NOTES regarding import
# Note: I think the pyvcf module is now installed and imported as vcf

# To Do - Problem Stage #1:
# 1) Add different arguments (pop1 and pop2 - these are name of the populations and will be added as header in the output file)
# 2) Add arguments (vcf1 and vc2) - these are vcf files that we will provide
# 3) Add argument for the name of output file

# 4a) Create an output file which should contain following headers
# contig    pos id  ref alt ref-freq-My ref-freq-Sp alt-A-freq-My   alt-A-freq-Sp
# the headers are separted by tab
# 4b) write the following values from vcf files: contig (from CHR), pos, id, ref - without any changes
# When merging information from two vcfs the the intersecting values can be kept and non intersecting values can be added
# 4c) Read the AF values in the vcf1 and vcf2 files and write the
# corresponding values

def main():
    # Arguments passed
    parser = argparse.ArgumentParser()
    # required  # Description - parser.add_argument adds the argument to the
    # program which is required in stage 1.
    parser.add_argument("--vcf1",
                        help="sorted vcf file (comma separated if there are multiple vcf's) containing allele frequency for reference and alternate allele for population 1",
                        required=True)
    parser.add_argument("--vcf2",
                        help="sorted vcf file (comma separated if there are multiple vcf's) containing allele frequency for reference and alternate allele for population 2",
                        required=True)
    parser.add_argument(
        "--pop1", help="Sample name for population 1", required=True)
    parser.add_argument(
        "--pop2", help="Sample name for population 2", required=True)
    parser.add_argument(
        "--output", help="Name of the output file", required=False)

    # debug / development / reporting
    parser.add_argument(
        "--chr", default="", help="Restrict haplotype stitching to a specific chromosome.")

    global args
    args = parser.parse_args()

    # setup
    version = "0.6"
    print("")
    print("##################################################")
    print("              Welcome to phase_stitcher")
    print("  Author: someone ")
    print("##################################################")
    print("")

    global devnull
    devnull = open(os.devnull, 'w')

    # checks if the required files (vcfs) are provided or not
    check_files = [args.vcf1, args.vcf2]

    # for xfile in check_files:
    #     if xfile != "":
    #         if not os.path.isfile(xfile):
    #             if __name__ == '__main__':
    #                 fatal_error(
    #                     "File: %s not found." % (xfile))  # reports error message if the checked files isn't found

    # # Now, load the allele frequency VCF file
    # if args.vcf1 != "":
    #     if os.path.isfile(args.vcf1) == True:
    #         vcf_af = vcf.Reader(filename=args.vcf1)
    #     else:
    #         fatal_error(
    #             "Allele frequency VCF (--vcf) specified does not exist.")
    pop1 = pysam.VariantFile(check_files[0], "r").fetch()
    pop2 = pysam.VariantFile(check_files[1], "r").fetch()
    merged_df = pd.read_csv("expected_st_1.txt",
                            delim_whitespace=True, header=0)

    columns = ['contig', 'pos', 'id', 'ref', 'alt', 'ref-freq-' + str(args.pop1),
               'ref-freq-' + str(args.pop2), 'alt-A-freq-' + str(args.pop1), 'alt-A-freq-' + str(args.pop2)]
    ref1 = []
    alt1 = []
    k = 0
    for rec in pop1:
        k = k + 1
        if k < 39:
            ref1.append(rec.ref)
            alt1.append(rec.alts[0])

    # adding 2
    ref2 = []
    alt2 = []
    k = 0
    for rec in pop2:
        k = k + 1
        if k < 39:
            ref2.append(rec.ref)
            alt2.append(rec.alts[0])

    # appending to existig expected_st_1
    merged_df[columns[5]] = ref1
    merged_df[columns[6]] = ref2
    merged_df[columns[7]] = alt1
    merged_df[columns[8]] = alt2

    merged_df.to_csv('output.txt', sep=' ', encoding='utf-8')

if __name__ == "__main__":
    main()

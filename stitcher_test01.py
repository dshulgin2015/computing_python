#!/usr/bin/env python
import argparse
import pysam
import vcf
import os


# IMPORTANT NOTES regarding import
# Note: I think the pyvcf module is now installed and imported as vcf

# To Do - Problem Stage #1:
# 1) Add different arguments (pop1 and pop2 - these are name of the populations
# and will be added as header in the output file)
# 2) Add arguments (vcf1 and vc2) - these are vcf files that we will provide
# 3) Add argument for the name of output file

# 4a) Create an output file which should contain following headers
# contig    pos id  ref alt ref-freq-My ref-freq-Sp alt-A-freq-My
# alt-A-freq-Sp
# the headers are separted by tab
# 4b) write the following values from vcf files: contig (from CHR), pos, id,
# ref - without any changes
# When merging information from two vcfs the the intersecting values can be
# kept and non intersecting values can be added
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
        "--pop1", help="Sample name for population 1", type=basestring, required=False)
    parser.add_argument(
        "--pop2", help="Sample name for population 2", type=basestring, required=False)
    parser.add_argument(
        "--output", help="Name of the output file", type=basestring, required=False)

    # debug / development / reporting
    parser.add_argument(
        "--chr", default="", help="Restrict haplotype stitching to a specific chromosome.")

    global args
    args = parser.parse_args()

    # setup
    version = "0.6"
    # fun_flush_print("")
    # fun_flush_print("##################################################")
    # fun_flush_print("              Welcome to phase_stitcher")
    # fun_flush_print("  Author: someone ")
    # fun_flush_print("##################################################")
    # fun_flush_print("")

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
    #     if os.path.isfile(args.vcf1):
    #         vcf_af = vcf.Reader(filename=args.vcf1)
    #     else:
    #         fatal_error(
    #             "Allele frequency VCF (--vcf) specified does not exist.")
    print check_files


if __name__ == "__main__":
    check = main()

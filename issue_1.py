import pysam

# read the input file
myvcf = pysam.VariantFile("in.vcf", "r")


# Add the HP field to header. Say its a string and can take any values. It
# depends what format you want to give.
myvcf.header.formats.add("HP", ".", "String", "HP value")
# create an object of new vcf file and open in to write data.
vcf_out = pysam.VariantFile('out.vcf', 'w', header=myvcf.header)

with open("out.vcf", "a") as out:

    for variant in myvcf:
        hp_value = ''
        for sample in variant.samples:
            if "|" in variant.samples[sample]['PG']:
                hp_value += str(variant.pos) + '-'
                if variant.samples[sample]['PG'] == "1|0":
                    hp_value = hp_value + '2' + ',' + str(variant.pos) + '-1'
                    variant.samples[sample]['HP'] = hp_value
                    # print hp_value
                if variant.samples[sample]['PG'] == "0|1":
                    hp_value = hp_value + '1' + ',' + str(variant.pos) + '-2'
                    variant.samples[sample]['HP'] = hp_value
        out.write(str(variant))

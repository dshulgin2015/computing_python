#!/usr/bin/env python

# standard library
from __future__ import print_function

try:
    from StringIO import StringIO  # Python 2
except ImportError:
    from io import StringIO  # Python 3

# biopython
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

f_records = SeqIO.parse('../computing_python/m_cold.fasta', 'fasta')
ban_list = ["pinus", "Pinus","pine", "Pine", "picea", "spruce", "Picea", "Spruce"]
counter = 0

with open('m_cold_blast.out', 'w') as save_file:

    while True:
        try:
            f_record = next(f_records)
            ban = False
            print('Doing the BLAST and retrieving the results...')
            result_handle = NCBIWWW.qblast('blastn', 'nr', f_record.format('fasta'))

            blast_results = result_handle.read()

            print('Parsing the results and extracting info...')
            counter += 1
            print (counter)

            # option 1 -- open the saved file to parse it
            # option 2 -- create a handle from the string and parse it
            string_result_handle = StringIO(blast_results)
            b_record = NCBIXML.read(string_result_handle)

            # now get the alignment info for all e values greater than some threshold
            E_VALUE_THRESH = 0.1

            for alignment in b_record.alignments[0:3]:
                if any(s in alignment.title for s in ban_list):
                    ban = True

            print (ban)
            if ban is False:
                save_file.write('\n\n----RecordId: ' + f_record.id + '----\n\n')
                for alignment in b_record.alignments[0:3]:
                    if not any(s in alignment.title for s in ban_list):
                        for hsp in alignment.hsps:
                            if hsp.expect < E_VALUE_THRESH:
                                save_file.write('****Alignment****\n')
                                save_file.write('sequence: %s\n' % alignment.title)
                                save_file.write('length: %i\n' % alignment.length)
                                save_file.write('e value: %f\n' % hsp.expect)
                                save_file.write(hsp.query[0:100] + '...\n')
                                save_file.write(hsp.match[0:100] + '...\n')
                                save_file.write(hsp.sbjct[0:100] + '...\n')
                                save_file.write(hsp.sbjct[0:100] + '...\n')
            if counter is 50:
                break
        except StopIteration:
            break
from Bio.Seq import Seq
from Bio.Restriction import *
import json


def find_plasmid_sites(p_seq):
    p_seq = Seq(p_seq)
    ana = Analysis(AllEnzymes, p_seq, linear=False)
    res = ana.with_N_sites(1, ana.blunt())
    return res


def find_gene_sites(i_seq, p_enzymes):
    i_seq = Seq(i_seq)
    rb = RestrictionBatch([])
    for enzyme in p_enzymes.keys():
        rb += enzyme
    ana = Analysis(rb, i_seq, linear=True)
    res = ana.without_site()
    result_parsed = {}
    ct = 0
    for i in res.keys():
        ct += 1
        result_parsed["Enzyme {}".format(ct)] = str(i)
    return result_parsed


def insert_sequence(p_seq, i_seq, cut_pos):
    final_seq = p_seq[:cut_pos] + i_seq + p_seq[cut_pos:]

    # if final seq doesn't have 30bp flanking 5' and 3' end append sequence from opposite side
    if final_seq.find(i_seq) <= 20:
        final_seq = final_seq[-30:] + final_seq[:-30]
    return final_seq

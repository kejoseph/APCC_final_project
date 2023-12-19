from Bio.Seq import Seq
#from primer3 import calc_hairpin


def design_gibson_primers(full_sequence, cut_pos, insert_sequence, overlap_length):

    # Extract 20bp left plasmid + target gene + 20bp right plasmid
    target_sequence = full_sequence[cut_pos - overlap_length:cut_pos + len(insert_sequence) + overlap_length]

    # Design primers using the target sequence
    fwd_primer = target_sequence[:overlap_length*2]
    rev_primer = str(Seq(target_sequence[-overlap_length*2:]).reverse_complement())

    # # check for hairpin structures at 60C
    # fwd_res = calc_hairpin(fwd_primer, temp_c=60)
    # rev_res = calc_hairpin(rev_primer, temp_c=60)

    # curr_overlap = overlap_length
    # # Adjust primers if hairpin structures are found
    # while fwd_res.structure_found or rev_res.structure_found:
    #     curr_overlap -= 1  # Decrease overlap length
    #     # Reduce overlap length by 1 base on each side for primers and calc new primer
    #     if fwd_res.structure_found:
    #         fwd_primer = target_sequence[overlap_length-curr_overlap:curr_overlap*2+1]
    #     if rev_res.structure_found:
    #         rev_primer = str(Seq(target_sequence[overlap_length-curr_overlap:curr_overlap*2+1]).reverse_complement())

    #     # Check for hairpin structures with the adjusted primers
    #     fwd_res = calc_hairpin(fwd_primer, temp_c=60)
    #     rev_res = calc_hairpin(rev_primer, temp_c=60)

    return [fwd_primer, rev_primer]

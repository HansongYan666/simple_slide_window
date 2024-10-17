import sys,os



def filter_blast(blast_out, fasta):
    dic_ref = {}
    seq = "seq"
    name = "name"
    for line in open(fasta):
        if line.startswith('>'):
            dic_ref[name] = seq
            name = line.strip().split()[0][1:]
            seq = ""
        else:
            seq += line
    dic_ref[name] = seq

    dic = {}
    for i in open(blast_out,'r').readlines():
        tmp = i.strip().split()
        blast_length = int(tmp[3])
        gene = tmp[1]
        mismatch = tmp[5]
        gap = [6]
        total = int(mismatch) + int(gap)
        if blast_length >= 17 and blast_length - total >= 15:
            if gene not in dic:
                dic[gene] = 1
            else:
                dic[gene] += 1
    for k in dic.keys():
        print(f"{k}\t{dic[k]}\t{dic_ref[k]}")


if __name__ == '__main__':
    blast_out = sys.argv[1]
    fasta= int(sys.argv[2])
    filter_blast(blast_out, fasta)
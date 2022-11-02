# simple_slide_window
a simpe script for slicing the fasta sequence, for example, you can use this to infer siRNA with a sequence from cds.
usage: python slide.py [-h] -i I -o O -w W

optional arguments

  -h, --help  show this help message and exit
  
  -i I        input fasta file name
  
  -o O        output fasta file name
  
  -w W        window size
  
Example:
  python slide.py -i test.fa -o result.fa -w 29

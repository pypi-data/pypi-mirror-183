# Text-Similarity
Package for texts similarity, based on [textdistance](https://pypi.org/project/textdistance/)

# Usage
1. installation
  ```
  pip install textsimi
  ```
2. example usage:
  ```python
  from testsimi import textsimilarity as ts
  ts.print_all_algorithms()

  print(ts.compute_similarity('hello','hi'))

  print(ts.top_K_similarity_between_one_mention_and_many_candidates(5,'hi',['hi','hihi','hello',"what's up", 'greetings', 'how are you', 'hallo', 'wie gehts']))
  
  
  '''
  ['hamming', 'mlipns', 'levenshtein', 'damerau_levenshtein', 'jaro_winkler', 'strcmp95', 'needleman_wunsch', 'gotoh', 'smith_waterman', 'jaccard', 'sorensen', 'tversky', 'overlap', 'tanimoto', 'cosine', 'monge_elkan', 'bag', 'ratcliff_obershelp', 'arith_ncd', 'rle_ncd', 'bwtrle_ncd', 'sqrt_ncd', 'entropy_ncd', 'bz2_ncd',   'zlib_ncd', 'editex', 'prefix', 'postfix', 'length', 'identity', 'matrix']
  Current algorithm is Jaccard({'qval': 1, 'as_set': False, 'external': True})
  0.16666666666666666
  ['hi', 'hihi', 'wie gehts', 'hallo', 'hello']
  '''
  ```
3. [colab notebook for tf-idf text similarity](https://colab.research.google.com/gist/leoxiang66/1275ad6c11e97df29abe474c50712668/tf-idf-text-similarity.ipynb)

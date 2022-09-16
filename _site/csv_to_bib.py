import sys, getopt, csv
import os, subprocess
from collections import namedtuple

SCRIPT_NAME = 'csv2bib'

BIB_DIR = 'bibs'

KEY = 'name'

READY_KEY = 'ready'

BIB_ATTRIBUTE_MAP = {
  'abstract':     ['abstract'],
  'address':      ['address', 'place of publication'],
  'anthology':    ['anthology'],
  'author':       ['author', 'authors'],
  'arXiv':        ['arxiv'],
  'booktitle':    ['volume title', 'booktitle'],
  'chapter':      ['chapter'],
  'code':         ['code'],
  'edition':      ['edition'],
  'editor':       ['editor', 'editors'],
  'featured':     ['featured'],
  'journal':      ['journal', 'journal name'],
   KEY:           [KEY],
  'month':        ['month'],
  'number':	      ['issue number'],
  'pages':        ['pages'],
  'publisher':    ['publisher'],
  'slides':       ['slides'],
  'series':       ['series'],
  'title':        ['title'],
  'url':          ['url'],
  'venue':        ['venue'],
  'video':        ['video'],
  'volume':       ['volume'],
  'year':         ['year', 'date'],
  'ready':        ['ready'],
  'recent':       ['recent']
}

class CSVParseError(Exception):
    pass

# [0 => 'author', 1 => 'title', ...]
def parse_headers(headers, bib_attribute_map = BIB_ATTRIBUTE_MAP):
  valid_columns = {}
  invalid_columns = {}

  for i, header in enumerate(headers):
    found = False
    for bib_attribute, bib_attribute_variants in bib_attribute_map.items():
      # The reference attribute is recognised, and allowed for that reference type
      if header.lower() in bib_attribute_variants:
        valid_columns[i] = bib_attribute
        found = True

    if found == False:
      invalid_columns[i] = header.strip()

  if KEY not in valid_columns.values():
    import ipdb; ipdb.set_trace()
    raise CSVParseError('no key column found')


  columns = namedtuple("columns", ["valid", "invalid"])
  return columns(valid_columns, invalid_columns)

def parse_reference(row, attributes_order):
  ref = {}
  for i, col in enumerate(row):
    # Skip columns for which we did not recognise the header
    if i not in attributes_order:
      continue

    col = col.strip()

    if len(col) == 0:
      continue

    ref[attributes_order[i]] = col

  return ref


def guess_ref_type(ref):
  if ref.get('booktitle'):
    if "transactions" in ref.get('booktitle').lower():
      return 'article'
    return 'inproceedings'
  return 'misc'

  # if 'pages' in headers.values():
  #   return 'incollection'
  # return 'book'

def to_bib(ref):
  ref_type = guess_ref_type(ref)

  featured = False

  if ref.get('anthology'):
    ref['url'] = ref.get('anthology')
  elif ref.get('arXiv'):
    ref['url'] = ref.get('arXiv')

  bib_ref = "@%s{%s, \n" % (ref_type, ref.get(KEY, "unnamed"))
  for attr, attr_value in ref.items():
    if attr == READY_KEY:
        # if attr_value == 'no':
        #   return None, None, None
        continue
    if attr == 'featured':
      if attr_value == 'yes':
        featured = True
      continue

    if attr == 'recent':
      #attr_value = "true" if attr_value == "yes" else "false"
      continue

    if attr == KEY:
      continue

    if not attr_value:
      continue

    if attr == "author":
      all_authors = attr_value.replace('and ', ',').split(",") 
      bib_ref += '  %s = {' % attr
      for i, author in enumerate(all_authors):
        # in case of empty string
        if author.isspace():
          continue
        full_name = author.split()
        bib_ref += '%s, ' % ' '.join(full_name[1:])#'%s, ' % full_name[-1]
        if i == len(all_authors) - 1:
          bib_ref += ' '.join(full_name[:1]) #' '.join(full_name[:len(full_name) - 1])
        else:
          bib_ref += '%s and \n\t' % ' '.join(full_name[:1])
      bib_ref += '},\n'
    else:
      bib_ref += '  %s = {%s},\n' %(attr, attr_value.strip())

  bib_ref += "}\n"
  return ref[KEY], bib_ref, featured


def csv_to_bib(csv_file, delimiter):
  columns_found = False
  bib_refs = {}

  with open(csv_file, 'r') as f:
    refs_type = ''
    csv_reader = csv.reader(f, delimiter=delimiter, quotechar='"')

    for row in csv_reader:
      if len(''.join(row)) == 0: # skip leading empty lines
        continue
      
      if not columns_found:
        # We assume all refs in a CSV are the same type (book, article, ...)
        columns = parse_headers(row)

        for idx in columns.invalid:
          print('Warning in file %s: unrecognised column %s' % (csv_file, columns.invalid[idx]), file=sys.stderr)

        columns_found = True
        continue

      reference = parse_reference(row, columns.valid)
      key, bib, featured = to_bib(reference)
      if key:
        bib_refs[key] = bib, featured

  return bib_refs


def main(argv):
  failure = 0
  delimiter = '\t'

  try:
    opts, csv_files = getopt.getopt(argv,"-d:")
  except getopt.GetoptError:
    print('Error parsing command line. Usage:\n')
    print("    %s -d <delimiter> file1 file2 ...\n" % SCRIPT_NAME)
    return 2

  for o, a in opts:
    if o == "-d":
      delimiter = a
    else:
      assert False, "unhandled option"

  for csv_file in csv_files:
    try:
      bibs = csv_to_bib(csv_file, delimiter)
      for key, tup in bibs.items():
        bib, featured = tup
        file_name = os.path.join(BIB_DIR, key + '.bib')
        with open(file_name, 'w') as f:
          f.write(bib)
        command = ['academic', 'import', '--bibtex', file_name, '--overwrite']
        if featured:
          command.append('--featured')
        subprocess.run(command)
    except CSVParseError as e:
        print ('Error: Failed to parse %s: %s' % (csv_file, str(e)), file=sys.stderr)
        failure = 1
    except FileNotFoundError as e:
        print ('Error: Failed to parse %s: file not found' % csv_file, file=sys.stderr)
        print(e)
        failure = 1

  return failure


if __name__ == "__main__":
   sys.exit(main(sys.argv[1:]))


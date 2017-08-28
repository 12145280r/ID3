import re
import sys

def main(path):

    [attr, data] = read_csv(path)

def read_csv(path):
    '''
    Parameters:
	path - string : path to csv file

    Returns:
	attr - list : a list containing the name of all attributes in the 
			csv header line
	
	data - list : a nested list containing the value for each attribute in the
			dataset.  
    Notes:
    '''

    fin = open(path)
    header = fin.readline()
    attr = parse_header(header)
    data_lines = fin.readlines()
    data = parse_data(data_lines)
    fin.close()
    return [attr, data]


def parse_header(header_line):
    '''
    Parameters:
	header_line - string : expected csv header line

    Returns:
	attr - list : a list containing the name of all attributes in the 
			csv header line
	
    Notes: Exptected header format:
		# attribute1,attribute2,...,attributeN
	   any whitespace will be ignored.
    '''
    if header_line[0] == '#':
	header_line = re.sub('\s', '', header_line[1:])
	attr = header_line.split(',')
        return attr
    else:
	print 'Error incorrect header line format'

def parse_data(data_lines):
    '''
    Parameters:
	data_lines - string : expected csv data lines

    Returns:
	data - list : a nested list containing the value for each attribute in the
			dataset.  
	
    '''

    data = []
    for line in data_lines:
 	data.append(line[:-1].split(','))
    return data
	

if __name__ == '__main__':
    main(sys.argv[1])


import re
import sys
import numpy as np



def main(path):

    [attr, data] = read_csv(path)
    enc = encoder()
    encoded = enc.encode(data) 
    data = np.transpose(encoded)
    #print info_gain(np.array(data[0], dtype=int), np.array(data[4],dtype=int))
    for i in range(1,17):
        print info_gain(data[0], data[i])





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
	

class encoder:
    '''
	class for one hot encoding
    '''

    def __init__(self):
        self.attr_labels = []


    def create_labels(self, data):
	#Create a list of unique labels for each attr in data
        for attr in np.transpose(data): 
	    self.attr_labels.append(list(np.unique(attr)))


    def encode(self, data):
        if len(self.attr_labels) == 0:
	    self.create_labels(data)
	data = np.transpose(data)
        col_idx = 0
        for i in range(0, len(data)):
	    for j in range(0, len(data[0])):
	        data[i][j] = (self.attr_labels[i].index(data[i][j]))
	return np.array(data, dtype=int).T


#    def decode(self, data):
#	data = np.transpose(data)
 #       col_idx = 0
  #      for i in range(0, len(data)):
#	    for j in range(0, len(data[0])):
#		data[i][j] = self.attr_labels[i][int(data[i][j])]
#	return np.transpose(data)


def entropy(x):
    '''
    Notes: it is assumed that this tree works ONLY with binary classes  
    '''
    pos = float(np.count_nonzero(x))/float(len(x))
    neg = 1-pos
    if (neg == 0) or (pos == 0):
	return 0 
    else:
        return neg*np.log(float(1)/float(neg))+pos*np.log(float(1)/float(pos))

def info_gain(y, attr):
    '''
	compute information gain of 
    '''

    ent_y = entropy(y)
    attr_vals = np.unique(attr)
    w_sum = 0
    y= np.array(y)
    for val in attr_vals:
	y_val = y[attr == val]
        w_sum = w_sum + (float(len(y_val)) / float(len(y))) * entropy(y_val)
    return ent_y - w_sum


if __name__ == '__main__':
    main(sys.argv[1])


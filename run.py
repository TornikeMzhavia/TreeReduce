from Tree import Tree_Simplifier
from configobj import ConfigObj

def data_generator(input_directory, split_symbol, list_separator):
        '''
        Reads the input file from the directory
        Splits the line by the separator, strips the input and yields the results
        '''

        try:
            with open(input_directory, 'r') as file:
                for line in file:
                    # get node identifier url and string containing technologies split by list_separator
                    # extra spaces from left adn right are being stripped
                    url, tech_list_string = (chunk.strip().strip('/') for chunk in line.split(split_symbol))
        
                    # seperate the technologies used by a generator comprehension
                    tech_list = (tech.strip() for tech in tech_list_string.split(list_separator))
        
                    # yield the results
                    yield url, tech_list
        except Exception as e:
            raise Exception('Error while reading the input file') from e
    
if __name__ == '__main__':
    # read the configuration
    config = ConfigObj('config.ini', interpolation = False)

    input_directory = config['input_directory']
    output_directory = config['output_directory']
    split_symbol = config['split_symbol']
    list_separator = config['element_separator']

    # create the inut data source
    data_source = data_generator(input_directory, split_symbol, list_separator)

    # create the simplifier instance and run it
    simplifier = Tree_Simplifier(data_source, output_directory)
    simplifier.run()
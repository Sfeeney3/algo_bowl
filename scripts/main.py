from mst_algorithm import MST 
import os
import sys





if __name__ == "__main__":
    directory_in = './competition_inputs/inputs/'
    index = 0
    for filename in os.scandir(directory_in):
        print(type(filename))
        if filename.is_file():
            data = ''
            with open(filename, 'r') as x:

                for line in x:
                    data = data + line
            data = data.strip().split('\n')
            min_tree = MST(data)

        output = min_tree.find_minimum_subset_tree()
    #print(output)
        with open('./outputs/output_'+filename.name+'.txt', 'w') as file:
            file.write(output)   
        index = index + 1 

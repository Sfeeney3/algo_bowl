# enter filenames as strings, see as below
def store_output(input_file, output_file_mst, output_file_sim):
    store_string = input_file + ' '
    file_mst = open(output_file_mst)
    values_mst = file_mst.readlines()

    # cost of MST
    cost_without_sim_ann = values_mst[0]

    store_string += cost_without_sim_ann + ' '

    file_sim = open(output_file_sim)
    values_sim = file_sim.readlines()

    # cost of MST
    cost_with_sim_ann = values_sim[0]

    store_string += cost_with_sim_ann + '\n'

    file = open('output_store.txt', 'w')
    file.write(store_string)
    file.close()

    return

# TESTING
# input_file = './inputs/output_graph_bias_1_kreg.txt'
# output_file_mst = 'output_test.txt'
# output_file_sim = 'output_test.txt'
# store_output(input_file, output_file_mst, output_file_sim)
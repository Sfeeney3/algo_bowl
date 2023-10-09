

from input_script_bias_variation import InputScript as input_gen_kreg






if __name__ == "__main__":

    node_params = [700,1000]

    input_script = input_gen_kreg(node_params)
    input_script.output_graph()
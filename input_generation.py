from scripts.input_script import InputScript as input_gen
from scripts.input_script_bias import InputScript as input_gen_bias






if __name__ == "__main__":

    node_params = [1000,2000]

    input_script = input_gen_bias(node_params)
    input_script.output_graph()
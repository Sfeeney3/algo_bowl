from scripts.input_script import InputScript as input_gen






if __name__ == "__main__":

    node_params = [10,30]
    input_script = input_gen(node_params)
    input_script.output_graph()
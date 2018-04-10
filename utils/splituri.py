#splits uri into [URL,[parameter_1,parameter_1_value],[parameter_2,parameter_2_value],...,[parameter_n,parameter_n_value]]
def splituri(uri):

    # splits uri into [URL,parameters_and_values]
    uri_split = uri.split('?')
    print('utils.splituri: first uri split executed > ' + str(uri_split))

    #splits parameters into [parameter_1_and_value_1,parameter_2_and_value_2,parameter_3_and_value_3,...,parameter_n_and_value_n]
    param_tuple_split = uri_split[1].split('&')
    print('utils.splituri: param tuples split executed > ' + str(param_tuple_split))

    #removes parameters from current uri split
    del uri_split[1]
    print('utils.splituri: parameter list deleted from uri split > ' + str(uri_split))

    #for each (parameter,value) tuple in the line:
    for param_tuple in param_tuple_split:
        #spluts tuple and appends split to uri_split
        uri_split.append(param_tuple.split('='))
        print('utils.splituri: parameter tuple added to uri split')
    print('utils.splituri: uri split completed > ' + str(uri_split))

    #returns final uri split
    return uri_split


#makes current module executable
if __name__ == "__main__":
    import sys
    result = splituri(str(sys.argv[1]))
    print(str(result))

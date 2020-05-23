def forward_checking(h_domains, v_domains, h_to_fill, v_to_fill):

    for i in h_to_fill:
        if h_domains[i] == []:
            return False

    for i in v_to_fill:
        if v_domains[i] == []:
            return False

    return True

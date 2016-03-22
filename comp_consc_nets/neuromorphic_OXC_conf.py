from micro_mechanisms import COPY, NOR
import graphite as g
import pyphi
import pickle

net_conf = [('AA', NOR, 'BC', 'CF'),
            ('AB', NOR, 'AA'),
            ('AC', COPY, 'AB'),
            ('BA', COPY, 'CF'),
            ('BB', COPY, 'BA'),
            ('BC', COPY, 'BB'),
            ('CA', NOR, 'AC'),
            ('CB', NOR, 'BC'),
            ('CC', NOR, 'AC', 'BC'),
            ('CD', NOR, 'CA', 'CB'),
            ('CE', COPY, 'CC'),
            ('CF', NOR, 'CD', 'CE')]

state1 = {'on': ['AC']}

if __name__ == "__main__":
    # Shared setup ============================================================
    g_net = g.Network(net_conf, state1)
    pyphi_net = pyphi.Network(g_net.tpm, g_net.state,
                              connectivity_matrix=g_net.connectivity_matrix)
    hidden_indices = [0, 1, 3, 4, 6, 7, 8, 9, 10]
    possible_backgrounds = [None, 6, 7, 8, 9, 10]

    def blackbox_with_background_element(bg_element_idx):
        internal_indices = list(range(pyphi_net.size))
        if bg_element_idx is not None:
            del internal_indices[bg_element_idx]
        pyphi_sub = pyphi.Subsystem(internal_indices=internal_indices,
                                    network=pyphi_net,
                                    hidden_indices=hidden_indices,
                                    time_scale=3)
        return pyphi.compute.big_mip(pyphi_sub)

    # Try each reasonable background condition ===============================
    results = dict()
    for bg_element_idx in possible_backgrounds:
        print('Trying with background elements:', bg_element_idx)
        big_mip = blackbox_with_background_element(bg_element_idx)
        print(big_mip.phi)
        print(big_mip.cut)
        results[bg_element_idx] = (big_mip.phi, big_mip.cut)
        fname = 'neuromorphic_OXC_bg%s_big_mip.pickle' % bg_element_idx
        with open(fname, 'wb') as f:
            pickle.dump(big_mip, f, pickle.HIGHEST_PROTOCOL)

    import pdb; pdb.set_trace()

    # Graphite code ===========================================================
    # concepts = net.net_first_order_concepts(just_phi=False, use_roi=False)
    # print(concepts)
    # big_phi = net.net_first_order_mip()
    # print(big_phi)
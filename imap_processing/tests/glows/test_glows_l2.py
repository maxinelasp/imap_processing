from imap_processing.glows.l2.glows_l2 import glows_l2, split_data_by_observational_day, \
    generate_l2


def test_glows_l2(l1b_hist_dataset):
    l2 = glows_l2(l1b_hist_dataset, "v001")


def test_split_by_observational_day(l1b_hist_dataset):
    split = split_data_by_observational_day(l1b_hist_dataset)
    # print(split)
    l2 = generate_l2(split[0])
    print(l2)

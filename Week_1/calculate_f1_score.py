"""This module define function for AIO2024 Module 1 week 1 exercise."""

def cal_f1_score(tp: int, fn: int, fp: int) -> tuple[float,float,float]:
    """_summary_

    Args:
        tp (int): True positive for observation
        fn (int): False negative for observation
        fp (int): False positive for observation

    Returns:
        tuple[precision,recall,f1]: Return a tuple with 3 metrics
    """
    assert isinstance(tp, int), "TP must be a int"
    assert isinstance(fn, int), "FN must be a int"
    assert isinstance(fp, int), "FP must be a int"
    assert tp > 0 and fn > 0 and fp > 0, "tp and fp and fn must be greater than zero"

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)
    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1 score is {f1}")
    return precision,recall,f1

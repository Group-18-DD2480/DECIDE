from src.utils import InvalidInputException

def LAUNCH(FUV):
    """
    Constructs the LAUNCH boolean variable based on FUV (Final Unlocking Vector)

    Args:
        FUV (list of bool): Final Unlocking Vector.

    Returns:
        boolean value

    Raises:
        InvalidInputException: If FUV is not a list, if its size does not match
    """

    if type(FUV) != list or len(FUV) != 15:
        raise InvalidInputException

    return all(FUV)
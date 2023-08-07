from .formats_constants import ECB_NATIONAL_IDENTIFIERS_REGISTERS


def get_verification_register(identifier: str):
    """
    List of national identifiers registers issued by European Central Bank, used to manually verify identifiers.

    :param identifier: String with identifier code
    :return: list, str
    """
    return ECB_NATIONAL_IDENTIFIERS_REGISTERS.get(identifier, ())

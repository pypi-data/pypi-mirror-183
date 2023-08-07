from identifier_tools.mappers import get_verification_register


def test_get_verification_register():
    assert get_verification_register("DK_CVR_CD") == "http://www.cvr.dk"
    assert get_verification_register("US_EIN_CD") == (
        "https://www.irs.gov/businesses/small-businesses-self-employed/employer-id-numbers-eins",
        "https://eintaxid.com/",
    )

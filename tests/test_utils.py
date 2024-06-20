from app import utils


def test_sluggify_socar_euro_regular():
    result = utils.sluggify_fuel("Nano Euro Regular")
    assert result == "euro_regular"


def test_sluggify_rompetrol_euro_diesel():
    result = utils.sluggify_fuel("efix Euro Diesel")
    assert result == "euro_diesel"


def test_sluggify_georgian_euro_regular():
    result = utils.sluggify_fuel("Evro Regulari")
    assert result == "euro_regular"


def test_sluggify_3():
    result = utils.sluggify_fuel("Hello World")
    assert result is None


def test_sluggify_euro_premium():
    result = utils.sluggify_fuel("Nano Evro Premiumi")
    assert result == "euro_premium"


def test_sluggify_gulf_super():
    result = utils.sluggify_fuel("G-Force Super")
    assert result == "super"


def test_extract_fuel_type_regular():
    result = utils.extract_fuel_type("Nano Euro Regular")
    assert result == "regular"


def test_extract_fuel_grade_euro():
    result = utils.extract_fuel_grade("g-force evro regulari")
    assert result == "euro"

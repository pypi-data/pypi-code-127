import pytest

from woodwork.config import Config


@pytest.fixture
def defaults():
    return {
        "option1": "value1",
        "option2": "value2",
    }


@pytest.fixture
def config(defaults):
    return Config(defaults)


def test_init_conifg(defaults):
    config = Config(defaults)
    assert config._data == defaults
    assert config._defaults == defaults
    assert config._data == config._defaults
    assert config._data is not config._defaults


def test_get_option(config):
    assert config.get_option("option1") == "value1"
    assert config.get_option("option2") == "value2"


def test_set_option(config):
    config.set_option("option1", "updated_value")
    assert config.get_option("option1") == "updated_value"
    assert config.get_option("option2") == "value2"


def test_reset_option(config):
    config.set_option("option1", "updated_value")
    assert config.get_option("option1") == "updated_value"
    config.reset_option("option1")
    assert config.get_option("option1") == "value1"


def test_with_options(config):
    old_value_1 = config.get_option("option1")
    old_value_2 = config.get_option("option2")

    with_value_1 = "some_other_value_1"
    with_value_2 = "some_other_value_2"

    with config.with_options(option1=with_value_1, option2=with_value_2):
        assert config.get_option("option1") == with_value_1
        assert config.get_option("option2") == with_value_2

    assert config.get_option("option1") == old_value_1
    assert config.get_option("option2") == old_value_2

    # Make sure that config gets reset when exceptions occur
    try:
        with config.with_options(option1="lkjasdlfkjasdf"):
            raise RuntimeError("something went wrong!")
    except RuntimeError:
        pass
    assert config.get_option("option1") == old_value_1


def test_invalid_option_warnings(config):
    error_msg = "Invalid option specified: invalid_option"

    with pytest.raises(KeyError, match=error_msg):
        config.get_option("invalid_option")

    with pytest.raises(KeyError, match=error_msg):
        config.set_option("invalid_option", "updated_value")

    with pytest.raises(KeyError, match=error_msg):
        config.reset_option("invalid_option")


def test_repr(config, defaults):
    repr_output = repr(config)
    assert "Woodwork Global Config Settings" in repr_output
    for key, value in defaults.items():
        assert f"{key}: {value}" in repr_output

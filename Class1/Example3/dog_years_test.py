import pytest
import dog_years


@pytest.mark.parametrize("human_years, dog_year", [(9, 49.0), (31, 137.0), (1, 10.5), (0, 0), (-99, 0)])
def test_human_to_dog_years(human_years, dog_year):
    assert dog_years.human_to_dog_years(human_years) == dog_year

from app.measure_conversor import DistanceMeasure, TimeMeasure, TimePerDistance


class TestMeasureConversor:
    ONE_KILOMETER = 1
    TEN_MIPPS = 10
    TEN_WORS = 10
    FIVE_MIRS = 5
    ONE_HOUR = 1

    def __init__(self):
        pass

    def init_tests(self):
        self.test_mipps_to_kilometer()
        self.test_lutt_to_mipps()
        self.test_dar_to_wor()
        self.test_wor_to_mir()
        self.test_mir_to_hour()
        self.test_luts_per_wor_to_kilometers_to_hour()
        print("All tests suceed")

    def test_mipps_to_kilometer(self):
        assert DistanceMeasure()._mipps_to_kilometer(2) == self.ONE_KILOMETER

    def test_lutt_to_mipps(self):
        assert DistanceMeasure()._lutt_to_mipps(1) == self.TEN_MIPPS

    def test_dar_to_wor(self):
        assert TimeMeasure()._dar_to_wor(1) == self.TEN_WORS

    def test_wor_to_mir(self):
        assert TimeMeasure()._wor_to_mir(1) == self.FIVE_MIRS

    def test_mir_to_hour(self):
        assert TimeMeasure()._mir_to_hour(2) == self.ONE_HOUR

    def test_luts_per_wor_to_kilometers_to_hour(self):
        """
        1 MIPPS == 0.5 KILOMETERS
        1 LUTT == 10 MIPPS == (0.5) * 10 == 5 KILOMETERS
        1 LUTT == 5 KILOMETERS

        1 MIR == 0.5 HOURS
        1 WOR == 5 MIRS == (0.5) * 5 == 2.5 HOURS
        1 DAR == 10 WORS == (2.5) * 10 == 25 HOURS
        1 WOR == 2.5 HOURS

        1 LUTT == 5 kilometers
        1 WOR == 2.5 HOURS

        LUTT/WOR = 5KM/2.5 HOURS == 2KM/HR
        """
        assert (
            TimePerDistance().luts_per_wor_to_kilometers_to_hour(1, 1)
            == "The average speed is 5.0/2.5"
        )


if __name__ == "__main__":
    TestMeasureConversor().init_tests()

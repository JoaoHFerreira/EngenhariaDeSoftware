class DistanceMeasure:
    def lutt_to_kilometer(self, lutt):
        return self._mipps_to_kilometer(self._lutt_to_mipps(lutt))

    @staticmethod
    def _lutt_to_mipps(lutt):
        return lutt * 10

    @staticmethod
    def _mipps_to_kilometer(mipps):
        return mipps / 2


class TimeMeasure:
    def wor_to_hour(self, wor):
        return self._mir_to_hour(self._wor_to_mir(wor))

    def dar_to_hour(self, dar):
        return self._mir_to_hour(self._wor_to_mir(self._dar_to_wor(dar)))

    @staticmethod
    def _dar_to_wor(dar):
        return dar * 10

    @staticmethod
    def _wor_to_mir(wor):
        return wor * 5

    @staticmethod
    def _mir_to_hour(mir):
        return mir / 2


class TimePerDistance(TimeMeasure, DistanceMeasure):
    def luts_per_wor_to_kilometers_to_hour(self, lut, wor):
        kms = self.lutt_to_kilometer(lut)
        hours = self.wor_to_hour(wor)
        return f"The average speed is {kms}/{hours}"

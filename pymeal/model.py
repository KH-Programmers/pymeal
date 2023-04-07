import re
import requests
from typing import List


class MealStatus:
    class NotExist:
        pass

    class OnlyLunch:
        pass

    class OnlyDinner:
        pass

    class Exist:
        pass


class Menu:
    def __init__(self, name: str, allergy: list):
        self._name = name
        self._allergy = allergy

    @property
    def name(self):
        return self._name

    @property
    def allergy(self):
        return self._allergy


class Meal:
    def __init__(self, apiKey: str, schoolCode: str, date: str):
        self._apiKey = apiKey
        self._schoolCode = schoolCode
        self._date = date

    def getMeal(self):
        url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
        params = {
            "Type": "json",
            "ATPT_OFCDC_SC_CODE": self._schoolCode,
            "SD_SCHUL_CODE": self._schoolCode,
            "MLSV_YMD": self._date,
            "KEY": self._apiKey,
        }
        response = requests.get(url, params=params)
        mealData = response.json()
        return mealData

    #     self._lunch: List[Menu] = []
    #     self._dinner: List[Menu] = []
    #     data = []
    #     if self.status == MealStatus.Exist:
    #         data.append((self._mealData["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"], self._lunch))
    #         data.append((self._mealData["mealServiceDietInfo"][1]["row"][1]["DDISH_NM"], self._dinner))
    #     elif self.status == MealStatus.OnlyLunch:
    #         data.append((self._mealData["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"], self._lunch))
    #     elif self.status == MealStatus.OnlyDinner:
    #         data.append((self._mealData["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"], self._dinner))
    #
    #     for i in data:
    #         for menu in list(
    #             map(
    #                 lambda x: x.strip(),
    #                 i[0].replace("*", "").split("<br/>"),
    #             )
    #         ):
    #             i[1].append(
    #                 Menu(
    #                     name="".join(list(filter(lambda x: x.isalpha() or x == " ", re.sub(r"\([^)]*\)", "", menu).strip()))),
    #                     allergy=list(
    #                         filter(
    #                             lambda x: x != "" and x.isdigit(),
    #                             str(
    #                                 ""
    #                                 if len(re.findall(r"\([^)]*\)", menu)) == 0
    #                                 else re.findall(r"\([^)]*\)", menu)[0]
    #                             )
    #                             .replace("(", "")
    #                             .replace(")", "")
    #                             .split("."),
    #                         )
    #                     ),
    #                 )
    #             )
    #
    # @property
    # def status(self):
    #     if (
    #         self._mealData.get("RESULT") is not None
    #         and self._mealData["RESULT"]["CODE"] == "INFO-200"
    #     ):
    #         return MealStatus.NotExist
    #     if len(self._mealData["mealServiceDietInfo"][1]["row"]) == 1:
    #         if (
    #             self._mealData["mealServiceDietInfo"][1]["row"][0]["MMEAL_SC_NM"]
    #             == "중식"
    #         ):
    #             return MealStatus.OnlyLunch
    #         else:
    #             return MealStatus.OnlyDinner
    #     return MealStatus.Exist
    #
    # def to_dict(self):
    #     if self.status == MealStatus.Exist:
    #         return {
    #             "lunch": list(map(lambda x: {"name": x.name, "allergy": x.allergy}, self._lunch)),
    #             "dinner": list(map(lambda x: {"name": x.name, "allergy": x.allergy}, self._dinner)),
    #         }
    #     elif self.status == MealStatus.OnlyLunch:
    #         return {
    #             "lunch": list(map(lambda x: {"name": x.name, "allergy": x.allergy}, self._lunch)),
    #             "dinner": None,
    #         }
    #     elif self.status == MealStatus.OnlyDinner:
    #         return {
    #             "lunch": None,
    #             "dinner": list(map(lambda x: {"name": x.name, "allergy": x.allergy}, self._dinner)),
    #         }
    #     else:
    #         return {
    #             "lunch": None,
    #             "dinner": None,
    #         }

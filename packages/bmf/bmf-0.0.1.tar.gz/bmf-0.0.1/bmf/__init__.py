"""Python request wrapper for BMF
"""
import os
from functools import lru_cache
from xml.dom import minidom

import requests

# BMF_URL = os.environ.get("BMF_URL",
# "http://www.bmf-steuerrechner.de/interface/2023Version1.xhtml?code=ext2023&LZZ=1&RE4=")


class BMFParameters:  # pylint: disable=too-few-public-methods
    """Class for parameter wrapping, such as "RE4=0, LZZ=1" and build GET parameter
    representation"""

    parameters = {"LZZ": 1, "RE4": 0, "STKL": 1}

    def __init__(self, **kwargs):
        """Any parameter can be submitted and will be attached to the bmf get requests"""
        for (key, value) in kwargs.items():
            self.parameters[key] = value

    def __str__(self) -> str:
        """GET parameter concatenation

        Returns:
            str: key=value pairs with &, e.g. 'LZZ=1&RE4=2000000&STKL=1'
        """
        ret = []
        for (key, value) in self.parameters.items():
            ret.append(f"{key}={value}")
        return "&".join(ret)


def set_bmf_url(bmf_url: str) -> None:
    """Set `BMF_URL` environment variable

    Has to be compliant to following format (which is default):
    `http://www.bmf-steuerrechner.de/interface/2022Version1.xhtml?code=ext2023&`


    Args:
        BMF_URL (str): new BMF Url
    """
    os.environ["BMF_URL"] = bmf_url


def get_bmf_url() -> str:
    """Get BMF URL

    Default is: `http://www.bmf-steuerrechner.de/interface/2022Version1.xhtml?code=ext2023&`

    Returns:
        str: BMF URL
    """
    return os.environ.get(
        "BMF_URL",
        "http://www.bmf-steuerrechner.de/interface/2022Version1.xhtml?code=ext2023&",
    )


@lru_cache(maxsize=128, typed=False)
def get_taxes(  # pylint: disable=too-many-arguments
    gross: float,
    tax_class: int = 1,
    church: int = 0,
    health_insurance: int = 0,
    kids: int = 0,
    health_insurance_additional: float = 0,
) -> dict:
    """Query BMF API

    See documentation at
    https://www.bundesfinanzministerium.de/Content/DE/Downloads/
        Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2022-11-18-PAP-2023-anlage-1.pdf

    This is using the @lru_cache in order to reduce actual queries

    Args:
        gross (float): Gross salary in Euros
        tax_class (int, optional): Tax class from 1-6 aka I, II, etc. Defaults to 1.
        church (int, optional): Has to pay church taxes. Defaults to 0.
        health_insurance (int, optional): Which type of health insurance. Defaults to 0.
        kids (int, optional): amount of kids. Defaults to 0.
        health_insurance_additional (float, optional): health insurance percentage. Defaults to 0.

    Returns:
        dict: { `BK`      : Bemessungsgrundlage für die Kirchenlohnsteuer in Cent
                `BKS`     : Bemessungsgrundlage der sonstigen Bezüge (ohne Vergütung für mehrjährige
                            Tätigkeit) für die Kirchenlohnsteuer in Cent.
                `BKV`     : Bemessungsgrundlage der Vergütung für mehrjährige Tätigkeit und der
                            tarifermäßigt zu besteuernden Vorteile bei Vermögensbeteiligungen für
                            die Kirchenlohnsteuer in Cent
                `LSTLZZ`  : Für den Lohnzahlungszeitraum einzubehaltende Lohnsteuer in Cent
                `SOLZLZZ` : Für den Lohnzahlungszeitraum einzubehaltender Solidaritätszuschlag
                            in Cent
                `SOLZS`   : Solidaritätszuschlag für sonstige Bezüge (ohne Vergütung für
                            mehrjährige Tätigkeit in Cent.
                `SOLZV`   : Solidaritätszuschlag für die Vergütung für mehrjährige Tätigkeit und
                            der tarifermäßigt zu besteuernden Vorteile bei Vermögensbeteiligungen
                            in Cent
                `STS`     : Lohnsteuer für sonstige Bezüge (ohne Vergütung für mehrjährige
                            Tätigkeit und ohne tarifermäßigt zu besteuernde Vorteile bei
                            Vermögensbeteiligungen) in Cent
                `STV`     : Lohnsteuer für die Vergütung für mehrjährige Tätigkeit und der
                            tarifermäßigt zu besteuernden Vorteile bei Vermögensbeteiligungen
                            in Cent
                `VKVLZZ`  : Für den Lohnzahlungszeitraum berücksichtigte Beiträge des
                            Arbeitnehmers zur privaten Basis-Krankenversicherung und privaten
                            Pflege-Pflichtversicherung (ggf. auch die Mindestvorsorgepauschale)
                            in Cent beim laufenden Arbeitslohn. Für Zwecke der
                            Lohnsteuerbescheinigung sind die einzelnen Ausgabewerte außerhalb
                            des eigentlichen Lohnsteuerberechnungsprogramms zu addieren;
                            hinzuzurechnen sind auch die Ausgabewerte VKVSONST.
                `VKVSONST`: Für den Lohnzahlungszeitraum berücksichtigte Beiträge des Arbeitnehmers
                            zur privaten Basis-Krankenversicherung und privaten Pflege-
                            Pflichtversicherung (ggf. auch die Mindestvorsorgepauschale) in Cent
                            bei sonstigen Bezügen. Der Ausgabewert kann auch negativ sein. Für
                            tarifermäßigt zu besteuernde Vergütungen für mehrjährige Tätigkeiten
                            enthält der PAP keinen entsprechenden Ausgabewert.
        }

    """

    request_params = BMFParameters(
        RE4=int(gross * 1000),
        STKL=tax_class,
        LZZ=1,
        R=church,
        PKV=health_insurance,
        ZKF=kids,
        KVZ=health_insurance_additional,
    )
    request_string = get_bmf_url() + str(request_params)
    xmldoc = minidom.parseString(
        requests.get(request_string, timeout=10000).content
    )
    ausgaben = xmldoc.getElementsByTagName("ausgabe")
    tax = {}
    for element in ausgaben:
        key = element.attributes["name"].value
        value = element.attributes["value"].value

        tax[key] = 0 if (value == "0") else float(value) / 1000.0

    return tax

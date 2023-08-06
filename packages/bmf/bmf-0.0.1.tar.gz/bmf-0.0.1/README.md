# Bundesministerium für Finanzen - Steuer API

Python request wrapper for the BMF-Calculator provided by the Bundesministerium für Finanzen

## Usage

```python
from bmf import set_BMF_url, get_taxes

# change the url that is queried (e.g. for 2023 or new access code such as `code=ext2024`))
>>> set_bmf_url('http://www.bmf-steuerrechner.de/interface/2022Version1.xhtml?code=ext2023&')

>>> get_taxes(
    gross=2500,                 # gross salary
    tax_class=1,                # Tax class from I-VI as 1..6
    church=1                    # Church tax modifier
    health_insurance: int = 0,  # see BMF website for codes
    kids: int = 0,              # How many kids?
    health_insurance_additional: float = 0, # additional tax, e.g. 1.6 (%)
)
```

`dict` mit
`BK`      : Bemessungsgrundlage für die Kirchenlohnsteuer in Cent
`BKS`     : Bemessungsgrundlage der sonstigen Bezüge (ohne Vergütung für mehrjährige Tätigkeit)
            für die Kirchenlohnsteuer in Cent.
`BKV`     : Bemessungsgrundlage der Vergütung für mehrjährige Tätigkeit und der tarifermäßigt
            zu besteuernden Vorteile bei Vermögensbeteiligungen für die Kirchenlohnsteuer
            in Cent
`LSTLZZ`  : Für den Lohnzahlungszeitraum einzubehaltende Lohnsteuer in Cent
`SOLZLZZ` : Für den Lohnzahlungszeitraum einzubehaltender Solidaritätszuschlag in Cent
`SOLZS`   : Solidaritätszuschlag für sonstige Bezüge (ohne Vergütung für mehrjährige Tätigkeit in Cent.
`SOLZV`   : Solidaritätszuschlag für die Vergütung für mehrjährige Tätigkeit und der tarifermäßigt
            zu besteuernden Vorteile bei Vermögensbeteiligungen in Cent
`STS`     : Lohnsteuer für sonstige Bezüge (ohne Vergütung für mehrjährige Tätigkeit
            und ohne tarifermäßigt zu besteuernde Vorteile bei Vermögensbeteiligungen) in Cent
`STV`     : Lohnsteuer für die Vergütung für mehrjährige Tätigkeit und der tarifermäßigt zu
            besteuernden Vorteile bei Vermögensbeteiligungen in Cent
`VKVLZZ`  : Für den Lohnzahlungszeitraum berücksichtigte Beiträge des Arbeitnehmers zur privaten
            Basis-Krankenversicherung und privaten Pflege-Pflichtversicherung (ggf. auch die
            Mindestvorsorgepauschale) in Cent beim laufenden Arbeitslohn. Für Zwecke der
            Lohnsteuerbescheinigung sind die einzelnen Ausgabewerte außerhalb des eigentlichen
            Lohnsteuerberechnungsprogramms zu addieren; hinzuzurechnen sind auch die Ausgabewerte
            `VKVSONST`.
`VKVSONST`: Für den Lohnzahlungszeitraum berücksichtigte Beiträge des Arbeitnehmers zur privaten
            Basis-Krankenversicherung und privaten Pflege-Pflichtversicherung (ggf. auch die
            Mindestvorsorgepauschale) in Cent bei sonstigen Bezügen. Der Ausgabewert kann auch
            negativ sein. Für tarifermäßigt zu besteuernde Vergütungen für mehrjährige Tätigkeiten
            enthält der PAP keinen entsprechenden Ausgabewert.

## Links

- [Bundesministerium für Finanzen](https://www.bmf-steuerrechner.de/interface/einganginterface.xhtml)

## Dependencies

- Python $\geq$ 3.10
- `requests`

import pandas as pd
from enum import Enum
import functools
import operator


class Period(Enum):
    monthly = 1
    quarterly = 3
    semesterly = 6
    yearly = 12
    two_yearly = 24
    four_yearly = 48

    @staticmethod
    def get_period(period, period_unit):
        period_unit = int(period_unit)
        if period_unit == 1 and period == 'Year':
            return Period.yearly
        elif period_unit == 1 and period == 'Month':
            return Period.monthly
        elif period_unit == 2 and period == 'Year':
            return Period.two_yearly
        elif period_unit == 4 and period == 'Year':
            return Period.four_yearly
        else:
            print("period {}, periodUnit {}".format(period, period_unit))
            raise Exception('Invalid period')


class Pricing:

    @classmethod
    def get_obj(cls, currency, period, period_unit, price):
        a_period = Period.get_period(period, period_unit)
        a_value = a_period.value
        print(price, a_value)
        return cls(currency, a_period,
                   price / a_value)

    def __init__(self, currency, period, price) -> None:
        self.currency = currency
        self.period = period
        self.price = price

    def __iter__(self):
        return iter([self.currency, self.period])

    def __hash__(self):
        return functools.reduce(operator.xor, map(hash, self), 0)

    def __eq__(self, other):
        return self.currency == other.currency and self.period == other.period

    def __repr__(self):
        return '"{}":"{}"'.format(self.currency, self.period)


def main1():
    pricing_list = pd.read_excel('/Users/anurag.sh/workspace/SQLDump/temp/pricing.xlsx')
    print(pricing_list)

def main():
    pricing_list = pd.read_excel('/Users/anurag.sh/workspace/SQLDump/temp/pricing.xlsx')
    # print(pricing_list.head(5))
    # print(pricing_list['price'])

    # actual_config = pricing_list[['currency_code', 'period', 'period_unit', 'price']]
    desired_config = set()
    for index, row in pricing_list.iterrows():
        if index > 80:
            break
        desired_config.add(Pricing.get_obj(row['currency_code'], row['period_unit'], row['period'], row['price']))

    print(desired_config)
    curr_pricing = current_pricing()

    curr_config = set()
    for row in curr_pricing:
        add_current_pricing(curr_config, row, 'yearly')
        add_current_pricing(curr_config, row, 'monthly')
        add_current_pricing(curr_config, row, 'quarterly')
        add_current_pricing(curr_config, row, 'semesterly')
        add_current_pricing(curr_config, row, 'two_yearly')
        add_current_pricing(curr_config, row, 'four_yearly')

    print("**************")
    print("**************")
    print("**************")
    print(curr_config)

    print("Difference in config")
    actual_diff = curr_config - desired_config
    currencies = set()
    for a in actual_diff:
        currencies.add(a.currency)
    print(currencies)

    print("Actual Difference in config")
    actual_diff = desired_config - curr_config
    # actual_diff = sorted(actual_diff, key=lambda a: a.currency)
    # print(actual_diff)
    currencies = set()
    for a in actual_diff:
        currencies.add(a.currency)
    print(sorted(currencies))


def add_current_pricing(curr_config, row, period):
    try:
        curr_config.add(Pricing(row['currency'], period, row['billingCyclePriceMap'][period]))
    except KeyError as e:
        print(row['currency'], e)


def current_pricing():
    return [{"currency": "ARS",
             "billingCyclePriceMap": {"yearly": 119, "monthly": 175, "quarterly": 175,
                                      "semesterly": 175,
                                      "two_yearly": 79, "four_yearly": 79}}, {"currency": "BRL",
                                                                              "billingCyclePriceMap": {
                                                                                  "yearly": 5.79,
                                                                                  "monthly": 8.55,
                                                                                  "quarterly": 8.55,
                                                                                  "semesterly": 8.55,
                                                                                  "two_yearly": 3.89,
                                                                                  "four_yearly": 3.85}},
            {"currency": "CNY",
             "billingCyclePriceMap": {"yearly": 10.35, "monthly": 15.25, "quarterly": 15.25,
                                      "semesterly": 15.25, "two_yearly": 6.89,
                                      "four_yearly": 6.89}}, {"currency": "COP",
                                                              "billingCyclePriceMap": {
                                                                  "yearly": 4959,
                                                                  "monthly": 7285,
                                                                  "quarterly": 7285,
                                                                  "semesterly": 7285,
                                                                  "two_yearly": 3295,
                                                                  "four_yearly": 3295}},
            {"currency": "CZK",
             "billingCyclePriceMap": {"yearly": 34.49, "monthly": 50.69, "quarterly": 50.69,
                                      "semesterly": 50.69, "two_yearly": 22.95,
                                      "four_yearly": 22.95}}, {"currency": "DKK",
                                                               "billingCyclePriceMap": {
                                                                   "yearly": 10.05,
                                                                   "monthly": 14.69,
                                                                   "quarterly": 14.69,
                                                                   "semesterly": 14.69,
                                                                   "two_yearly": 6.65,
                                                                   "four_yearly": 6.65}},
            {"currency": "EUR",
             "billingCyclePriceMap": {"yearly": 1.49, "monthly": 2.19, "quarterly": 2.19,
                                      "semesterly": 2.19,
                                      "two_yearly": 0.99, "four_yearly": 0.99}},
            {"currency": "GBP",
             "billingCyclePriceMap": {
                 "yearly": 1.49,
                 "monthly": 2.19,
                 "quarterly": 2.19,
                 "semesterly": 2.19,
                 "two_yearly": 0.99,
                 "four_yearly": 0.99}},
            {"currency": "HRK",
             "billingCyclePriceMap": {"yearly": 9.95, "monthly": 14.59, "quarterly": 14.59,
                                      "semesterly": 14.59, "two_yearly": 6.59,
                                      "four_yearly": 6.59}}, {"currency": "HUF",
                                                              "billingCyclePriceMap": {
                                                                  "yearly": 439,
                                                                  "monthly": 645,
                                                                  "quarterly": 645,
                                                                  "semesterly": 645,
                                                                  "two_yearly": 295,
                                                                  "four_yearly": 295}},
            {"currency": "IDR",
             "billingCyclePriceMap": {"yearly": 21265, "monthly": 31255, "quarterly": 31255,
                                      "semesterly": 31255, "two_yearly": 14129,
                                      "four_yearly": 14129}}, {"currency": "ILS",
                                                               "billingCyclePriceMap": {
                                                                   "yearly": 5.25,
                                                                   "monthly": 7.65,
                                                                   "quarterly": 7.65,
                                                                   "semesterly": 7.65,
                                                                   "two_yearly": 3.49,
                                                                   "four_yearly": 3.49}},
            {"currency": "INR",
             "billingCyclePriceMap": {"yearly": 105, "monthly": 159, "quarterly": 159,
                                      "semesterly": 159,
                                      "two_yearly": 69, "four_yearly": 69}}, {"currency": "JPY",
                                                                              "billingCyclePriceMap": {
                                                                                  "yearly": 159,
                                                                                  "monthly": 235,
                                                                                  "quarterly": 235,
                                                                                  "semesterly": 235,
                                                                                  "two_yearly": 109,
                                                                                  "four_yearly": 109}},
            {"currency": "KRW",
             "billingCyclePriceMap": {"yearly": 1815, "monthly": 2665, "quarterly": 2665,
                                      "semesterly": 2665,
                                      "two_yearly": 1205, "four_yearly": 1205}},
            {"currency": "MXN",
             "billingCyclePriceMap": {
                 "yearly": 35,
                 "monthly": 45,
                 "quarterly": 45,
                 "semesterly": 45,
                 "two_yearly": 19,
                 "four_yearly": 19}},
            {"currency": "MYR",
             "billingCyclePriceMap": {"yearly": 6.25, "monthly": 9.15, "quarterly": 9.15,
                                      "semesterly": 9.15,
                                      "two_yearly": 4.15, "four_yearly": 4.15}},
            {"currency": "NOK",
             "billingCyclePriceMap": {
                 "yearly": 13.35,
                 "monthly": 19.59,
                 "quarterly": 19.59,
                 "semesterly": 19.59,
                 "two_yearly": 8.95,
                 "four_yearly": 8.89}},
            {"currency": "PHP",
             "billingCyclePriceMap": {"yearly": 79, "monthly": 115, "quarterly": 115,
                                      "semesterly": 115,
                                      "two_yearly": 55, "four_yearly": 55}}, {"currency": "PLN",
                                                                              "billingCyclePriceMap": {
                                                                                  "yearly": 5.79,
                                                                                  "monthly": 8.49,
                                                                                  "quarterly": 8.49,
                                                                                  "semesterly": 8.49,
                                                                                  "two_yearly": 3.89,
                                                                                  "four_yearly": 3.85}},
            {"currency": "RUB",
             "billingCyclePriceMap": {"yearly": 99, "monthly": 145, "quarterly": 145,
                                      "semesterly": 145,
                                      "two_yearly": 65, "four_yearly": 65}}, {"currency": "SEK",
                                                                              "billingCyclePriceMap": {
                                                                                  "yearly": 19,
                                                                                  "monthly": 25,
                                                                                  "quarterly": 25,
                                                                                  "semesterly": 25,
                                                                                  "two_yearly": 9,
                                                                                  "four_yearly": 9}},
            {"currency": "THB",
             "billingCyclePriceMap": {"yearly": 49, "monthly": 69, "quarterly": 69,
                                      "semesterly": 69,
                                      "two_yearly": 35, "four_yearly": 35}}, {"currency": "TRY",
                                                                              "billingCyclePriceMap": {
                                                                                  "yearly": 8.35,
                                                                                  "monthly": 12.25,
                                                                                  "quarterly": 12.25,
                                                                                  "semesterly": 12.25,
                                                                                  "two_yearly": 5.55,
                                                                                  "four_yearly": 5.55}},
            {"currency": "UAH",
             "billingCyclePriceMap": {"yearly": 45, "monthly": 59, "quarterly": 59,
                                      "semesterly": 59,
                                      "two_yearly": 29, "four_yearly": 29}}, {"currency": "USD",
                                                                              "billingCyclePriceMap": {
                                                                                  "yearly": 1.49,
                                                                                  "monthly": 2.19,
                                                                                  "quarterly": 2.19,
                                                                                  "semesterly": 2.19,
                                                                                  "two_yearly": 0.99,
                                                                                  "four_yearly": 0.99}},
            {"currency": "VND",
             "billingCyclePriceMap": {"yearly": 34445, "monthly": 50619, "quarterly": 50619,
                                      "semesterly": 50619, "two_yearly": 22885,
                                      "four_yearly": 22885}}, {"currency": "CHF",
                                                               "billingCyclePriceMap": {
                                                                   "yearly": 1.49,
                                                                   "monthly": 2.19,
                                                                   "two_yearly": 0.99,
                                                                   "four_yearly": 0.99}},
            {"currency": "AUD",
             "billingCyclePriceMap": {"yearly": 2.89, "monthly": 4.29, "two_yearly": 1.89,
                                      "four_yearly": 1.89}}]


if __name__ == '__main__':
    main()

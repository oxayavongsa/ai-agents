# quote_estimator.py — quick notary quote: signatures + travel + after-hours.
# Rates below are the ones from my own sheet — update them when yours change.
PER_SIGNATURE = 15     # CA max fee per signature
MILEAGE_RATE = 0.70    # <-- check the current IRS business rate, update here


def travel_fee(miles):
    return miles * MILEAGE_RATE


def after_hours_fee(day, hour):
    # day: "weekday" or "weekend"; hour: 0-23
    day = day.lower()
    if day == "weekday":
        if 17 <= hour < 21:
            return 25
        if 21 <= hour < 22:
            return 50
        if hour >= 22 or hour < 6:
            return 75
    else:  # weekend
        if 8 <= hour < 9:
            return 25
        if 17 <= hour < 21:
            return 25
        if 21 <= hour < 22:
            return 50
        if hour >= 22 or hour < 6:
            return 75
    return 0


def quote(signatures, miles, day, hour, military=False):
    total = signatures * PER_SIGNATURE + travel_fee(miles) + after_hours_fee(day, hour)
    if military:
        total *= 0.9  # 10% off
    return round(total, 2)


if __name__ == "__main__":
    sigs = int(input("Number of signatures: "))
    miles = float(input("One-way miles: "))
    day = input("Weekday or weekend? ")
    hour = int(input("Appointment hour (0-23): "))
    mil = input("Military/veteran discount? (y/n) ").lower().startswith("y")
    print("Quote: $%.2f" % quote(sigs, miles, day, hour, mil))

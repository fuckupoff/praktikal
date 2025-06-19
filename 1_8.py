def date_dict(date_str):
    year, month, day = date_str.split("-")
    return{"year": year,"month": month,"day": day}

date = "2093-10-10"
print(date_dict(date))
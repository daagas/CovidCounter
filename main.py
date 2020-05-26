from covid import Covid

covid = Covid()

def covid_worldwide():
    print(covid.get_total_active_cases())
    print(covid.get_total_confirmed_cases())
    print(covid.get_total_recovered())
    print(covid.get_total_deaths())

covid_worldwide()

country = input("Country ")

spain = covid.get_status_by_country_name(f"{country}")
data = {
    key: spain[key]
    for key in spain.keys() and {'active', 'confirmed', 'recovered', 'deaths'}
}
print(f"{country} data")
print(data)
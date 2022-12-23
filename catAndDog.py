def human_years_cat_years_dog_years(human_years):
    # Your code here
    catYears = 15
    dogYears = 15

    if human_years == 1:
        catYears
        dogYears
    elif human_years == 2:
        catYears += 9
        dogYears += 9
    else:
        catYears = 24 + human_years * 5
        dogYears = 24 + human_years * 5
    
    return [human_years, catYears, dogYears]

print(human_years_cat_years_dog_years(1))
print(human_years_cat_years_dog_years(2))
print(human_years_cat_years_dog_years(10))
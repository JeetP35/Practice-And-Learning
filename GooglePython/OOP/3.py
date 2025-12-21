class PigletAge:
    years = 0
    def pig_years(self):
        return self.years * 18

piggy_age = PigletAge()
piggy_age.years = 2
print(piggy_age.pig_years())

spider_age = PigletAge()
spider_age.years = 3
print(spider_age.pig_years())
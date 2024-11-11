class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12: #add from 0 < age to 0 <= age
            return 50
        elif 13 <= age <= 20: #add from age < 20 to age <= 20
            return 100
        elif 21 <= age <= 60: #add from 21 < age to 21 <= age
            return 150
        elif age >= 60:
            return 100
        else :  #add case: lower than 0 => Invalid age
            return 'Invalid Age'
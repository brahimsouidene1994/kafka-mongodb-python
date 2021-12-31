from faker import Faker

fake = Faker()


def get_registered_user():
    return {
        "name": fake.name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "address": fake.address(),
        "createdAt": fake.year(),
        "phone_number": fake.phone_number()
    }

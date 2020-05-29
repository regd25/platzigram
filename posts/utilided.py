from posts.models import User

user = User.objects.create(
    email='r.galadiaz@gmail.com',
    password = '1234567',
    first_name='Gabriel',
    last_name='Estrada',
    birthdate='1977-01-25',
    country='Mexico',
    city='Merida'
)
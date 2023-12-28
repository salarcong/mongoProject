from decouple import config


URL = 'mongodb+srv://sebsler08:{}@cluster0.trgd3sm.mongodb.net/?retryWrites=true&w=majority'.format(
    config('MONGODB_PASSWORD', default='zKHqZJEzRInAQlFw')
)
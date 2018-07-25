from decouple import config


DB_URL = config("SQLDATABASE")
REDISHOST = config("REDISHOST")
REDISPORT = config("REDISPORT")
TESTDB = config("SQLTEMP")
MAILGUNPASS = config("MAILGUNPASSWORD")
MAILGUNAPI = config("MAILGUNAPI")
STRIPEKEY = config("STRIPEKEY")
REWARDS = {
    'first': [
        {
            "name": "1st Referral One",
            "number": 30,
            "description": "This is the description for the referral",
            "benefits": [
                'benefit1',
                'benefit2',
                'benefit3',
                'benefit4'
            ] 
        },
        {
            "name": "1st Referral Two",
            "number": 100,
            "description": "This is the description for the referral",
            "benefits": [
                'benefit1',
                'benefit2',
                'benefit3',
                'benefit4'
            ]
        },
        {
            "name": "1st Referral Three",
            "number": 150,
            "description": "This is the description for the referral",
            "benefits": [
                'benefit1',
                'benefit2',
                'benefit3',
                'benefit4'
            ]
        }
    ],
    'second': [
        {
            "name": "2nd Referral One",
            "number": 90,
            "description": "This is the description for the referral",
            "benefits": [
                'benefit1',
                'benefit2',
                'benefit3',
                'benefit4'
            ] 
        },
        {
            "name": "2nd Referral Two",
            "number": 300,
            "description": "This is the description for the referral",
            "benefits": [
                'benefit1',
                'benefit2',
                'benefit3',
                'benefit4'
            ] 
        },
        {
            "name": "2nd Referral Three",
            "number": 500,
            "description": "This is the description for the referral",
            "benefits": [
                'benefit1',
                'benefit2',
                'benefit3',
                'benefit4'
            ] 
        }
    ],
    'third': [
        {
            "name": "3rd Referral One",
            "number": 270,
            "description": "This is the description for the referral",
            "benefits": [
                'benefit1',
                'benefit2',
                'benefit3',
                'benefit4'
            ] 
        },
        {
            "name": "3rd Referral Two",
            "number": 1500,
            "description": "This is the description for the referral",
            "benefits": [
                'benefit1',
                'benefit2',
                'benefit3',
                'benefit4'
            ] 
        },
        {
            "name": "3rd Referral Three",
            "number": 2000,
            "description": "This is the description for the referral",
            "benefits": [
                'benefit1',
                'benefit2',
                'benefit3',
                'benefit4'
            ] 
        }
    ]
}
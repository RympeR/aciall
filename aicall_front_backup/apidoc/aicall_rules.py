
"""
    @api {GET} /api/token/logout/ 1.1 Logout
    @apiName 1.1 Logout
    @apiGroup User
    @apiSuccess {String} auth_token  or error

    @apiSuccessExample {json} Success-Response:
    HTTP 200 OK
    Allow: POST, OPTIONS
    Content-Type: application/json
    @apiErrorExample {json} Error-Response:

    HTTP 400 Bad Request
    Allow: POST, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "non_field_errors": [
            "Пользователя  с таким токеном не существует."
        ]
    }
"""
"""
    @api {POST} /api/user/login/ 1.2 Login
    @apiName 1.2 Login
    @apiGroup User


    @apiParam {String} username
    @apiParam {String} password
    @apiParam {String} code

    @apiSuccess {String} auth_token  or error
    @apiSuccessExample {json} Success-Response:

    HTTP 200 OK
    Allow: POST, OPTIONS
    Content-Type: application/json
    Vary: Accept
    {
        "auth_token": "ea69a27ca231c17292d4c1f9db48b8cb2aaa736c"
    }
    @apiErrorExample {json} Error-Response:

    HTTP 400 Bad Request
    Allow: POST, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "non_field_errors": [
            "Невозможно войти с предоставленными учетными данными."
        ]
    }
"""

"""
    @api {GET} /api/user/get-user/{user_id} 1.3 Get user
    @apiName 1.3 Get user
    @apiGroup User
    @apiHeader {String} Authorization Users unique token

    @apiSuccess {Number} id
    @apiSuccess {Number} birthday_date
    @apiSuccess {Number} average_rating Avg user rating
    @apiSuccess {String} email
    @apiSuccess {String} phone
    @apiSuccess {String} username Username in app
    @apiSuccess {String} sex 0-Не выбран 1-Женский 2-Мужской
    @apiSuccess {String} family Family status 0-Свободен, 1-В браке
    @apiSuccess {Boolean} notifications are enabled
    @apiSuccess {Object} country country object
    @apiSuccess {Object} education education object
    @apiSuccess {Object} action_area action_area object
    @apiSuccess {Object} languages languages list

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "birthday_date": 1616511570.0,
        "date_joined": 1616518798.0,
        "average_rating": 5.0,
        "email": "admin@gmail.com",
        "phone": 2345,
        "username": "admin",
        "sex": 0,
        "family": 0,
        "notifications": false,
        "mobile_book_access": false,
        "psycho_type": 5,
        "country": {
            "id": 3,
            "name_ru": "Россия",
            "name_eng": "Russia"
        },
        "education": {
            "id": 4,
            "name_ru": "Магистр",
            "name_eng": "Магистр"
        },
        "action_area": {
            "id": 3,
            "name_ru": "Строительство",
            "name_eng": "Строительство"
        },
        "languages": [
            {
                "id": 2,
                "name_ru": "Русский",
                "name_eng": "Russain"
            },
            {
                "id": 4,
                "name_ru": "Украинский",
                "name_eng": "Ukrainian"
            }
        ]
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 Not Found
    {
        "status": "invalid token"
    }

"""


"""
    @api {PUT} /api/user/update-user/ 1.4 Update user
    @apiName 1.4 Update user
    @apiGroup User
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} id
    @apiParam {Number} birthday_date
    @apiParam {String} email
    @apiParam {Number} phone
    @apiParam {String} username
    @apiParam {String} sex 0-Не выбран 1-Женский 2-Мужской
    @apiParam {String} family Family status 0-Свободен, 1-В браке
    @apiParam {Boolean} notifications are enabled
    @apiParam {Object} country country object
    @apiParam {Object} education education object
    @apiParam {Object} action_area action_area object
    @apiParam {Object} languages languages list

    @apiSuccess {Number} id
    @apiSuccess {Number} birthday_date
    @apiSuccess {String} email
    @apiSuccess {Number} phone
    @apiSuccess {String} username
    @apiSuccess {String} sex 0-Не выбран 1-Женский 2-Мужской
    @apiSuccess {String} family Family status 0-Свободен, 1-В браке
    @apiSuccess {Boolean} notifications are enabled
    @apiSuccess {Object} country country object
    @apiSuccess {Object} education education object
    @apiSuccess {Object} action_area action_area object
    @apiSuccess {Object} languages languages list

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "birthday_date": 1616511570.0,
        "is_active": true,
        "email": "admin@gmail.com",
        "phone": "admin",
        "username": "admin",
        "sex": 0,
        "family": 0,
        "notifications": false,
        "mobile_book_access": false,
        "psycho_type": 5,
        "country": {
                "id": 3,
                "name_ru": "Россия",
                "name_eng": "Russia"
            },
        "education": {
            "id": 4,
            "name_ru": "Магистр",
            "name_eng": "Магистр"
        },
        "action_area": {
            "id": 3,
            "name_ru": "Строительство",
            "name_eng": "Строительство"
        },
        "languages": [
            {
                "id": 2,
                "name_ru": "Русский",
                "name_eng": "Russain"
            },
            {
                "id": 4,
                "name_ru": "Украинский",
                "name_eng": "Ukrainian"
            }
        ]
        
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 Not Found
    {
        "status": "invalid token"
    }
"""

"""
    @api {POST} /api/user/create-contact-phone/ 2.1 Create contact phone  
    @apiName 2.1 Create contact phone
    @apiGroup UserExtensions
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} owner User id
    @apiParam {String} phone User phone


    @apiSuccess {Number} id contact-phone id
    @apiSuccess {String} phone phone string
    @apiSuccess {String} owner user id
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "phone": "1234",
        "owner": 2
    }
"""

"""
    @api {PATCH} /api/user/update-psychotype/{user_id} 2.2 Update user psychotype
    @apiName 2.2 Update user psychotype
    @apiGroup UserExtensions
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} owner User id
    @apiParam {String} phone User phone


    @apiParam {Object} questions array with 12 objects {"id":1,"answer":0},

    @apiSuccess {Number} id
    @apiSuccess {Number} birthday_date
    @apiSuccess {String} email
    @apiSuccess {Number} phone
    @apiSuccess {String} username
    @apiSuccess {String} sex 0-Не выбран 1-Женский 2-Мужской
    @apiSuccess {String} family Family status 0-Свободен, 1-В браке
    @apiSuccess {Boolean} notifications are enabled
    @apiSuccess {Object} country country object
    @apiSuccess {Object} education education object
    @apiSuccess {Object} action_area action_area object
    @apiSuccess {Object} languages languages list
    
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "birthday_date": 1616511570.0,
        "psycho_type": 5,
        "email": "admin@gmail.com",
        "phone": 0953092993,
        "username": "admin",
        "sex": 0,
        "family": 0,
        "notifications": false,
        "country": 3,
        "education": 4,
        "action_area": 3,
        "languages": [
            2,
            4
        ]
    }
"""

"""
    @api {POST} /api/user/create-characteristics/ 3.1 Create characteristics
    @apiName 3.1 Create characteristics
    @apiGroup Characteristics
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} grade grade number
    @apiParam {String} sender_name characteristics name for sender
    @apiParam {Boolean} compatible characteristics compatible?
    @apiParam {Number} sender sender user id
    @apiParam {Number} reciever reciever user id
    @apiParam {Object} positive_sides list of positive_sides id
    @apiParam {Object} negative_sides list of negative_sides id


    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "grade": 3,
                "sender": 1,
                "reciever": 2,
                "sender_name": "1234",
                "reciever_name": "444",
                "compatible": true,
                "positive_sides": [
                    1
                ],
                "negative_sides": [
                    1
                ]
            }
        ]
    }
"""


"""
    @api {GET} /api/info/get-positive-sides 4.1 Get Positive sides    
    @apiName 4.1 Get positive-sides
    @apiGroup Info
    @apiHeader {String} Authorization Users unique token
    @apiSuccess {object} results positive-sides list
    @apiSuccess {Number} id line id
    @apiSuccess {String} name_ru positive-sides name_ru
    @apiSuccess {String} name_eng positive-sides name_eng
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "name_ru": "22",
                "name_eng": "222"
            }
        ]
    }
"""

"""
    @api {GET} /api/info/get-negative-sides 4.2 Get negative sides    
    @apiName 4.2 Get negative-sides
    @apiGroup Info
    @apiSuccess {object} results negative-sides list
    @apiSuccess {Number} id negative-side id
    @apiSuccess {String} name_ru negative-sides name_ru
    @apiSuccess {String} name_eng negative-sides name_eng
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "name_ru": "test",
                "name_eng": "tet"
            }
        ]
    }
"""

"""
    @api {GET} /api/info/get-countries 4.3 Get countries    
    @apiName 4.3 Get countries
    @apiGroup Info
    @apiSuccess {object} results countries list
    @apiSuccess {Number} id countries id
    @apiSuccess {String} name_ru countries name_ru
    @apiSuccess {String} name_eng countries name_eng
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "name_ru": "Украина",
                "name_eng": "Ukraine"
            },
            {
                "id": 3,
                "name_ru": "Россия",
                "name_eng": "Russia"
            }
        ]
    }
"""

"""
    @api {GET} /api/info/get-action-areas 4.4 Get action-areas    
    @apiName 4.4 Get action areas
    @apiGroup Info
    @apiSuccess {object} results action areas list
    @apiSuccess {Number} id action areas id
    @apiSuccess {String} name_ru action areas name_ru
    @apiSuccess {String} name_eng action areas name_eng
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "name_ru": "Бизнес",
                "name_eng": "Бизнес"
            },
            {
                "id": 3,
                "name_ru": "Строительство",
                "name_eng": "Строительство"
            },
            {
                "id": 4,
                "name_ru": "Медицина",
                "name_eng": "Медицина"
            }
        ]
    }
"""

"""
    @api {GET} /api/info/get-languages 4.5 Get languages    
    @apiName 4.5 Get languages
    @apiGroup Info
    @apiSuccess {object} results languages list
    @apiSuccess {Number} id languages id
    @apiSuccess {String} name_ru languages name_ru
    @apiSuccess {String} name_eng languages name_eng
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "name_ru": "Русский",
                "name_eng": "Russain"
            },
            {
                "id": 3,
                "name_ru": "Английский",
                "name_eng": "English"
            },
            {
                "id": 4,
                "name_ru": "Украинский",
                "name_eng": "Ukrainian"
            }
        ]
    }
"""

"""
    @api {GET} /api/info/get-educations 4.6 Get educations    
    @apiName 4.6 Get educations
    @apiGroup Info
    @apiSuccess {object} results educations list
    @apiSuccess {Number} id educations id
    @apiSuccess {String} name_ru educations name_ru
    @apiSuccess {String} name_eng educations name_eng
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "count": 4,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "name_ru": "Высшее",
                "name_eng": "Высшее"
            },
            {
                "id": 3,
                "name_ru": "Среднее",
                "name_eng": "Среднее"
            },
            {
                "id": 4,
                "name_ru": "Магистр",
                "name_eng": "Магистр"
            },
            {
                "id": 5,
                "name_ru": "Незаконченное высшее",
                "name_eng": "Незаконченное высшее"
            }
        ]
    }
"""

"""
    @api {GET} /api/info/get-talk-themes 4.7 Get talk themes    
    @apiName 4.6 Get talk themes   
    @apiGroup Info
    @apiSuccess {object} results talk themes list
    @apiSuccess {Number} id talk theme id
    @apiSuccess {String} name_ru talk theme name_ru
    @apiSuccess {String} name_eng talk theme name_eng
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "image_png": null,
                "image_svg": null,
                "name_ru": "Дети",
                "name_eng": "Children"
            },
            {
                "id": 1,
                "image_png": "http://api-aicall.maximusapp.com/media/image_2021-03-19_15-53-06.png",
                "image_svg": null,
                "name_ru": "Отношения",
                "name_eng": "Relationship"
            }
        ]
    }
"""


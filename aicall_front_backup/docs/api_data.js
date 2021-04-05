define({ "api": [
  {
    "type": "POST",
    "url": "/api/user/create-characteristics/",
    "title": "3.1 Create characteristics",
    "name": "3.1_Create_characteristics",
    "group": "Characteristics",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "grade",
            "description": "<p>grade number</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "sender_name",
            "description": "<p>characteristics name for sender</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "compatible",
            "description": "<p>characteristics compatible?</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "sender",
            "description": "<p>sender user id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "reciever",
            "description": "<p>reciever user id</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "positive_sides",
            "description": "<p>list of positive_sides id</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "negative_sides",
            "description": "<p>list of negative_sides id</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"count\": 1,\n    \"next\": null,\n    \"previous\": null,\n    \"results\": [\n        {\n            \"id\": 1,\n            \"grade\": 3,\n            \"sender_name\": \"1234\",\n            \"reciever_name\": \"444\",\n            \"compatible\": true,\n            \"sender\": 1,\n            \"reciever\": 2,\n            \"positive_sides\": [\n                1\n            ],\n            \"negative_sides\": [\n                1\n            ]\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "Characteristics"
  },
  {
    "type": "GET",
    "url": "/api/info/get-positive-sides",
    "title": "4.1 Get Positive sides",
    "name": "4.1_Get_positive-sides",
    "group": "Info",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>positive-sides list</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>line id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_ru",
            "description": "<p>positive-sides name_ru</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_eng",
            "description": "<p>positive-sides name_eng</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"count\": 1,\n    \"next\": null,\n    \"previous\": null,\n    \"results\": [\n        {\n            \"id\": 1,\n            \"name_ru\": \"22\",\n            \"name_eng\": \"222\"\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "Info"
  },
  {
    "type": "GET",
    "url": "/api/info/get-negative-sides",
    "title": "4.2 Get negative sides",
    "name": "4.2_Get_negative-sides",
    "group": "Info",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>negative-sides list</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>negative-side id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_ru",
            "description": "<p>negative-sides name_ru</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_eng",
            "description": "<p>negative-sides name_eng</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"count\": 1,\n    \"next\": null,\n    \"previous\": null,\n    \"results\": [\n        {\n            \"id\": 1,\n            \"name_ru\": \"test\",\n            \"name_eng\": \"tet\"\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "Info"
  },
  {
    "type": "GET",
    "url": "/api/info/get-countries",
    "title": "4.3 Get countries",
    "name": "4.3_Get_countries",
    "group": "Info",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>countries list</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>countries id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_ru",
            "description": "<p>countries name_ru</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_eng",
            "description": "<p>countries name_eng</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"count\": 2,\n    \"next\": null,\n    \"previous\": null,\n    \"results\": [\n        {\n            \"id\": 2,\n            \"name_ru\": \"Украина\",\n            \"name_eng\": \"Ukraine\"\n        },\n        {\n            \"id\": 3,\n            \"name_ru\": \"Россия\",\n            \"name_eng\": \"Russia\"\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "Info"
  },
  {
    "type": "GET",
    "url": "/api/info/get-action-areas",
    "title": "4.4 Get action-areas",
    "name": "4.4_Get_action_areas",
    "group": "Info",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>action areas list</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>action areas id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_ru",
            "description": "<p>action areas name_ru</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_eng",
            "description": "<p>action areas name_eng</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"count\": 3,\n    \"next\": null,\n    \"previous\": null,\n    \"results\": [\n        {\n            \"id\": 2,\n            \"name_ru\": \"Бизнес\",\n            \"name_eng\": \"Бизнес\"\n        },\n        {\n            \"id\": 3,\n            \"name_ru\": \"Строительство\",\n            \"name_eng\": \"Строительство\"\n        },\n        {\n            \"id\": 4,\n            \"name_ru\": \"Медицина\",\n            \"name_eng\": \"Медицина\"\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "Info"
  },
  {
    "type": "GET",
    "url": "/api/info/get-languages",
    "title": "4.5 Get languages",
    "name": "4.5_Get_languages",
    "group": "Info",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>languages list</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>languages id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_ru",
            "description": "<p>languages name_ru</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_eng",
            "description": "<p>languages name_eng</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"count\": 3,\n    \"next\": null,\n    \"previous\": null,\n    \"results\": [\n        {\n            \"id\": 2,\n            \"name_ru\": \"Русский\",\n            \"name_eng\": \"Russain\"\n        },\n        {\n            \"id\": 3,\n            \"name_ru\": \"Английский\",\n            \"name_eng\": \"English\"\n        },\n        {\n            \"id\": 4,\n            \"name_ru\": \"Украинский\",\n            \"name_eng\": \"Ukrainian\"\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "Info"
  },
  {
    "type": "GET",
    "url": "/api/info/get-educations",
    "title": "4.6 Get educations",
    "name": "4.6_Get_educations",
    "group": "Info",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>educations list</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>educations id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_ru",
            "description": "<p>educations name_ru</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_eng",
            "description": "<p>educations name_eng</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"count\": 4,\n    \"next\": null,\n    \"previous\": null,\n    \"results\": [\n        {\n            \"id\": 2,\n            \"name_ru\": \"Высшее\",\n            \"name_eng\": \"Высшее\"\n        },\n        {\n            \"id\": 3,\n            \"name_ru\": \"Среднее\",\n            \"name_eng\": \"Среднее\"\n        },\n        {\n            \"id\": 4,\n            \"name_ru\": \"Магистр\",\n            \"name_eng\": \"Магистр\"\n        },\n        {\n            \"id\": 5,\n            \"name_ru\": \"Незаконченное высшее\",\n            \"name_eng\": \"Незаконченное высшее\"\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "Info"
  },
  {
    "type": "GET",
    "url": "/api/info/get-talk-themes",
    "title": "4.7 Get talk themes",
    "name": "4.6_Get_talk_themes",
    "group": "Info",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>talk themes list</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>talk theme id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_ru",
            "description": "<p>talk theme name_ru</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name_eng",
            "description": "<p>talk theme name_eng</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"count\": 2,\n    \"next\": null,\n    \"previous\": null,\n    \"results\": [\n        {\n            \"id\": 2,\n            \"image_png\": null,\n            \"image_svg\": null,\n            \"name_ru\": \"Дети\",\n            \"name_eng\": \"Children\"\n        },\n        {\n            \"id\": 1,\n            \"image_png\": \"http://api-aicall.maximusapp.com/media/image_2021-03-19_15-53-06.png\",\n            \"image_svg\": null,\n            \"name_ru\": \"Отношения\",\n            \"name_eng\": \"Relationship\"\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "Info"
  },
  {
    "type": "POST",
    "url": "/api/user/login/",
    "title": "1.2 Login",
    "name": "1.2_Login",
    "group": "User",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "auth_token",
            "description": "<p>or error</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP 200 OK\nAllow: POST, OPTIONS\nContent-Type: application/json\nVary: Accept\n{\n    \"auth_token\": \"ea69a27ca231c17292d4c1f9db48b8cb2aaa736c\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "\nHTTP 400 Bad Request\nAllow: POST, OPTIONS\nContent-Type: application/json\nVary: Accept\n\n{\n    \"non_field_errors\": [\n        \"Невозможно войти с предоставленными учетными данными.\"\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "User"
  },
  {
    "type": "GET",
    "url": "/api/user/api-profile-get/",
    "title": "1.3 Get user",
    "name": "1.3_Get_user",
    "group": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "birthday_date",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_superuser",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_staff",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "avatar",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "sex",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "family",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "notifications",
            "description": "<p>are enabled</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "country",
            "description": "<p>country object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "education",
            "description": "<p>education object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "action_area",
            "description": "<p>action_area object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "languages",
            "description": "<p>languages list</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"birthday_date\": 1616511570.0,\n    \"is_superuser\": true,\n    \"last_name\": \"\",\n    \"is_staff\": true,\n    \"is_active\": true,\n    \"email\": \"admin@gmail.com\",\n    \"phone\": \"admin\",\n    \"avatar\": null,\n    \"username\": \"admin\",\n    \"first_name\": null,\n    \"sex\": 0,\n    \"family\": 0,\n    \"notifications\": false,\n    \"country\": {\n            \"id\": 3,\n            \"name_ru\": \"Россия\",\n            \"name_eng\": \"Russia\"\n        },\n    \"education\": {\n        \"id\": 4,\n        \"name_ru\": \"Магистр\",\n        \"name_eng\": \"Магистр\"\n    },\n    \"action_area\": {\n        \"id\": 3,\n        \"name_ru\": \"Строительство\",\n        \"name_eng\": \"Строительство\"\n    },\n    \"languages\": [\n        {\n            \"id\": 2,\n            \"name_ru\": \"Русский\",\n            \"name_eng\": \"Russain\"\n        },\n        {\n            \"id\": 4,\n            \"name_ru\": \"Украинский\",\n            \"name_eng\": \"Ukrainian\"\n        }\n    ],\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Not Found\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "User"
  },
  {
    "type": "PUT",
    "url": "/api/user/update-user/",
    "title": "1.4 Update user",
    "name": "1.4_Update_user",
    "group": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "birthday_date",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_superuser",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_staff",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "avatar",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "sex",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "family",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "notifications",
            "description": "<p>are enabled</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "country",
            "description": "<p>country object</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "education",
            "description": "<p>education object</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "action_area",
            "description": "<p>action_area object</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "languages",
            "description": "<p>languages list</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "birthday_date",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_superuser",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_staff",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "avatar",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "sex",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "family",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "notifications",
            "description": "<p>are enabled</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "country",
            "description": "<p>country object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "education",
            "description": "<p>education object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "action_area",
            "description": "<p>action_area object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "languages",
            "description": "<p>languages list</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"birthday_date\": 1616511570.0,\n    \"is_superuser\": true,\n    \"last_name\": \"\",\n    \"is_staff\": true,\n    \"is_active\": true,\n    \"email\": \"admin@gmail.com\",\n    \"phone\": \"admin\",\n    \"avatar\": null,\n    \"username\": \"admin\",\n    \"first_name\": null,\n    \"sex\": 0,\n    \"family\": 0,\n    \"notifications\": false,\n    \"country\": {\n            \"id\": 3,\n            \"name_ru\": \"Россия\",\n            \"name_eng\": \"Russia\"\n        },\n    \"education\": {\n        \"id\": 4,\n        \"name_ru\": \"Магистр\",\n        \"name_eng\": \"Магистр\"\n    },\n    \"action_area\": {\n        \"id\": 3,\n        \"name_ru\": \"Строительство\",\n        \"name_eng\": \"Строительство\"\n    },\n    \"languages\": [\n        {\n            \"id\": 2,\n            \"name_ru\": \"Русский\",\n            \"name_eng\": \"Russain\"\n        },\n        {\n            \"id\": 4,\n            \"name_ru\": \"Украинский\",\n            \"name_eng\": \"Ukrainian\"\n        }\n    ],\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Not Found\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "User"
  },
  {
    "type": "POST",
    "url": "/api/user/create-contact-phone/",
    "title": "2.1 Create contact phone",
    "name": "2.1_Create_contact_phone",
    "group": "UserExtensions",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "owner",
            "description": "<p>User id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>User phone</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>contact-phone id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>phone string</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "owner",
            "description": "<p>user id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"phone\": \"1234\",\n    \"owner\": 2\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "UserExtensions"
  },
  {
    "type": "PATCH",
    "url": "/api/user/update-psychotype/{user_id}",
    "title": "2.2 Update user psychotype",
    "name": "2.2_Update_user_psychotype",
    "group": "UserExtensions",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "owner",
            "description": "<p>User id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>User phone</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "questions",
            "description": "<p>array with 12 objects {&quot;id&quot;:1,&quot;answer&quot;:0},</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"birthday_date\": 1616511570.0,\n    \"psycho_type\": {\n        \"id\": 5,\n        \"shortcode\": \"ENFJ\",\n        \"name_ru\": \"5\",\n        \"name_eng\": \"5\",\n        \"description_ru\": \"5\",\n        \"description_eng\": \"5\"\n    },\n    \"is_superuser\": true,\n    \"last_name\": \"\",\n    \"is_staff\": true,\n    \"is_active\": true,\n    \"email\": \"admin@gmail.com\",\n    \"phone\": \"admin\",\n    \"avatar\": null,\n    \"username\": \"admin\",\n    \"first_name\": null,\n    \"sex\": 0,\n    \"family\": 0,\n    \"notifications\": false,\n    \"country\": 3,\n    \"education\": 4,\n    \"action_area\": 3,\n    \"languages\": [\n        2,\n        4\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/aicall_rules.py",
    "groupTitle": "UserExtensions"
  }
] });
